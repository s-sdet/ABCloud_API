import logging
import pytest
from pytest_testrail.plugin import pytestrail
from fixtures.assertions import Assertions
from data.constants import ISNotice

logger = logging.getLogger("ABCloud API")


class TestsCreateIS:
    """Тесты для создания информационных систем."""

    @pytestrail.case("C16677268", "C16677269", "C16692168", "C16692123", "C16692126", "C16692185", "C16692134",
                     "C16692135")
    @pytest.mark.parametrize("businessname, ns_is, prefix, description, state", ISNotice.VALIDATION_CREATE_INFO_SYSTEM)
    def test_creating_is(self, app, auth, businessname, ns_is, prefix, description, state):
        """Тест для проверки создания информационной системы с валидными данными."""
        res = app.info_system.create_is(
            ns_is=ns_is,
            businessname=businessname,
            state=state,
            description=description,
            header=auth,
        ).json()
        Assertions.assert_checking_key_after_creation_info_system(res=res, ns_is=ns_is, businessname=businessname,
                                                                  description=description, state=state)

        # Проверка информационной системы в apis
        app.info_system.get_is(ns_is=ns_is, header=auth)

        # Проверка информационной системы ИС в api namespaces
        app.info_system.checking_is_in_ns(ns_is=ns_is, header=auth)

        # Удаление информационной системы
        app.info_system.delete(ns_is=ns_is, header=auth)
