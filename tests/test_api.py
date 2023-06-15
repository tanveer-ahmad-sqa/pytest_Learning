import pytest
import requests


@pytest.mark.apiTesting
@pytest.mark.api
def test_get_method():

    # Arrange
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Act
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 200

