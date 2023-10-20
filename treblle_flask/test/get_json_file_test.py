from . import get_json_file

## ensure the json file is present in the test directory
## it does not work with the same directory config as the server


def test_fetch_json_file():
    assert get_json_file() is not None


def test_unpack_json_file():
    assert len(get_json_file()) == 3
