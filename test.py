import pytest
from main import get_cat

def test_get_cat_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
  {
    "id": "dlo",
    "url": "https://cdn2.thecatapi.com/images/dlo.jpg",
    "width": 640,
    "height": 426
  }
]

    cat_data = get_cat()

    assert cat_data == [
  {
    "id": "dlo",
    "url": "https://cdn2.thecatapi.com/images/dlo.jpg",
    "width": 640,
    "height": 426
  }
]

def test_get_cat_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    cat_data = get_cat()

    assert cat_data == None