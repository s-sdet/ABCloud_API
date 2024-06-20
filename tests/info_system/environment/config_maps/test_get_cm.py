from common.deco import log


class TestsPods:
    """Тесты для проверки Config Maps."""

    @log('Получение списка Config Maps')
    def test_get_configmaps(self, app, auth):
        """Получение списка Config Maps."""
        res = app.cm.get(url_api="api/v1/namespaces/is4-autotest/configmaps", header=auth)
        assert res.status_code == 200
        return res
