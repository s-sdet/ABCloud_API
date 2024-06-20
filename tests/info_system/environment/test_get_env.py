import pytest
import logging
from pytest_testrail.plugin import pytestrail
from data.constants import EnvNotice, ISNotice
from fixtures.info_system.environment.api import Env
from fixtures.assertions import Assertions

logger = logging.getLogger("ABCloud API")


class TestsGetEnv:
    """Тесты для проверки контуров."""

    @pytestrail.case("C16448033", "C16448118")
    @pytest.mark.parametrize("url", [Env.URL_LIST_ENVIRONMENTS,
                                     Env.URL_ENVIRONMENTS_IN_NAMESPACE_IS.format(Env.NS_IS)])
    def test_checking_environments(self, app, auth, url):
        """
        Получение и проверка контуров из всех namespaces и из одного namespace.
        Параметризацией проверяем два урла:
           1. Для получения контуров всех namespaces;
           2. Для получения контуров конкретного namespace;
        После получения списка контуров - циклом проходим по json и проверяем каждый контур на ответ 200, с проверкой
        нужный полей.
        """
        res = app.env.get(
            url_api=url,
            header=auth
        ).json()
        Assertions.assert_valid_checking_key_apiversion_kind(res=res, version=EnvNotice.API_VERSION,kind=EnvNotice.KIND)
        for item in res['items']:
            name = item['metadata']['name']  # Значения ключа "name"
            namespace = item['metadata']['namespace']  # Значения ключа "namespace"
            information_system = item['metadata']['labels']['is']  # Значения ключа "is"
            env = item['metadata']['labels']['env']  # Значения ключа "env"
            app.env.check_env(
                ns_is=namespace,
                ns=namespace,
                ns_env=env,
                header=auth
            )
            assert res['kind'] == EnvNotice.KIND  # Проверка, что ['items']['kind']="Environment"
            assert namespace == information_system  # Проверка, что значение "namespace" соот-т значению "is"
            assert name == f"{information_system}-{env}"  # Проверка, что значение "name" соот-т значениям "is"-"env"


    @pytestrail.case("C16448124")
    def test_checking_environment(self, app, auth):
        """Получение и проверка одного контура из одного namespace."""
        res = app.env.check_env(
            ns_is=EnvNotice.IS,
            ns=EnvNotice.IS,
            ns_env=EnvNotice.NAMESPACE.split('-')[1],
            header=auth
        ).json()
        name = res['metadata']['name']  # Значения ключа "name"
        namespace = res['metadata']['namespace']  # Значения ключа "namespace"
        information_system = res['metadata']['labels']['is']  # Значения ключа "is"
        env = res['metadata']['labels']['env']  # Значения ключа "env"
        Assertions.assert_valid_checking_key_apiversion_kind(res=res, version=EnvNotice.API_VERSION,
                                                             kind=EnvNotice.KIND_ITEMS)
        assert namespace == information_system  # Проверка, что значение "namespace" соот-т значению "is"
        assert name == f"{information_system}-{env}"  # Проверка, что значение "name" соот-т значениям "is"-"env"


    @pytestrail.case("C16448369")
    def test_checking_environments_invalid_namespace(self, app, auth):
        """Получение конутров несуществующего namespace."""
        res = app.env.get(
            url_api=Env.URL_ENVIRONMENTS_IN_NAMESPACE_IS.format(Env.NS_IS_INVALID),
            header=auth
        ).json()
        Assertions.assert_valid_checking_key_apiversion_kind(res=res, version=EnvNotice.API_VERSION,
                                                             kind=EnvNotice.KIND)
        assert res['items'] == EnvNotice.ITEMS  # Проверка, что ['items']=[]
        assert 'resourceVersion' in res['metadata']  # Проверка, что "metadata" содержит ключ "resourceVersion"

    @pytestrail.case("C16448461")
    def test_checking_environment_invalid_namespace(self, app, auth):
        """Получение конутра несуществующего namespace."""
        res = app.env.check_env(
            ns_is=EnvNotice.NAMESPACE_INVALID,
            ns=EnvNotice.NAMESPACE_INVALID,
            ns_env=EnvNotice.NAME_INVALID.split('-')[1],
            header=auth,
            response_code=404
        ).json()
        Assertions.assert_valid_checking_key_apiversion_code(res=res, version=EnvNotice.API_VERSION_V1,
                                                             code=EnvNotice.CODE_404)
        assert res['details']['name'] == EnvNotice.NAME_INVALID  # Проверка, что "name" соот-т названию контура
        assert res['message'] == EnvNotice.MESSAGE_NOT_FOUND  # Проверка, что ['message']=
        assert res['metadata'] == EnvNotice.METADATA  # Проверка, что ['metadata']="{}"
        assert res['reason'] == EnvNotice.REASON  # Проверка, что ['reason']="NotFound"
        assert res['status'] == EnvNotice.STATUS  # Проверка, что ['status']="Failure"

    @pytestrail.case("C16676968")
    def test_checking_empty_list_environment(self, app, auth, create_is):
        """
        Получение пустого списка контуров конкретного ns.
            1. Фикстурой "create_is" создаем пустую информационную систему без контуров;
            2. GET-запросом проверяем, что информационная система не содержит контуров;
            3. Удаляем информационную систему.
        """
        res = app.env.get(
            url_api=Env.URL_ENVIRONMENTS_IN_NAMESPACE_IS.format(ISNotice.NS_IS),
            header=auth).json()
        Assertions.assert_valid_checking_key_apiversion_kind(res=res, version=EnvNotice.API_VERSION,
                                                             kind=EnvNotice.KIND)
        assert res['items'] == EnvNotice.ITEMS  # Проверка, что ['items']=[]
        assert res['metadata']['continue'] == EnvNotice.CONTINUE  # Проверка, что ['continue']=""

        # Удаление Environment
        app.info_system.delete(
            ns_is=ISNotice.NS_IS,
            header=auth
        )
