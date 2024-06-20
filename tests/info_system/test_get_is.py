import logging
from data.constants import ISNotice
from pytest_testrail.plugin import pytestrail
from fixtures.assertions import Assertions

logger = logging.getLogger("ABCloud API")


class TestsIS:
    """Тесты для проверки информационных систем."""

    @pytestrail.case("C16667407", "C16676963")
    def test_checking_information_systems(self, app, auth):
        """
        1. Получаем список всех информационных систем;
        2. Проверяем каждую ИС из списка на ответ 200.
        """
        res = app.info_system.get_list_is(
            header=auth
        ).json()
        Assertions.assert_valid_checking_key_apiversion_kind(res=res, version=ISNotice.API_VERSION,
                                                             kind=ISNotice.KIND_LIST)
        for item in res['items']:
            assert item['apiVersion'] == ISNotice.API_VERSION
            assert item['kind'] == ISNotice.KIND
            ns_is = item['metadata']['labels']['is']
            # Проверка каждой ИС на ответ 200
            app.info_system.get_is(
                ns_is=ns_is,
                header=auth,
            )
            assert item['metadata']['name'] == ns_is  # Проверка, что названия ИС совпадают
            assert item['spec']['state'] in ISNotice.STATE

    @pytestrail.case("C16676971")
    def test_checking_invalid_information_systems(self, app, auth):
        """Получение несуществующей информационной системы."""
        res = app.info_system.get_is(
            ns_is=ISNotice.NS_IS,
            header=auth,
            response_code=404
        ).json()
        Assertions.assert_valid_checking_key_apiversion_code_message(res=res, version=ISNotice.API_VERSION_V1,
                                                                     message=ISNotice.MESSAGE, code=ISNotice.CODE_404)
        assert res['metadata'] == ISNotice.METADATA
        assert res['details']['name'] == ISNotice.NS_IS
        assert res['details']['group'] == ISNotice.GROUP
        assert res['details']['kind'] == ISNotice.KIND_INVALID