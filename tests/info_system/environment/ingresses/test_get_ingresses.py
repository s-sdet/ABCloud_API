from common.deco import log


class TestsIngresses:
    """Тесты для проверки Ingresses."""

    @log('Получение списка Ingresses')
    def test_get_ingresses(self, app, auth):
        """Получение списка Ingresses."""
        res = app.ingresses.get(url_api="apis/networking.k8s.io/v1/namespaces/is4-autotest/ingresses", header=auth)
        assert res.status_code == 200
        return res
