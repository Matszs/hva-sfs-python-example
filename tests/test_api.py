# Set path so
import sys
sys.path.append("..")
from api.amsterdam_api import AmsterdamApi


def test_api_path():
    amsterdam_api = AmsterdamApi()
    assert amsterdam_api.get_api_path() == "https://api.data.amsterdam.nl/", "Should be https://api.data.amsterdam.nl/"


if __name__ == "__main__":
    test_api_path()
    print("Everything passed")