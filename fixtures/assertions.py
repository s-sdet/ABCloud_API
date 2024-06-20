from data.constants import EnvNotice, ISNotice


class Assertions:
    """Проверки нужный полей после создания/удаления сущностей."""

    @staticmethod
    def assert_valid_checking_key_apiversion_kind(res=None, version=None, kind=None):
        assert res['apiVersion'] == version  # Проверка версии API
        assert res['kind'] == kind  # Проверка, что ['kind']="EnvironmentList"

    @staticmethod
    def assert_checking_key_after_creation_env(res=None, ns_is=None, ns_env=None):
        assert res['apiVersion'] == EnvNotice.API_VERSION  # Проверка версии API
        assert res['metadata']['labels']['env'] == ns_env  # Проверка, что "env"=имени контура
        assert res['metadata']['labels']['is'] == ns_is  # Проверка, что "env"=имени namespace
        assert res['metadata']['labels']['paas'] == "true"  # Проверка, что ""=true
        assert res['metadata']['name'] == f"{ns_is}-{ns_env}"  # Проверка, что "name"="namespace-env"
        assert res['metadata']['namespace'] == ns_is  # Проверка, что "namespace"="namespace-is"
        assert res['spec']['description'] == EnvNotice.DESCRIPTION  # Проверка, что описание контура корректно

    @staticmethod
    def assert_valid_checking_key_apiversion_code(res=None, version=None, code=None):
        assert res['apiVersion'] == version  # Проверка версии API
        assert res['code'] == code  # Проверка кода

    @staticmethod
    def assert_valid_checking_key_apiversion_code_message(res=None, version=None, code=None, message=None):
        assert res['apiVersion'] == version  # Проверка версии API
        assert res['code'] == code  # Проверка кода
        assert res['message'] == message  # Проверка ответа webhook сервера

    @staticmethod
    def assert_checking_key_after_deletion_env(res=None):
        assert res['apiVersion'] == EnvNotice.API_VERSION_V1
        assert res['kind'] == EnvNotice.KIND_INVALID
        assert res['metadata'] == EnvNotice.METADATA
        assert res['details']['name'] == EnvNotice.ENV_LENGTH_3_ENGLISH
        assert res['details']['group'] == EnvNotice.GROUP
        assert res['details']['kind'] == EnvNotice.ENVIRONMENTS

    @staticmethod
    def assert_checking_key_after_creation_info_system(res=None, version=ISNotice.API_VERSION, kind=ISNotice.KIND,
                                                       ns_is=ISNotice.NS_IS, businessname=ISNotice.BUSINESS_NAME[:12],
                                                       description=ISNotice.DESCRIPTION[:19], prefix=ISNotice.PREFIX,
                                                       state=ISNotice.STATE_PILOT):
        assert res['apiVersion'] == version
        assert res['kind'] == kind
        assert res['metadata']['labels']['is'] == ns_is
        assert res['metadata']['name'] == ns_is
        assert res['spec']['businessname'] == businessname
        assert res['spec']['description'] == description
        assert res['spec']['prefix'] == prefix
        assert res['spec']['state'] == state