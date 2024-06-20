import pytest
import logging
from data.constants import EnvNotice
from pytest_testrail.plugin import pytestrail
from fixtures.info_system.environment.api import Env
from fixtures.assertions import Assertions

logger = logging.getLogger("ABCloud API")


class TestsCreateEnv:
    """Тесты для проверок создания контура."""

    @pytestrail.case("C16448475", "C16507645")
    @pytest.mark.parametrize("data_environment, ns_env, ns_is", EnvNotice.VALIDATION_CREATE_ENV_WITHOUT_CHAT_ID)
    def test_creating_env_without_chat_id(self, app, auth, data_environment, ns_env, ns_is):
        """Создание контура в существующем namespace без chat_id."""
        res = app.env.create_env(
            ns_is=ns_is,
            header=auth,
            data=data_environment,
        ).json()
        Assertions.assert_checking_key_after_creation_env(res=res, ns_env=ns_env, ns_is=ns_is)

        # Проверка namespace-env в /apis/paas.akbars.tech/v1/
        app.env.get(url_api=Env.URL_ENVIRONMENT_IN_NAMESPACE_IS_APIS.format(ns_is, ns_is, ns_env), header=auth)

        # Проверка namespace-env в /api/v1/
        res_get_api = app.env.get(url_api=Env.URL_NAMESPACE.format(ns_is, ns_env), header=auth).json()
        assert res_get_api['metadata']['name'] == f"{ns_is}-{ns_env}"  # Проверка имени созданного контура

        # Удаление Environment
        app.env.delete(ns_is=ns_is, ns=ns_is, ns_env=ns_env, header=auth)

    @pytestrail.case("C16448877", "C16508205", "C16508207", "C16508247", "C16508243")
    @pytest.mark.parametrize("data_environment, ns_env, ns_is, chat_id", EnvNotice.VALIDATION_CREATE_ENV_WITH_CHAT_ID)
    @pytest.mark.xfail(reason="Возможна ошибка 404, т.к. на тестовом стенде environment создается с задержкой")
    def test_creating_env_with_chat_id(self, app, auth, data_environment, ns_env, ns_is, chat_id):
        """
        Создание контура в существующем namespace c chatid;
        Переиспользуется тест "test_create_env_without_chat_id", добавляется проверка ключа ['chatid']
        """
        res = app.env.create_env(
            ns_is=ns_is,
            header=auth,
            data=data_environment,
        ).json()
        Assertions.assert_checking_key_after_creation_env(res=res, ns_env=ns_env, ns_is=ns_is)
        assert res['spec']['chatid'] == chat_id  # Проверка, что chat_id корректный

        # Проверка namespace-env в /apis/paas.akbars.tech/v1/
        app.env.get(url_api=Env.URL_ENVIRONMENT_IN_NAMESPACE_IS_APIS.format(ns_is, ns_is, ns_env), header=auth)

        # Проверка namespace-env в /api/v1/
        res_get_api = app.env.get(url_api=Env.URL_NAMESPACE.format(ns_is, ns_env), header=auth).json()
        assert res_get_api['metadata']['name'] == f"{ns_is}-{ns_env}"  # Проверка имени созданного контура

        # Удаление Environment
        app.env.delete(ns_is=ns_is, ns=ns_is, ns_env=ns_env, header=auth)

    @pytestrail.case("C16450375")
    def test_creating_env_with_chat_id_and_labels(self, app, auth):
        """Создание контура в существующем namespace c chatid и с labels."""
        res = app.env.create_env(
            ns_is=EnvNotice.IS,
            header=auth,
            data=EnvNotice.INVALID_DATA_ENV,
        ).json()
        assert res['apiVersion'] == EnvNotice.API_VERSION  # Проверка версии API
        assert res['metadata']['labels']['env'] == EnvNotice.ENV  # Проверка, что "env"=имени контура
        assert res['metadata']['labels']['is'] == EnvNotice.IS  # Проверка, что "env"=имени namespace
        assert res['metadata']['name'] == EnvNotice.ENV_LENGTH_3_ENGLISH  # Проверка, что "name"="namespace-env"

        # Удаление Environment
        app.env.delete(ns_is=EnvNotice.IS, ns=EnvNotice.IS, ns_env=EnvNotice.ENV_LENGTH_21_ENGLISH[:3], header=auth)

    @pytestrail.case("C16458415", "C16458748", "C16508206", "C16508208", "C16508424", "C16664781", "C16664783",
                     "C16664782", "C16664784", "C16508445", "C16508496", "C16458783")
    @pytest.mark.parametrize("data_environment, webhook_message", EnvNotice.VALIDATION_WEBHOOK_LENGTH)
    def test_check_creation_env_with_invalid_name(self, app, auth, data_environment, webhook_message):
        """Негативные тесты на создание контура с невалидным названием."""
        res = app.env.create_env(
            ns_is=EnvNotice.IS,
            header=auth,
            data=data_environment,
            response_code=400,
        ).json()
        Assertions.assert_valid_checking_key_apiversion_code_message(res=res, version=EnvNotice.API_VERSION_V1,
                                                                     code=EnvNotice.CODE_400, message=webhook_message)

    @pytestrail.case("C16460369")
    def test_check_creation_env_without_name_and_invalid_namespace(self, app, auth):
        """Негативный тест на создание контура без названия и невалидным namespace."""
        res = app.env.create_env(
            ns_is=EnvNotice.IS,
            header=auth,
            data=EnvNotice.DATA_ENV_WITHOUT_NAME,
            response_code=422,
        ).json()
        assert res['apiVersion'] == EnvNotice.API_VERSION_V1
        assert res['message'] == EnvNotice.MESSAGE_NAME_INVALID_VALUE_PAAS
        assert res['details']['name'] == EnvNotice.NAME_WITHOUT_ENV
        assert res['details']['group'] == EnvNotice.GROUP
        assert res['details']['kind'] == EnvNotice.KIND_ITEMS
        for item in res['details']['causes']:
            assert item['reason'] == EnvNotice.REASON_CAUSES
            assert item['message'] == EnvNotice.MESSAGE_NAME_INVALID_VALUE
            assert item['field'] == EnvNotice.METADATA_NAME

    @pytestrail.case("C16507648", "C16508203", "C16508202", "C16508201")
    @pytest.mark.parametrize("data", EnvNotice.VALIDATION_CREATE_ENV_WITH_INVALID_NAME_RUS)
    def test_creating_env_with_invalid_name_rus(self, app, auth, data):
        """Негативные тесты на создание контура с именем на кириллице в существующем namespace."""
        res = app.env.create_env(
            ns_is=EnvNotice.IS,
            header=auth,
            data=data,
            response_code=422,
        ).json()
        Assertions.assert_valid_checking_key_apiversion_code(res=res, version=EnvNotice.API_VERSION_V1,
                                                             code=EnvNotice.CODE_422)

    @pytestrail.case("C16507646", "C16507647")
    @pytest.mark.parametrize("data, message, causes_message", EnvNotice.VALIDATION_CREATE_ENV_WITH_INVALID_NAME_ENG)
    def test_creating_env_with_invalid_name_eng(self, app, auth, data, message, causes_message):
        """
        Негативные тесты на создание контура с именем на латинице в существующем namespace.
        """
        res = app.env.create_env(
            ns_is=EnvNotice.IS,
            header=auth,
            data=data,
            response_code=422,
        ).json()
        Assertions.assert_valid_checking_key_apiversion_code(res=res, version=EnvNotice.API_VERSION_V1,
                                                             code=EnvNotice.CODE_422)
        assert res['message'] == message
        for item in res['details']['causes']:
            assert item['message'] == causes_message

    @pytestrail.case("C16508495")
    def test_creating_env_numbers_and_description_length_256(self, app, auth):
        """Тест на создание контура с именем из цифр в существующем namespace с description=256 символов."""
        res = app.env.create_env(
            ns_is=EnvNotice.IS,
            header=auth,
            data=EnvNotice.DATA_NAME_NUMBERS_LENGTH_3_WITH_DESCRIPTION_256
        ).json()
        Assertions.assert_valid_checking_key_apiversion_kind(res=res, version=EnvNotice.API_VERSION,
                                                             kind=EnvNotice.KIND_ITEMS)
        assert res['spec']['description'] == EnvNotice.DESCRIPTION_MAXIMUM_LENGTH[:256]

        # Удаление Environment
        app.env.delete(ns_is=EnvNotice.IS, ns=EnvNotice.IS, ns_env=EnvNotice.ENV_LENGTH_21_NUMBERS[:3], header=auth)

    @pytestrail.case("C16664775")
    def test_creating_env_with_duplicate_name(self, app, auth):
        """Тест на создание контура с именем которое уже есть в информационной системе."""
        res = app.env.create_env(
            ns_is=EnvNotice.IS,
            header=auth,
            data=EnvNotice.DATA_DUPLICATE_NAME,
            response_code=409,
        ).json()
        Assertions.assert_valid_checking_key_apiversion_code_message(res=res, version=EnvNotice.API_VERSION_V1,
                                                                     code=EnvNotice.CODE_409,
                                                                     message=EnvNotice.MESSAGE_ALREADY_EXISTS)
        assert res['details']['group'] == EnvNotice.GROUP
        assert res['details']['kind'] == EnvNotice.ENVIRONMENTS
        assert res['details']['name'] == EnvNotice.NAMESPACE

    @pytestrail.case("C16664785")
    def test_creating_env_with_invalid_api_version(self, app, auth):
        """Тест на создание контура с невалидной apiVersion."""
        res = app.env.create_env(
            ns_is=EnvNotice.IS,
            header=auth,
            data=EnvNotice.DATA_INVALID_API_VERSION,
            response_code=400,
        ).json()
        Assertions.assert_valid_checking_key_apiversion_code_message(res=res, version=EnvNotice.API_VERSION_V1,
                                                                     code=EnvNotice.CODE_400,
                                                                     message=EnvNotice.MESSAGE_INVALID_API_VERSION)
