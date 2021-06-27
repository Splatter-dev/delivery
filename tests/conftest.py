import pytest
from delivery.app import create_app


@pytest.fixture(scope="module")
def app():
    """app [Instance of Flask app]

    Returns:
        [app]: [app delivery]
    """
    return create_app()
