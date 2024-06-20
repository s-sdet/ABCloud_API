from fixtures.base import BaseClass
from fixtures.info_system.api import InfoSystem
from fixtures.info_system.environment.api import Env
from fixtures.info_system.environment.config_maps.api import ConfigMaps
from fixtures.info_system.environment.deployments.api import Deployments
from fixtures.info_system.environment.ingresses.api import Ingresses
from fixtures.info_system.environment.pods.api import Pods
from fixtures.info_system.environment.secrets.api import Secrets
from fixtures.info_system.environment.services.api import Services


class App:
    def __init__(self, url: str):
        self.url = url
        self.base = BaseClass
        self.info_system = InfoSystem(self)
        self.env = Env(self)
        self.cm = ConfigMaps(self)
        self.deployments = Deployments(self)
        self.ingresses = Ingresses(self)
        self.pods = Pods(self)
        self.secrets = Secrets(self)
        self.services = Services(self)
