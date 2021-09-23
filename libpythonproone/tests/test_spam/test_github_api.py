from unittest.mock import Mock

import pytest

from libpythonproone import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/52388350?v=4'
    resp_mock.json.return_value = {
        'login': 'emanuelfilipes', 'id': 52388350,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonproone.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('emanuelfilipes')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('emanuelfilipes')
    assert 'https://avatars.githubusercontent.com/u/52388350?v=4' == url  # mudar conforme aula de isolamento
