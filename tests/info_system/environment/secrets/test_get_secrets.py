from common.deco import log


class TestsSecrets:
    """Тесты для проверки Secrets."""

    @log('Получение списка Secrets')
    def test_get_secrets(self, app, auth):
        """Получение списка Secrets."""
        res = app.secrets.get(url_api="api/v1/namespaces/is4-autotest/secrets", header=auth)
        assert res.status_code == 200
        return res
