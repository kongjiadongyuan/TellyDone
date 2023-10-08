from abc import ABC, abstractmethod
from typing import Dict


class ConfigFormatError(Exception):
    # This exception should be thrown when the incoming configuration cannot be parsed.
    # This exception should not be handled as it is the developer's issue.
    def __init__(self, m: str, config: Dict):
        super().__init__(m)
        self.origin_config = config


class ConfigInvalid(Exception):
    # This exception should be thrown when the notifier cannot be activated properly in the current configuration.
    # This exception should be handled.
    def __init__(self, m: str, config: Dict):
        super().__init__(m)
        self.origin_config = config


class MessageFormatError(Exception):
    # This exception should be thrown when the incoming message cannot be parsed.
    # This exception should not be handled as it is the developer's issue.
    def __init__(self, m: str, message: Dict):
        super().__init__(m)
        self.origin_message = message


class NotifyFailed(Exception):
    # This exception should be thrown when the notifier works but fails.
    # This exception should be handled.
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
