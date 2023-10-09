from typing import List, Dict
import yaml
import pwd
import os


def home_dir():
    uid = os.getuid()
    maybe_prev_uid = os.environ.get("SUDO_UID")
    if maybe_prev_uid is not None:
        uid = int(maybe_prev_uid)
    return pwd.getpwuid(uid).pw_dir


default_config_file_list = []
default_config_file_list.append(os.path.join(home_dir(), ".telly_done"))
default_config_file_list.append("/etc/telly_done")


def get_config(specified_path: str = None) -> Dict:
    if specified_path is not None:
        with open(specified_path, "r") as f:
            try:
                config = yaml.safe_load(f)
                return config
            except Exception:
                return {}
    else:
        for config_file in default_config_file_list:
            if os.path.exists(config_file):
                with open(config_file, "r") as f:
                    try:
                        config = yaml.safe_load(f)
                        return config
                    except Exception:
                        pass
        return {}
