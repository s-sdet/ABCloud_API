import logging
import pytest
from pytest_testrail.plugin import pytestrail
from data.constants import EnvNotice
from fixtures.info_system.environment.api import Env
from fixtures.assertions import Assertions

logger = logging.getLogger("ABCloud API")


class TestDeleteEnv:
    """Тесты для проверок удаления конутра."""

    @pytestrail.case("C16667402")
    @pytest.mark.xfail(reason="GET запрос к /api/v1/ пока отдает 200 ответ, так как нет консестентного удаления Env")
    def test_delete_invalid_environment(self, app, auth):
        """Удаление несуществующего контура."""
        res = app.env.delete(
            ns_is=EnvNotice.IS,
            ns=EnvNotice.IS,
            ns_env=EnvNotice.ENV_LENGTH_21_ENGLISH[:3],
            header=auth,
            response_code=404,
        ).json()
        Assertions.assert_checking_key_after_deletion_env(res=res)

        # Проверка, что контур после удаления отсутствует в  k8s/apis/paas.akbars.tech/v1/
        res_get_apis = app.env.check_env(
            ns_is=EnvNotice.IS,
            ns=EnvNotice.IS,
            ns_env=EnvNotice.ENV_LENGTH_21_ENGLISH[:3],
            header=auth,
            response_code=404
        ).json()
        assert res_get_apis['message'] == EnvNotice.NAMESPACE_IN_APIS_NOT_FOUND

        # Проверка, что контур после удаления отсутствует в k8s/api/v1/
        app.env.get(
            url_api=Env.URL_NAMESPACE.format(EnvNotice.IS, EnvNotice.ENV_LENGTH_21_ENGLISH[:3]),
            header=auth,
            response_code=404
        ).json()

    @pytestrail.case("C16450160")
    @pytest.mark.xfail(reason="GET запрос к /api/v1/ пока отдает 200 ответ, так как нет консестентного удаления Env")
    def test_delete_environment(self, app, auth, create_env):
        """
        Удаление существующего контура;
        Перед тестом выполняется фикстура создания контура "create_env".
        """
        res = app.env.delete(
            ns_is=EnvNotice.IS,
            ns=EnvNotice.IS,
            ns_env=EnvNotice.ENV_LENGTH_21_ENGLISH[:3],
            header=auth
        ).json()
        Assertions.assert_checking_key_after_deletion_env(res=res)

        # Проверка, что контур после удаления отсутствует в  k8s/apis/paas.akbars.tech/v1/
        res_get_apis = app.env.check_env(
            ns_is=EnvNotice.IS,
            ns=EnvNotice.IS,
            ns_env=EnvNotice.ENV_LENGTH_21_ENGLISH[:3],
            header=auth,
            response_code=404
        ).json()
        assert res_get_apis['message'] == EnvNotice.NAMESPACE_IN_APIS_NOT_FOUND

        # Проверка, что контур после удаления отсутствует в k8s/api/v1/
        app.env.get(
            url_api=Env.URL_NAMESPACE.format(EnvNotice.IS, EnvNotice.ENV_LENGTH_21_ENGLISH[:3]),
            header=auth,
            response_code=404
        )
