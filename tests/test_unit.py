from app import app

def test_homepage():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b'Contact Form' in response.data
