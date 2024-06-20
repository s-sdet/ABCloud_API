import logging
import pytest
import requests
from data.data import Auth
from data.constants import ISNotice, EnvNotice
from fixtures.app import App


logger = logging.getLogger("ABCloud API")


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        default="https://***.akbars.ru/",
        help="ABCloud API",
    )


@pytest.fixture
def app(request):
    url = request.config.getoption('--api-url')
    logger.info(f"Start API tests ABCloud, url is {url}")
    return App(url)


@pytest.fixture
def auth(app):
    """Фикстура получения токена."""
    url_dex = "https://dex.dev-int.akbars.ru/token"

    payload = {'client_id': Auth.client_id,
               'client_secret': Auth.client_secret_key,
               'grant_type': Auth.grant_type,
               'username': Auth.login,
               'password': Auth.password,
               'scope': Auth.scope}

    res = requests.request("POST", url_dex, data=payload, verify=False)
    token = res.json()['id_token']

    headers = {
        'Content-Type': 'application/yaml',
        'Authorization': f'Bearer {token}'
    }
    return headers

@pytest.fixture
def auth_ui(app):
    """Фикстура получения токена."""
    url_dex = "https://dex.dev-int.akbars.ru/token"

    payload = {'client_id': Auth.client_id,
               'client_secret': Auth.client_secret_key,
               'grant_type': Auth.grant_type,
               'username': Auth.login,
               'password': Auth.password,
               'scope': Auth.scope}

    res = requests.request("POST", url_dex, data=payload, verify=False)
    token = res.json()['id_token']

    headers = {
        'Authorization': f'Bearer {token}'
    }
    return headers


@pytest.fixture
def create_is(app, auth):
    """Фикстура создания namespace."""
    app.info_system.create_is(
        header=auth,
        businessname=ISNotice.BUSINESS_NAME[:12],
        description=ISNotice.DESCRIPTION[:19]
    )


@pytest.fixture
def create_env(app, auth, response_code=201):
    """Фикстура создания environment."""
    res = app.env.create_env(
        ns_is=EnvNotice.IS,
        header=auth,
        data=EnvNotice.ENV_NAME_LENGTH_3_ENGLISH,
    )
    assert res.status_code == response_code
    logger.info(f"Environment '{res.json()['metadata']['name']}' created. Status code: {res.status_code}")
