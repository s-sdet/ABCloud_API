import logging

logger = logging.getLogger("ABCloud API")


class TestDeleteIS:
    """Тесты для удаления информационных систем."""

    def test_delete_is(self, app, auth):
        """Удаление Информационной ситемы."""
        res = app.info_system.delete(
            url_api="apis/paas.akbars.tech/v1/informationsystems/paas",
            header=auth,
        )
        assert res.status_code == 200
