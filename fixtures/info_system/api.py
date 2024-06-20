import logging
from requests import Response
from fixtures.base import BaseClass
from data.constants import ISNotice

logger = logging.getLogger("ABCloud API")


class InfoSystem(BaseClass):

    URL_INFO_SYSTEMS = "apis/paas.akbars.tech/v1/informationsystems"  # Для получения всех ИС
    URL_INFO_SYSTEM = "apis/paas.akbars.tech/v1/informationsystems/{}"  # Для получения конкретной ИС
    URL_INFO_SYSTEM_IN_NS = "api/v1/namespaces/{}"  # Для получения конкретной ИС в namespaces

    @staticmethod
    def create_data_is_body(ns_is: str, businessname: str, prefix: str, state: str, description: str):
        """Метод для передачи данных в тело запроса."""
        data = "apiVersion: paas.akbars.tech/v1\r\n" \
                "kind: InformationSystem\r\n" \
                "metadata:\r\n  " \
                    f"name: {ns_is}\r\n" \
                "spec:\r\n  " \
                    f"businessname: {businessname}\r\n  " \
                    f"prefix: \"{prefix}\"\r\n  " \
                    f"state: \"{state}\"\r\n  " \
                    f"description: \"{description}\""
        return data

    def get_list_is(self, header=None, response_code=200) -> Response:
        """Получение списка всех информационных систем."""
        res = self.app.base.request(
            method="GET",
            url=f"{self.app.url}{self.URL_INFO_SYSTEMS}",
            headers=header,
            verify=False,
        )
        logger.info(f"GET Info Systems. Status code: {res.status_code}")
        assert res.status_code == response_code
        return res

    def get_is(self, header=None, response_code=200, ns_is=None) -> Response:
        """Получение одной информационной системы."""
        res = self.app.base.request(
            method="GET",
            url=f"{self.app.url}{self.URL_INFO_SYSTEM.format(ns_is)}",
            headers=header,
            verify=False,
        )
        logger.info(f"Checking Info System: {ns_is} in apis. Status code: {res.status_code}")
        assert res.status_code == response_code
        return res

    def checking_is_in_ns(self, header=None, response_code=200, ns_is=None) -> Response:
        """Проверка информационной системы в namespaces api."""
        res = self.app.base.request(
            method="GET",
            url=f"{self.app.url}{self.URL_INFO_SYSTEM_IN_NS.format(ns_is)}",
            headers=header,
            verify=False,
        )
        logger.info(f"Checking Info System: {ns_is} in ns api. Status code: {res.status_code}")
        assert res.status_code == response_code
        return res

    def create_is(self, header=None, response_code=201, ns_is=ISNotice.NS_IS, businessname=ISNotice.BUSINESS_NAME,
                  prefix=ISNotice.PREFIX, state=ISNotice.STATE_PILOT, description=ISNotice.DESCRIPTION) -> Response:
        """Создание информационной системы."""
        res = self.app.base.request(
            method="POST",
            url=f"{self.app.url}{self.URL_INFO_SYSTEM.format(ns_is)}",
            data=self.create_data_is_body(ns_is=ns_is, businessname=businessname, prefix=prefix, state=state,
                                          description=description),
            headers=header,
            verify=False,
        )
        logger.info(f"Info System {ns_is} created. Status code: {res.status_code}")
        assert res.status_code == response_code
        return res

    def delete(self, header=None, response_code=200, ns_is=None) -> Response:
        """Удаление информационной системы."""
        res = self.app.base.request(
            method="DELETE",
            url=f"{self.app.url}{self.URL_INFO_SYSTEM.format(ns_is)}",
            headers=header,
            verify=False,
        )
        logger.info(f"Info System {ns_is} removed. Status code: {res.status_code}")
        assert res.status_code == response_code
        return res