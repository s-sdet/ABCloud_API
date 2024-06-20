from dataclasses import dataclass

@dataclass
class Auth:
    url_keycloak: str = ""
    login: str = ""
    password: str = ""
    client_id: str = ""
    realm_name: str = ""
    client_secret_key: str = ""
    url_k8s: str = ""

class Payload:
    payload_is: str = "apiVersion: paas.akbars.tech/v1\r\n" \
                      "kind: InformationSystem\r\n" \
                      "metadata:\r\n  " \
                      "name: abs03\r\nspec:\r\n  " \
                      "businessname: aws\r\n  " \
                      "prefix: \"test\"\r\n  " \
                      "state: \"pilot\"\r\n  " \
                      "description: \"TEST\""

class TestNameResource:
    names_is = [
        ("testdeploy"),
        ("finmarket"),
        ("abs03"),
        ("te")
    ]