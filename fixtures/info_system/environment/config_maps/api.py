from requests import Response
from fixtures.base import BaseClass


class ConfigMaps(BaseClass):

    def get(self, url_api: str, header=None) -> Response:
        """Получение Config Maps."""
        res = self.app.base.request(
            method="GET",
            url=f"{self.app.url}{url_api}",
            headers=header,
            verify=False,
        )
        return res
