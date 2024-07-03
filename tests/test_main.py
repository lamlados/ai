from app.main import get_response

def test_get_response():
    prompt = "Hello, how can I assist you today?"
    response = get_response(prompt)
    assert isinstance(response, str)
    assert len(response) > 0