import pytest
from app import app, db, Output
from datetime import date

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Use in-memory SQLite for testing

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_get_outputs_empty(client):
    rv = client.get('/api/outputs')
    assert rv.status_code == 200
    assert rv.json == []

def test_add_output(client):
    new_output = {
        "title": "Test Blog",
        "url": "http://example.com",
        "type": "blog",
        "published_date": "2023-10-27"
    }
    rv = client.post('/api/outputs', json=new_output)
    assert rv.status_code == 201
    assert rv.json['title'] == "Test Blog"

    rv = client.get('/api/outputs')
    assert len(rv.json) == 1
    assert rv.json[0]['title'] == "Test Blog"

def test_delete_output(client):
    new_output = {
        "title": "To Delete",
        "url": "http://example.com/delete",
        "type": "other",
        "published_date": "2023-10-27"
    }
    rv = client.post('/api/outputs', json=new_output)
    output_id = rv.json['id']

    rv = client.delete(f'/api/outputs/{output_id}')
    assert rv.status_code == 200

    rv = client.get('/api/outputs')
    assert rv.json == []
