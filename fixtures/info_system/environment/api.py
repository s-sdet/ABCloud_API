import logging
from requests import Response
from fixtures.base import BaseClass

logger = logging.getLogger("ABCloud API")


class Env(BaseClass):
    NS_IS_CREATING = "bbivn"  # Название namespace-is для создания информационной системы

    NS_IS = "is4"  # Название namespace-is
    NS_ENV = "is4-autotest"  # Название namespace-env

    NS_IS_INVALID = "qa4"  # Невалидное значение namespace-is
    NS_ENV_INVALID = "qa4-autotest"  # Невалидное значение namespace-env

    URL_INFORMATION_SYSTEM = "apis/paas.akbars.tech/v1/informationsystems/{}"
    URL_NAMESPACE = "api/v1/namespaces/{}-{}"
    URL_LIST_ENVIRONMENTS = "apis/paas.akbars.tech/v1/environments"
    URL_ENVIRONMENTS_IN_NAMESPACE_IS = "apis/paas.akbars.tech/v1/namespaces/{}/environments"
    URL_ENVIRONMENT_IN_NAMESPACE_IS = "apis/paas.akbars.tech/v1/namespaces/{}/environments/{}"
    URL_ENVIRONMENTS_IN_INVALID_NAMESPACE_IS = "apis/paas.akbars.tech/v1/namespaces/{}/environments"
    URL_ENVIRONMENT_IN_NAMESPACE_IS_APIS = "apis/paas.akbars.tech/v1/namespaces/{}/environments/{}-{}"

    def get(self, url_api: str, header=None, response_code=200) -> Response:
        """Получение контура."""
        res = self.app.base.request(
            method="GET",
            url=f"{self.app.url}{url_api}",
            headers=header,
            verify=False,
        )
        logger.info(f"GET Environment Response: {res.status_code}")
        assert res.status_code == response_code
        return res

    def check_env(self, header=None, response_code=200, ns_is=None, ns=None, ns_env=None) -> Response:
        """Проверка контура."""
        res = self.app.base.request(
            method="GET",
            url=f"{self.app.url}{self.URL_ENVIRONMENT_IN_NAMESPACE_IS_APIS.format(ns_is, ns, ns_env)}",
            headers=header,
            verify=False,
        )
        logger.info(f"Name Environment: '{ns_is}-{ns_env}' - status code: {res.status_code}")
        assert res.status_code == response_code
        return res

    def create_env(self, data: dict = None, header=None, response_code=201, ns_is=None) -> Response:
        """Создание контура."""
        res = self.app.base.request(
            method="POST",
            url=f"{self.app.url}{self.URL_ENVIRONMENTS_IN_NAMESPACE_IS.format(ns_is)}",
            data=data,
            headers=header,
            verify=False,
        )
        logger.info(f"Environment created. Status code: {res.status_code}")
        assert res.status_code == response_code
        return res

    def delete(self, header=None, response_code=200, ns_is=None, ns=None, ns_env=None) -> Response:
        """Удаление контура."""
        res = self.app.base.request(
            method="DELETE",
            url=f"{self.app.url}{self.URL_ENVIRONMENT_IN_NAMESPACE_IS_APIS.format(ns_is, ns, ns_env)}",
            headers=header,
            verify=False,
        )
        logger.info(f"Environment removed. Status code: {res.status_code}")
        assert res.status_code == response_code
        return res
