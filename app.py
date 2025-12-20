from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='frontend/dist')

@app.route('/api/feeds')
def get_feeds():
    # Mock data for YouTube and Blog entries
    data = [
        {
            "type": "youtube",
            "title": "Introduction to Kubernetes",
            "url": "https://www.youtube.com/watch?v=PH-2FfFD2PU",
            "thumbnail": "https://img.youtube.com/vi/PH-2FfFD2PU/mqdefault.jpg",
            "description": "Learn the basics of Kubernetes in this introductory video.",
            "date": "2023-10-01"
        },
        {
            "type": "blog",
            "title": "React Hooks Explained",
            "url": "https://reactjs.org/docs/hooks-intro.html",
            "thumbnail": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png",
            "description": "A comprehensive guide to using Hooks in React.",
            "date": "2023-10-05"
        },
        {
            "type": "youtube",
            "title": "Flask API Development",
            "url": "https://www.youtube.com/watch?v=GMppyAPbLYk",
            "thumbnail": "https://img.youtube.com/vi/GMppyAPbLYk/mqdefault.jpg",
            "description": "Build a REST API using Flask and Python.",
            "date": "2023-10-10"
        },
        {
            "type": "blog",
            "title": "Dockerizing Your App",
            "url": "https://docs.docker.com/get-started/",
            "thumbnail": "https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png",
            "description": "Step-by-step guide to containerizing applications with Docker.",
            "date": "2023-10-15"
        }
    ]
    return jsonify(data)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
