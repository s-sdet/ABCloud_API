from common.deco import log


class TestsServices:
    """Тесты для проверки Services."""

    @log('Получение списка Services')
    def test_get_secrets(self, app, auth):
        """Получение списка Services."""
        res = app.services.get(url_api="api/v1/namespaces/is4-autotest/services", header=auth)
        assert res.status_code == 200
        return res
