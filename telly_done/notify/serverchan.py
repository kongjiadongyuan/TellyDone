from .base import NotifierBase, MessageFormatError, ConfigFormatError, NotifyFailed
from typing import Dict
import traceback
import requests
import json

format_string = "https://sctapi.ftqq.com/{sendkey}.send"


class ServerchanNotifier(NotifierBase):
    def __init__(self, config: dict):
        self.config = config
        if self.config.get("sendkey") is None:
            raise ConfigFormatError("sendkey is required", config)
        self.url = format_string.format(sendkey=self.config["sendkey"])

    def do_notify(self, message: Dict):
        title = message.get("title", None)
        desp = message.get("desp", None)
        short = message.get("short", None)
        channel = message.get("channel", None)

        if title is None:
            raise MessageFormatError("title is required", message)

        data = {"title": title}
        if desp is not None:
            data["desp"] = desp
        if short is not None:
            data["short"] = short
        if channel is not None:
            data["channel"] = channel

        # header = "Content-Type: application/json;charset=utf-8"
        headers = {
            "Content-Type": "application/json",
            "charset": "utf-8",
        }
        try:
            response = requests.post(
                self.url, data=json.dumps(data), headers=headers, timeout=10
            )
            response.raise_for_status()
        except Exception as e:
            raise NotifyFailed("Notify failed", e, traceback.format_exc())


if __name__ == "__main__":
    serverchan = ServerchanNotifier({"sendkey": "test"})
    serverchan.do_notify({"title": "testtitle", "desp": "test", "short": "test"})
