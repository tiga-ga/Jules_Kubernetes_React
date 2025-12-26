from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__, static_folder='frontend/dist')

# Database Configuration
# In Minikube, the service name 'postgres-service' resolves to the cluster IP
db_user = os.environ.get('POSTGRES_USER', 'user')
db_password = os.environ.get('POSTGRES_PASSWORD', 'password')
db_host = os.environ.get('POSTGRES_HOST', 'postgres-service')
db_name = os.environ.get('POSTGRES_DB', 'output_db')

if os.environ.get('FLASK_ENV') == 'test':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Data Model
class Output(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(50), nullable=False) # 'zenn', 'youtube', 'other'
    published_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "type": self.type,
            "published_date": self.published_date.isoformat() if self.published_date else None,
            "created_at": self.created_at.isoformat()
        }

# Routes
@app.route('/api/outputs', methods=['GET'])
def get_outputs():
    outputs = Output.query.order_by(Output.published_date.desc()).all()
    return jsonify([output.to_dict() for output in outputs])

@app.route('/api/outputs', methods=['POST'])
def add_output():
    data = request.json
    try:
        new_output = Output(
            title=data['title'],
            url=data['url'],
            type=data['type'],
            published_date=datetime.strptime(data['published_date'], '%Y-%m-%d').date() if data.get('published_date') else None
        )
        db.session.add(new_output)
        db.session.commit()
        return jsonify(new_output.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/outputs/<int:id>', methods=['DELETE'])
def delete_output(id):
    output = Output.query.get_or_404(id)
    db.session.delete(output)
    db.session.commit()
    return jsonify({"message": "Output deleted successfully"})

# Static Files
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    # Initialize Database only when running the app directly
    with app.app_context():
        try:
            db.create_all()
            print("Database initialized successfully.")
        except Exception as e:
            print(f"Error initializing database: {e}")

    app.run(host='0.0.0.0', port=5000)
