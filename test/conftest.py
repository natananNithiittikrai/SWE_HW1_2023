import pytest

from app import start


@pytest.fixture()
def app():
    app = start()
    # app.config["WTF_CSRF_ENABLED"] = False
    app.config.update(
        {
            "SECRET_KEY": "dev",
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
