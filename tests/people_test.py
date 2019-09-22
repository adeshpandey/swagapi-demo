import pytest
from swagapi_demo import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    yield client

def test_people(client):
    rv = client.get('/api/people')
    assert rv.status_code == 200
