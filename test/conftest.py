import pytest

from app import start


@pytest.fixture()
def app():
    app = start()

    app.config.update(
        {
            "SECRET_KEY": "dev",
            "TESTING": True,
        }
    )
    app.config["WTF_CSRF_ENABLED"] = False

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
