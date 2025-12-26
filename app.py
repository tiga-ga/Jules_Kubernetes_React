import os
import datetime
from flask import Flask, jsonify, request, send_from_directory
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import sqlite3

load_dotenv()

app = Flask(__name__, static_folder='frontend/dist')

# Database configuration
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'outputs_db')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
FLASK_ENV = os.getenv('FLASK_ENV', 'development')

def get_db_connection():
    if FLASK_ENV == 'test':
        # Use a file-based DB for persistence during manual testing in this environment
        conn = sqlite3.connect('test.db')
        conn.row_factory = sqlite3.Row
        return conn
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def init_db():
    conn = get_db_connection()
    if conn is None:
        return

    # Create table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS outputs (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        url TEXT NOT NULL,
        content_type VARCHAR(50) NOT NULL,
        published_at DATE NOT NULL,
        comment TEXT,
        created_at TIMESTAMP DEFAULT NOW(),
        updated_at TIMESTAMP DEFAULT NOW()
    );
    """

    # SQLite syntax adjustment if needed
    if FLASK_ENV == 'test':
        create_table_query = """
        CREATE TABLE IF NOT EXISTS outputs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            content_type TEXT NOT NULL,
            published_at DATE NOT NULL,
            comment TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

    try:
        cur = conn.cursor()
        cur.execute(create_table_query)
        conn.commit()
        cur.close()
        conn.close()
        print("Database initialized.")
    except Exception as e:
        print(f"Error initializing database: {e}")

# Initialize DB on start
init_db()

# --- API Endpoints ---

@app.route('/api/outputs', methods=['GET'])
def get_outputs():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        if FLASK_ENV == 'test':
            cur = conn.cursor()
        else:
            cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("SELECT * FROM outputs ORDER BY published_at DESC")
        outputs = cur.fetchall()

        # Convert to dict list if SQLite
        if FLASK_ENV == 'test':
             outputs = [dict(row) for row in outputs]

        cur.close()
        conn.close()
        return jsonify(outputs)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/outputs', methods=['POST'])
def create_output():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    required_fields = ['title', 'url', 'content_type', 'published_at']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cur = conn.cursor()
        query = """
            INSERT INTO outputs (title, url, content_type, published_at, comment)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id;
        """
        # SQLite placeholders are ?
        if FLASK_ENV == 'test':
             query = """
                INSERT INTO outputs (title, url, content_type, published_at, comment)
                VALUES (?, ?, ?, ?, ?)
            """

        params = (data['title'], data['url'], data['content_type'], data['published_at'], data.get('comment', ''))

        cur.execute(query, params)

        if FLASK_ENV == 'test':
            output_id = cur.lastrowid
        else:
            output_id = cur.fetchone()['id'] if isinstance(cur, RealDictCursor) else cur.fetchone()[0]

        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"id": output_id, "message": "Output created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/outputs/<int:id>', methods=['PUT'])
def update_output(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cur = conn.cursor()

        # We need to construct the update query dynamically or fetch existing first
        # For simplicity, let's update fields that are present
        fields = []
        params = []
        for key in ['title', 'url', 'content_type', 'published_at', 'comment']:
            if key in data:
                if FLASK_ENV == 'test':
                    fields.append(f"{key} = ?")
                else:
                    fields.append(f"{key} = %s")
                params.append(data[key])

        if not fields:
             return jsonify({"error": "No fields to update"}), 400

        params.append(id)

        query = f"UPDATE outputs SET {', '.join(fields)}, updated_at = NOW() WHERE id = "
        if FLASK_ENV == 'test':
             query = f"UPDATE outputs SET {', '.join(fields)}, updated_at = CURRENT_TIMESTAMP WHERE id = ?"
        else:
             query += "%s"

        cur.execute(query, tuple(params))
        conn.commit()

        if cur.rowcount == 0:
            cur.close()
            conn.close()
            return jsonify({"error": "Output not found"}), 404

        cur.close()
        conn.close()
        return jsonify({"id": id, "message": "Output updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/outputs/<int:id>', methods=['DELETE'])
def delete_output(id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cur = conn.cursor()
        query = "DELETE FROM outputs WHERE id = "
        if FLASK_ENV == 'test':
            query += "?"
        else:
            query += "%s"

        cur.execute(query, (id,))
        conn.commit()

        if cur.rowcount == 0:
             cur.close()
             conn.close()
             return jsonify({"error": "Output not found"}), 404

        cur.close()
        conn.close()
        return jsonify({"message": "Output deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
