import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_contact_get(client):
    """Test if the form loads correctly on GET request"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Contact Form' in response.data
    assert b'First name:' in response.data
    assert b'Last name:' in response.data
    assert b'Password:' in response.data
    assert b'Enter Your E-mail' in response.data

def test_contact_post(client):
    """Test if form submission works on POST request"""
    form_data = {
        'Firstname': 'Alice',
        'lastname': 'Smith',
        'pwd': 'SecretPass123',
        'Gender': 'Female',
        'email': 'alice@example.com'
    }
    response = client.post('/', data=form_data)
    assert response.status_code == 200
    assert b'Alice' in response.data
    assert b'Smith' in response.data
    assert b'Female' in response.data
    assert b'alice@example.com' in response.data
