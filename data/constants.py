"""Константы, в т.ч. тексты ошибок и уведомлений."""


class ISNotice:
    """Константы для информационные системы."""

    """Константы для валидных тестов."""
    NS_IS = "bbivn"  # Название информационной системы
    PREFIX = "bbivn"  # Префикс
    BUSINESS_NAME = "Autotest API Autotest API Autotest API Autotest API Autotest API Autotest API Autotest API " \
                    "Autotest API Autotest API Autotest API Autotest API Autotest API Autotest API Autotest API " \
                    "Autotest API Autotest API Autotest API Autotest API Autotest API AutotesttA"  # Бизнес наименование
    DESCRIPTION = "Created by autotest Created by autotest Created by autotest Created by autotest Created by autotest " \
                  "Created by autotest Created by autotest Created by autotest Created by autotest Created by autotest " \
                  "Created by autotest Created by autotest Created by autote"  # Описание (257 символов)

    # Варианты статуса информационной системы
    STATE_PILOT = "pilot"
    STATE_COMMERCIAL = "commercial"
    STATE_ARCHIVE = "archive"

    URL_INFORMATION_SYSTEM_BBIVN = f"apis/paas.akbars.tech/v1/informationsystems/{NS_IS}"
    URL_ENVIRONMENTS_ONE_NAMESPACE = f"apis/paas.akbars.tech/v1/namespaces/{NS_IS}/environments"

    API_VERSION = "paas.akbars.tech/v1"  # Значение поля apiVersion
    KIND = "InformationSystem"  # Значение поля kind
    KIND_LIST = "InformationSystemList"  # Значение поля kind внутри ["items"]
    STATE = "pilot, commercial, archive"  # Варианты статуса ИС

    """Константы для не валидных тестов."""
    NS_IS_INVALID = "sdfsdfsd"  # Название информационной системы
    API_VERSION_V1 = "v1"  # Значение поля apiVersion
    GROUP = "paas.akbars.tech"  # Значение поля group
    CODE_404 = 404  # Значение поля code
    MESSAGE = f"informationsystems.paas.akbars.tech \"{NS_IS}\" not found"  # Значение поля message
    METADATA = {}  # Значение поля metadata
    KIND_INVALID = "informationsystems"  # Значение поля kind при невалидном кейсе

    DATA_IS: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                    "kind: InformationSystem\r\n" \
                    "metadata:\r\n  " \
                        f"name: {NS_IS}\r\n" \
                    "spec:\r\n  " \
                        "businessname: Autotest API\r\n  " \
                        f"prefix: \"{PREFIX}\"\r\n  " \
                        "state: \"pilot\"\r\n  " \
                        "description: \"Created by autotest\""

    VALIDATION_CREATE_INFO_SYSTEM = [
        #  Создание ИС со статусом Pilot
        [BUSINESS_NAME[:12].replace(" ", ""), NS_IS, PREFIX, DESCRIPTION[:19], STATE_PILOT],
        #  Создание ИС со статусом Commercial
        [BUSINESS_NAME[:12].replace(" ", ""), NS_IS, PREFIX, DESCRIPTION[:19], STATE_COMMERCIAL],
        #  Создание ИС с пробелом между текстом в поле businessname
        [BUSINESS_NAME[:12], NS_IS, PREFIX, DESCRIPTION[:19], STATE_PILOT],
        #  Создание ИС с 2 символами в поле businessname
        [BUSINESS_NAME[:2], NS_IS, PREFIX, DESCRIPTION[:19], STATE_PILOT],
        #  Создание ИС с 256 символами в поле businessname
        [BUSINESS_NAME[:256], NS_IS, PREFIX, DESCRIPTION[:19], STATE_PILOT],
        #  Создание ИС с пробелом между текстом в поле description
        [BUSINESS_NAME[:12], NS_IS, PREFIX, DESCRIPTION[:19], STATE_PILOT],
        #  Создание ИС с 2 символами в поле description
        [BUSINESS_NAME[:12], NS_IS, PREFIX, DESCRIPTION[:2], STATE_PILOT],
        #  Создание ИС с 256 символами в поле description
        [BUSINESS_NAME[:12], NS_IS, PREFIX, DESCRIPTION[:256], STATE_PILOT],
    ]


class EnvNotice:
    """Константы для контура."""

    """Константы для проверки значений в json response Environment."""
    KIND = "EnvironmentList"  # Значение поля kind
    KIND_ITEMS = "Environment"  # Значение поля kind внутри items
    API_VERSION = "paas.akbars.tech/v1"  # Значение поля apiVersion
    API_VERSION_V1 = "v1"  # Значение поля apiVersion v1
    IS = "is4"  # Значение поля namespace
    NAMESPACE = "is4-autotest"  # Значение поля name для GET запросов
    ENV_LENGTH_3_ENGLISH = "is4-api"  # Значение поля name для POST запросов
    DESCRIPTION = "Created by autotest"
    CHAT_ID = "132036546532"
    CHAT_ID_MAXIMUM_LENGTH = "56546546546546546546546545686768667867867867867867867867678678678"  # Chat ID 65 символов
    ENV = "api"  # Название контура
    ENV_LENGTH_20_ENGLISH = "is4-qaaaaaaaaaaaaaaaaaaa"
    GROUP = "paas.akbars.tech"
    METADATA_NAME = "metadata.name"
    ENVIRONMENTS = "environments"
    STATUS_DELETE = "Success"
    CONTINUE = ""
    MESSAGE_INVALID_API_VERSION = "the API version in the data (v1) does not match the expected API version " \
                                  "(paas.akbars.tech/v1)"

    """Константы для невалидных запросов и проверки значений в json response."""
    NAMESPACE_INVALID = "qa4"  # Невалидное значение поля namespace
    NAME_INVALID = "qa4-autotest"  # Невалидное значение поля name
    NAME_WITHOUT_ENV = "is4-"  # name без environment
    ENV_LENGTH_21_ENGLISH = "apiiiiiiiiiiiiiiiiiii"  # Название контура 21 символ
    ENV_LENGTH_21_NUMBERS = "123456789123456789123"  # Название контура 21 цифра
    ENV_LENGTH_3_RUSSIAN = "is4-апи".encode('utf-8')  # Значение поля name для POST запросов
    ENV_MAXIMUM_LENGTH_RUSSIAN = "апиииииииииииииииииии".encode('utf-8')  # Название Env на кириллице 21 символ
    CHAT_ID_LENGTH_1_ENGLISH = "q"
    CHAT_ID_LENGTH_1_RUSSIAN = "й".encode('utf-8')
    CHAT_ID_LENGTH_1_SPECIAL = "%"
    CHAT_ID_LENGTH_1_SPACE = " "
    DESCRIPTION_MAXIMUM_LENGTH = "Created by autotest Created by autotest Created by autotest Created by autotest " \
                                 "Created by autotest Created by autotest Created by autotest Created by autotest " \
                                 "Created by autotest Created by autotest Created by autotest Created by autotest " \
                                 "Created by autote"
    NAMESPACE_IN_APIS_NOT_FOUND = f"environments.paas.akbars.tech \"{IS}-{ENV_LENGTH_21_ENGLISH[:3]}\" not found"
    NAMESPACE_IN_API_NOT_FOUND = f"namespaces \"{IS}-{ENV_LENGTH_21_ENGLISH[:3]}\" not found"
    ITEMS = []  # Значение items при невалидном namespaces
    METADATA = {}  # Значение metadata при невалидном namespaces
    CODE_404 = 404
    CODE_400 = 400
    CODE_422 = 422
    CODE_409 = 409
    KIND_INVALID = "Status"
    MESSAGE_NOT_FOUND = f'environments.paas.akbars.tech "{NAME_INVALID}" not found'
    MESSAGE_ALREADY_EXISTS = f'environments.paas.akbars.tech "{NAMESPACE}" already exists'
    REASON = "NotFound"
    REASON_CAUSES = "FieldValueInvalid"
    STATUS = "Failure"
    ADMISSION_WEBHOOK_MESSAGE_NAME_LENGTH = "admission webhook \"env-validation.webhook-server.svc\" denied the " \
                                            "request: environment name length is more than 20"
    ADMISSION_WEBHOOK_MESSAGE_CHAT_ID_LENGTH = "admission webhook \"env-validation.webhook-server.svc\" denied the " \
                                               "request: chat ID cannot be more than 64 characters"
    ADMISSION_WEBHOOK_MESSAGE_CHAT_ID_FORMAT = "admission webhook \"env-validation.webhook-server.svc\" denied the " \
                                               "request: chat ID format is not a valid"
    ADMISSION_WEBHOOK_MESSAGE_DESCRIPTION_LENGTH = "admission webhook \"env-validation.webhook-server.svc\" denied " \
                                                   "the request: description length is not a valid"
    ADMISSION_WEBHOOK_MESSAGE_DESCRIPTION_FORMAT = "admission webhook \"env-validation.webhook-server.svc\" denied " \
                                                   "the request: description format is not a valid"
    ADMISSION_WEBHOOK_MESSAGE_DELIMITER = "admission webhook \"env-mutation.webhook-server.svc\" denied the " \
                                          "request: delimiter \"-\" is missing"
    MESSAGE_NAME_INVALID_VALUE_PAAS = "Environment.paas.akbars.tech \"is4-\" is invalid: metadata.name: Invalid " \
                                      "value: \"is4-\": a lowercase RFC 1123 subdomain must consist of lower case " \
                                      "alphanumeric characters, '-' or '.', and must start and end with an " \
                                      "alphanumeric character (e.g. 'example.com', regex used for validation is " \
                                      "'[a-z0-9]([-a-z0-9]*[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*')"
    MESSAGE_NAME_INVALID_VALUE = "Invalid value: \"is4-\": a lowercase RFC 1123 subdomain must consist of lower case " \
                                 "alphanumeric characters, '-' or '.', and must start and end with an alphanumeric " \
                                 "character (e.g. 'example.com', regex used for validation is '[a-z0-9]([-a-z0-9]*" \
                                 "[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*')"

    MESSAGE_NAME_LENGTH_3_ENG_UPPER_PAAS = f"Environment.paas.akbars.tech \"{IS}-{ENV.upper()}\" is invalid: " \
                                           f"metadata.name: Invalid value: \"{IS}-{ENV.upper()}\": a lowercase " \
                                           f"RFC 1123 subdomain must consist of lower case alphanumeric characters," \
                                           f" '-' or '.', and must start and end with an alphanumeric character " \
                                           f"(e.g. 'example.com', regex used for validation is '[a-z0-9]([-a-z0-9]" \
                                           f"*[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*')"
    MESSAGE_NAME_LENGTH_3_ENG_UPPER = f"Invalid value: \"{IS}-{ENV.upper()}\": a lowercase RFC 1123 subdomain must " \
                                      f"consist of lower case alphanumeric characters, '-' or '.', and must start " \
                                      f"and end with an alphanumeric character (e.g. 'example.com', regex used for " \
                                      f"validation is '[a-z0-9]([-a-z0-9]*[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9]" \
                                      f")?)*')"

    MESSAGE_NAME_LENGTH_20_ENG_UPPER_PAAS = f"Environment.paas.akbars.tech" \
                                            f" \"{IS}-{ENV_LENGTH_21_ENGLISH.upper()[:20]}\" is invalid: metadata." \
                                            f"name: Invalid value: \"{IS}-{ENV_LENGTH_21_ENGLISH.upper()[:20]}\": a " \
                                            f"lowercase RFC 1123 subdomain must consist of lower case alphanumeric " \
                                            f"characters, '-' or '.', and must start and end with an alphanumeric " \
                                            f"character (e.g. 'example.com', regex used for validation is '[a-z0-9]" \
                                            f"([-a-z0-9]*[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*')"
    MESSAGE_NAME_LENGTH_20_ENG_UPPER = f"Invalid value: \"{IS}-{ENV_LENGTH_21_ENGLISH.upper()[:20]}\": a lowercase " \
                                       f"RFC 1123 subdomain must consist of lower case alphanumeric characters, '-' " \
                                       f"or '.', and must start and end with an alphanumeric character (e.g. " \
                                       f"'example.com', regex used for validation is '[a-z0-9]([-a-z0-9]*[a-z0-9])?" \
                                       f"(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*')"

    """Ручки для запросов."""
    URL_ENVIRONMENTS_ALL_NAMESPACES = "apis/paas.akbars.tech/v1/environments"
    URL_ENVIRONMENTS_ONE_NAMESPACE = f"apis/paas.akbars.tech/v1/namespaces/{IS}/environments"


    URL_ENVIRONMENTS_WITH_NAMESPACE = f"apis/paas.akbars.tech/v1/namespaces/{IS}/environments/" \
                                      f"{IS}-{ENV_LENGTH_21_ENGLISH[:3]}"
    URL_INVALID_ENVIRONMENT = f"apis/paas.akbars.tech/v1/namespaces/{IS}/environments/{IS}-{ENV_LENGTH_21_ENGLISH[:3]}"
    URL_ENVIRONMENTS_WITH_NAMESPACE_NUMBERS = f"apis/paas.akbars.tech/v1/namespaces/{IS}/environments/" \
                                              f"{IS}-{ENV_LENGTH_21_NUMBERS[:3]}"
    URL_NAMESPACE = f"api/v1/namespaces/{IS}-{ENV_LENGTH_21_ENGLISH[:3]}"
    URL_ENVIRONMENTS_INVALID_NAMESPACE = f"apis/paas.akbars.tech/v1/namespaces/{NAMESPACE_INVALID}/environments"
    URL_ENVIRONMENT_ONE_NAMESPACE = f"apis/paas.akbars.tech/v1/namespaces/{IS}/environments/{NAMESPACE}"
    URL_ENVIRONMENT_INVALID_NAMESPACE = f"apis/paas.akbars.tech/v1/namespaces/{NAMESPACE_INVALID}/environments/" \
                                        f"{NAME_INVALID}"

    # Для проверки создания контура (name-env - 3 латинских символа) без chatid
    DATA_ENV_WITHOUT_CHAT_ID: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                     "kind: Environment\r\n" \
                                     "metadata:\r\n  " \
                                         f"name: {IS}-{ENV_LENGTH_21_ENGLISH[:3]}\r\n" \
                                     "spec:\r\n  " \
                                         f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 3 латинских символа) c chatid
    ENV_NAME_LENGTH_3_ENGLISH: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                      "kind: Environment\r\n" \
                                      "metadata:\r\n  " \
                                          f"name: {IS}-{ENV_LENGTH_21_ENGLISH[:3]}\r\n" \
                                      "spec:\r\n  " \
                                          f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                          f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 3 латинских символа).В labels в поле env подается значение is и наоборот
    INVALID_DATA_ENV: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                             "kind: Environment\r\n" \
                             "metadata:\r\n  " \
                                 "labels:\r\n    " \
                                     f"env: {IS}\r\n    " \
                                     f"is: {ENV}\r\n  " \
                                 f"name: {IS}-{ENV}\r\n" \
                             "spec:\r\n  " \
                                f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 20 латинских символов)
    ENV_NAME_LENGTH_20_ENGLISH: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                            "kind: Environment\r\n" \
                                            "metadata:\r\n  " \
                                                f"name: {IS}-{ENV_LENGTH_21_ENGLISH[:20]}\r\n" \
                                            "spec:\r\n  " \
                                                f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                                f"description: {DESCRIPTION}"

    # Для проверки невалидного создания контура (name-env - 2 латинских символа)
    DATA_ENV_NAME_LENGTH_2: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                   "kind: Environment\r\n" \
                                   "metadata:\r\n  " \
                                       f"name: {IS}-{ENV_LENGTH_21_ENGLISH[:2]}\r\n" \
                                   "spec:\r\n  " \
                                       f"description: {DESCRIPTION}"

    # Для проверки невалидного создания контура (name-env - 21 латинских символа)
    DATA_ENV_NAME_LENGTH_21: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                   "kind: Environment\r\n" \
                                   "metadata:\r\n  " \
                                       f"name: {IS}-{ENV_LENGTH_21_ENGLISH}\r\n" \
                                   "spec:\r\n  " \
                                       f"description: {DESCRIPTION}"

    # Для проверки невалидного создания контура без указания namespace
    DATA_ENV_NAME_LENGTH_3_WITHOUT_NAMESPACE: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                     "kind: Environment\r\n" \
                                                     "metadata:\r\n  " \
                                                         f"name: {ENV}\r\n" \
                                                     "spec:\r\n  " \
                                                         f"description: {DESCRIPTION}"

    # Для проверки невалидного создания контура без его указания, только namespace
    DATA_ENV_WITHOUT_NAME: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                    "kind: Environment\r\n" \
                                    "metadata:\r\n  " \
                                        f"name: {IS}-\r\n" \
                                    "spec:\r\n  " \
                                        f"description: {DESCRIPTION}"

    # Для проверки невалидного создания контура (name 3 символа на латинице uppercase)
    ENV_NAME_LENGTH_3_ENGLISH_UPPER: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                            "kind: Environment\r\n" \
                                            "metadata:\r\n  " \
                                                f"name: {IS}-{ENV.upper()}\r\n" \
                                            "spec:\r\n  " \
                                                f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                                f"description: {DESCRIPTION}"

    # Для проверки невалидного создания контура (name 20 символов на латинице uppercase)
    ENV_NAME_LENGTH_20_ENGLISH_UPPER: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                            "kind: Environment\r\n" \
                                            "metadata:\r\n  " \
                                                f"name: {IS}-{ENV_LENGTH_21_ENGLISH.upper()[:20]}\r\n" \
                                            "spec:\r\n  " \
                                                f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                                f"description: {DESCRIPTION}"

    # Для проверки невалидного создания контура (name 3 символа на кириллице lowercase)
    ENV_NAME_LENGTH_3_RUSSIAN: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                      "kind: Environment\r\n" \
                                      "metadata:\r\n  " \
                                          f"name: {IS}-{ENV_MAXIMUM_LENGTH_RUSSIAN[:3]}\r\n" \
                                      "spec:\r\n  " \
                                          f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                          f"description: {DESCRIPTION}"

    #  Для проверки невалидного создания контура(name 3 символа на кириллице uppercase)
    ENV_NAME_LENGTH_3_RUSSIAN_UPPER: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                            "kind: Environment\r\n" \
                                            "metadata:\r\n  " \
                                                f"name: {IS}-{ENV_MAXIMUM_LENGTH_RUSSIAN[:3].upper()}\r\n" \
                                            "spec:\r\n  " \
                                                f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                                f"description: {DESCRIPTION}"

    # Для проверки невалидного создания контура (name 20 символов на кириллице lowercase)
    ENV_NAME_LENGTH_20_RUSSIAN: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                       "kind: Environment\r\n" \
                                       "metadata:\r\n  " \
                                           f"name: {IS}-{ENV_MAXIMUM_LENGTH_RUSSIAN[:20]}\r\n" \
                                       "spec:\r\n  " \
                                           f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                           f"description: {DESCRIPTION}"

    #  Для проверки невалидного создания контура(name 3 символов на кириллице uppercase)
    ENV_NAME_LENGTH_20_RUSSIAN_UPPER: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                             "kind: Environment\r\n" \
                                             "metadata:\r\n  " \
                                                 f"name: {IS}-{ENV_MAXIMUM_LENGTH_RUSSIAN[:20].upper()}\r\n" \
                                             "spec:\r\n  " \
                                                 f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                                 f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 3 цифры) c chatid
    ENV_NAME_NUMBERS_LENGTH_3: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                      "kind: Environment\r\n" \
                                      "metadata:\r\n  " \
                                          f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                      "spec:\r\n  " \
                                          f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                          f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 20 цифр) в существующем ns c chatid
    ENV_NAME_NUMBERS_LENGTH_20: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                      "kind: Environment\r\n" \
                                      "metadata:\r\n  " \
                                          f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:20]}\r\n" \
                                      "spec:\r\n  " \
                                          f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                          f"description: {DESCRIPTION}"

    # Для проверки невалидного создания контура (name-env - 2 цифры) в существующем ns c chatid
    DATA_NAME_NUMBERS_LENGTH_2_WITH_CHAT_ID: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                    "kind: Environment\r\n" \
                                                    "metadata:\r\n  " \
                                                        f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:2]}\r\n" \
                                                    "spec:\r\n  " \
                                                        f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                                        f"description: {DESCRIPTION}"

    # Для проверки невалидного создания контура (name-env - 21 цифра) в существующем ns c chat id
    DATA_NAME_NUMBERS_LENGTH_21_WITH_CHAT_ID: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                     "kind: Environment\r\n" \
                                                     "metadata:\r\n  " \
                                                         f"name: {IS}-{ENV_LENGTH_21_NUMBERS}\r\n" \
                                                     "spec:\r\n  " \
                                                         f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                                         f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 3 цифры) в существующем ns c chat id 65 цифр
    DATA_NAME_NUMBERS_LENGTH_2_WITH_CHAT_ID_65: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                       "kind: Environment\r\n" \
                                                       "metadata:\r\n  " \
                                                           f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                                       "spec:\r\n  " \
                                                           f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH}\"\r\n  " \
                                                           f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 3 цифры) в существующем ns c chat id 64 цифры
    DATA_NAME_NUMBERS_LENGTH_2_WITH_CHAT_ID_64: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                       "kind: Environment\r\n" \
                                                       "metadata:\r\n  " \
                                                           f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                                       "spec:\r\n  " \
                                                           f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:64]}\"\r\n  " \
                                                           f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 3 цифры) в существующем ns c chat id 1 цифра
    DATA_NAME_NUMBERS_LENGTH_2_WITH_CHAT_ID_1: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                       "kind: Environment\r\n" \
                                                       "metadata:\r\n  " \
                                                           f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                                       "spec:\r\n  " \
                                                           f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:1]}\"\r\n  " \
                                                           f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 3 цифры) в существующем ns c chat id 1 латинский символ в lowercase
    DATA_NAME_NUMBERS_LENGTH_3_WITH_CHAT_ID_ENGLISH: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                            "kind: Environment\r\n" \
                                                            "metadata:\r\n  " \
                                                                f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                                            "spec:\r\n  " \
                                                                f"chatid: \"{CHAT_ID_LENGTH_1_ENGLISH}\"\r\n  " \
                                                                f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 3 цифры) в существующем ns c chat id 1 кириллический символ в lowercase
    DATA_NAME_NUMBERS_LENGTH_3_WITH_CHAT_ID_RUSSIAN: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                            "kind: Environment\r\n" \
                                                            "metadata:\r\n  " \
                                                                f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                                            "spec:\r\n  " \
                                                                f"chatid: \"{CHAT_ID_LENGTH_1_RUSSIAN}\"\r\n  " \
                                                                f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 3 цифры) в существующем ns c chat id 1 спецсимвол
    DATA_NAME_NUMBERS_LENGTH_3_WITH_CHAT_ID_SPECIAL: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                            "kind: Environment\r\n" \
                                                            "metadata:\r\n  " \
                                                                f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                                            "spec:\r\n  " \
                                                                f"chatid: \"{CHAT_ID_LENGTH_1_SPECIAL}\"\r\n  " \
                                                                f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 3 цифры) в существующем ns c chat id 1 пробел
    DATA_NAME_NUMBERS_LENGTH_3_WITH_CHAT_ID_SPACE: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                            "kind: Environment\r\n" \
                                                            "metadata:\r\n  " \
                                                                f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                                            "spec:\r\n  " \
                                                                f"chatid: \"{CHAT_ID_LENGTH_1_SPACE}\"\r\n  " \
                                                                f"description: {DESCRIPTION}"

    # Для проверки создания контура (name-env - 3 цифры) в существующем ns c Description 1 символ
    DATA_NAME_NUMBERS_LENGTH_3_WITH_DESCRIPTION_1: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                          "kind: Environment\r\n" \
                                                          "metadata:\r\n  " \
                                                              f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                                          "spec:\r\n  " \
                                                              f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                                              f"description: {DESCRIPTION_MAXIMUM_LENGTH[:1]}"

    # Для проверки создания контура (name-env - 3 цифры) в существующем ns c Description 257 символов
    DATA_NAME_NUMBERS_LENGTH_3_WITH_DESCRIPTION_257: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                          "kind: Environment\r\n" \
                                                          "metadata:\r\n  " \
                                                              f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                                          "spec:\r\n  " \
                                                              f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                                              f"description: {DESCRIPTION_MAXIMUM_LENGTH}"

    # Для проверки создания контура (name-env - 3 цифры) в существующем ns c Description 256 символов
    DATA_NAME_NUMBERS_LENGTH_3_WITH_DESCRIPTION_256: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                                            "kind: Environment\r\n" \
                                                            "metadata:\r\n  " \
                                                                f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                                            "spec:\r\n  " \
                                                                f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                                                f"description: {DESCRIPTION_MAXIMUM_LENGTH[:256]}"

    # Для проверки создания контура с именем которое есть в информационной системе
    DATA_DUPLICATE_NAME: dict = "apiVersion: paas.akbars.tech/v1\r\n" \
                                "kind: Environment\r\n" \
                                "metadata:\r\n  " \
                                    f"name: {NAMESPACE}\r\n" \
                                "spec:\r\n  " \
                                    f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                    f"description: {DESCRIPTION_MAXIMUM_LENGTH[:19]}"

    # Для проверки создания контура с невалидным apiVersion
    DATA_INVALID_API_VERSION: dict = "apiVersion: v1\r\n" \
                                     "kind: Environment\r\n" \
                                     "metadata:\r\n  " \
                                         f"name: {IS}-{ENV_LENGTH_21_NUMBERS[:3]}\r\n" \
                                     "spec:\r\n  " \
                                         f"chatid: \"{CHAT_ID_MAXIMUM_LENGTH[:12]}\"\r\n  " \
                                         f"description: {DESCRIPTION_MAXIMUM_LENGTH[:19]}"

    VALIDATION_CREATE_ENV_WITH_INVALID_NAME_RUS = [
        #  Создать контур(name 3 символа на кириллице lowercase) в существующем ns
        ENV_NAME_LENGTH_3_RUSSIAN,
        #  Создать контур(name 3 символа на кириллице uppercase) в существующем ns
        ENV_NAME_LENGTH_3_RUSSIAN_UPPER,
        #  Создать контур(name 20 символов на кириллице lowercase) в существующем ns
        ENV_NAME_LENGTH_20_RUSSIAN,
        #  Создать контур(name 20 символов на кириллице uppercase) в существующем ns
        ENV_NAME_LENGTH_20_RUSSIAN_UPPER
    ]

    VALIDATION_CREATE_ENV_WITH_INVALID_NAME_ENG = [
        #  Создать контур(name 3 латинских символa в uppercase) в существующем ns
        [ENV_NAME_LENGTH_3_ENGLISH_UPPER, MESSAGE_NAME_LENGTH_3_ENG_UPPER_PAAS, MESSAGE_NAME_LENGTH_3_ENG_UPPER],
        #  Создать контур(name 20 латинских символoв в uppercase) в существующем ns
        [ENV_NAME_LENGTH_20_ENGLISH_UPPER, MESSAGE_NAME_LENGTH_20_ENG_UPPER_PAAS, MESSAGE_NAME_LENGTH_20_ENG_UPPER],
    ]

    # Варианты невалидного создания контура, проверка сообщения webhook сервера
    #  1-тело запроса; 2-сообщение webhook сервера
    VALIDATION_WEBHOOK_LENGTH = [
        # Невалидное создание контура (name-env=2 латинских символа) в существующем ns без chatid
        [DATA_ENV_NAME_LENGTH_2, ADMISSION_WEBHOOK_MESSAGE_NAME_LENGTH],
        # Невалидное создание контура (name-env=21 латинский символ) в существующем ns без chatid
        [DATA_ENV_NAME_LENGTH_21, ADMISSION_WEBHOOK_MESSAGE_NAME_LENGTH],
        # Невалидное создание контура (name-env=2 цифры) в существующем ns c chatid
        [DATA_NAME_NUMBERS_LENGTH_2_WITH_CHAT_ID, ADMISSION_WEBHOOK_MESSAGE_NAME_LENGTH],
        # Невалидное создание контура (name-env=21 цифра) в существующем ns c chatid
        [DATA_NAME_NUMBERS_LENGTH_21_WITH_CHAT_ID, ADMISSION_WEBHOOK_MESSAGE_NAME_LENGTH],
        # Невалидное создание контура (name-env=21 цифра) в существующем ns c chatid
        [DATA_NAME_NUMBERS_LENGTH_2_WITH_CHAT_ID_65, ADMISSION_WEBHOOK_MESSAGE_CHAT_ID_LENGTH],
        # Невалидное создание контура (name-env=3 цифры) в существующем ns с chat id=1 латинский символ в lowercase
        [DATA_NAME_NUMBERS_LENGTH_3_WITH_CHAT_ID_ENGLISH, ADMISSION_WEBHOOK_MESSAGE_CHAT_ID_FORMAT],
        # Невалидное создание контура (name-env=3 цифры) в существующем ns с chat id=1 кириллический символ в lowercase
        [DATA_NAME_NUMBERS_LENGTH_3_WITH_CHAT_ID_RUSSIAN, ADMISSION_WEBHOOK_MESSAGE_CHAT_ID_FORMAT],
        # Невалидное создание контура (name-env=3 цифры) в существующем ns с chat id=1 спецсимвол
        [DATA_NAME_NUMBERS_LENGTH_3_WITH_CHAT_ID_SPECIAL, ADMISSION_WEBHOOK_MESSAGE_CHAT_ID_FORMAT],
        # Невалидное создание контура (name-env=3 цифры) в существующем ns с chat id=1 пробел
        [DATA_NAME_NUMBERS_LENGTH_3_WITH_CHAT_ID_SPACE, ADMISSION_WEBHOOK_MESSAGE_CHAT_ID_FORMAT],
        # Невалидное создание контура (name-env=3 цифры) в существующем ns с Description=1 символ
        [DATA_NAME_NUMBERS_LENGTH_3_WITH_DESCRIPTION_1, ADMISSION_WEBHOOK_MESSAGE_DESCRIPTION_FORMAT],
        # Невалидное создание контура (name-env=3 цифры) в существующем ns с Description=257 символов
        [DATA_NAME_NUMBERS_LENGTH_3_WITH_DESCRIPTION_257, ADMISSION_WEBHOOK_MESSAGE_DESCRIPTION_LENGTH],
        # Невалидное создание контура (name-env=3 лат. символа в lowercase) в существующем ns без названия namespace
        [DATA_ENV_NAME_LENGTH_3_WITHOUT_NAMESPACE, ADMISSION_WEBHOOK_MESSAGE_DELIMITER],

    ]

    VALIDATION_CREATE_ENV_WITHOUT_CHAT_ID = [
        #  1-тело запроса; 2-контур; 3-информационная система
        #  Создать контур(name 3 латинских символa в lowercase) в существующем ns без chat id
        [DATA_ENV_WITHOUT_CHAT_ID, ENV_LENGTH_21_ENGLISH[:3], IS],
        #  Создать контур(name 20 латинских символов в lowercase) в существующем ns без chat id
        [ENV_NAME_LENGTH_20_ENGLISH, ENV_LENGTH_21_ENGLISH[:20], IS],
    ]

    VALIDATION_CREATE_ENV_WITH_CHAT_ID = [
        #  1-тело запроса; 2-контур; 3-информационная система; 4-chat id
        #  Создать контур(name=3 латинских символa в lowercase) в существующем ns с chat id
        [ENV_NAME_LENGTH_3_ENGLISH, ENV_LENGTH_21_ENGLISH[:3], IS, CHAT_ID_MAXIMUM_LENGTH[:12]],
        #  Создать контур(name=3 цифры) в существующем ns с chat id
        [ENV_NAME_NUMBERS_LENGTH_3, ENV_LENGTH_21_NUMBERS[:3], IS, CHAT_ID_MAXIMUM_LENGTH[:12]],
        #  Создать контур(name=20 цифр) в существующем ns с chat id
        [ENV_NAME_NUMBERS_LENGTH_20, ENV_LENGTH_21_NUMBERS[:20], IS, CHAT_ID_MAXIMUM_LENGTH[:12]],
        #  Создать контур(name=3 цифры) в существующем ns с chat id=64 цифры
        [DATA_NAME_NUMBERS_LENGTH_2_WITH_CHAT_ID_64, ENV_LENGTH_21_NUMBERS[:3], IS, CHAT_ID_MAXIMUM_LENGTH[:64]],
        #  Создать контур(name=3 цифры) в существующем ns с chat id=1 цифра
        [DATA_NAME_NUMBERS_LENGTH_2_WITH_CHAT_ID_1, ENV_LENGTH_21_NUMBERS[:3], IS, CHAT_ID_MAXIMUM_LENGTH[:1]],
    ]

    VALIDATION_DELETE_ENV = [
        #  1-url; 2-
        #  Удаление существующего Env
        [URL_ENVIRONMENTS_WITH_NAMESPACE],
        #  Удаление несуществующего Env
        [ENV_NAME_NUMBERS_LENGTH_3],
    ]