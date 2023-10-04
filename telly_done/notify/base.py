from abc import ABC, abstractmethod
from typing import Dict


class ConfigError(Exception):
    def __init__(self, m: str, config: Dict):
        super().__init__(m)
        self.origin_config = config


class ConfigInvalid(Exception):
    def __init__(self, m: str, config: Dict):
        super().__init__(m)
        self.origin_config = config


class MessageFormatError(Exception):
    def __init__(self, m: str, message: Dict):
        super().__init__(m)
        self.origin_message = message


class NotifyFailed(Exception):
    def __init__(self, m: str, exception: Exception, trace: str):
        super().__init__(m)
        self.origin_exception = exception
        self.origin_trace = trace


class NotifierBase(ABC):
    @abstractmethod
    def __init__(self, config: dict):
        pass

    @abstractmethod
    def do_notify(self, message: Dict):
        pass
