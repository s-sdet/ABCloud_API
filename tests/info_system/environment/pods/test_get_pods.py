from common.deco import log


class TestsPods:
    """Тесты для проверки Pods."""

    def test_get_pods(self, app, auth):
        """Получение списка Pods."""
        res = app.pods.get(
            header=auth
        ).json()
        return res
