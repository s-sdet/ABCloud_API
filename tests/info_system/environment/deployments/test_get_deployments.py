from common.deco import log


class TestsDeployments:
    """Тесты для проверки Deployments."""

    @log('Получение списка Deployments')
    def test_get_deployments(self, app, auth):
        """Получение списка Deployments."""
        res = app.deployments.get(url_api="apis/apps/v1/namespaces/is4-autotest/deployments", header=auth)
        assert res.status_code == 200
        return res
