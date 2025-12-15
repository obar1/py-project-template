import pytest


from src import APP_DESCRIPTION, APP_NAME


@pytest.fixture(scope="session")
def app_config():
    return {
        "app_name": APP_NAME,
        "app_description": APP_DESCRIPTION,
    }
