from typing import List, Dict
import os
import time
import apprise


def execute(config: Dict, args: List[str]):
    apprise_url_list = config.get("apprise_url", [])

    apobj = apprise.Apprise()
    for apprise_url in apprise_url_list:
        apobj.add(apprise_url)
    apobj.add(config)

    command = " ".join(args)
    start_time = time.time()
    return_value = os.system(command=command)
    end_time = time.time()

    used_time = end_time - start_time

    title = "Execution FAIL" if return_value else "Execution SUCCEED"
    content = f"""Command: {command}
    Execution time: {used_time: .2f} seconds
    Return Value: {return_value}"""

    apobj.notify(body=content, title=title)


if __name__ == "__main__":
    config = {"apprise_url": ["schan://XXXXXXX/"]}
    execute(config, ["echo", "hello"])
