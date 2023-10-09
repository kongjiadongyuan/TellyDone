from typing import List, Dict
import os
import time
import apprise


def proc_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def watch(config: Dict, pid: int):
    apprise_url_list = config.get("apprise_url", [])
    watch_config = config.get("watch")
    continuous = watch_config.get("continuous", False)
    interval = watch_config.get("interval", 1800)

    last_check = 0

    notifier = apprise.Apprise()
    for apprise_url in apprise_url_list:
        notifier.add(apprise_url)
    notifier.add(config)

    start_time = time.time()
    while True:
        if proc_alive(pid):
            time.sleep(0.1)
        else:
            break
        current_time = time.time()

        if current_time - last_check > interval:
            if continuous:
                notifier.notify(
                    title=f"Process {pid} is still alive",
                    body=f"Runned for {current_time - start_time: .2f} seconds.",
                )
            last_check = (current_time // interval) * interval
    end_time = time.time()

    notifier.notify(
        title=f"Process {pid} finished",
        body=f"Runned for {end_time - start_time: .2f} seconds.",
    )


if __name__ == "__main__":
    pass
