import logging
from requests import Response
from fixtures.base import BaseClass
from common.deco import log
logger = logging.getLogger("ABCloud API")


class Pods(BaseClass):

    URL_PODS = "api/v1/namespaces/is4-autotest/pods"  # Для получения всех Pods
    NS_IS = "is4"
    NS_ENV = "autotest"
    POD = "busybox"
    CONTAINER = "busybox"
    URL_UI = "https://paas-dev.dev-int.akbars.ru"
    URL_INIT = f"/terminal-api/api/v1/pod/{NS_IS}-{NS_ENV}/{POD}/shell/{CONTAINER}?shell=sh"

    @log('')
    def get(self, header=None, response_code=200) -> Response:
        """Получение всех Pods."""
        res = self.app.base.request(
            method="GET",
            url=f"{self.app.url}{self.URL_PODS}",
            headers=header,
            verify=False,
        )
        logger.info(f"GET list Pods. Status code: {res.status_code}")
        assert res.status_code == response_code
        return res

    @log('')
    def create_session(self, header=None, response_code=200) -> Response:
        """"""
        res = self.app.base.request(
            method="GET",
            url=f"{self.URL_UI}{self.URL_INIT}",
            headers=header,
            verify=False,
        )
        logger.info(f"Create Session. Status code: {res.status_code}")
        assert res.status_code == response_code
        return res