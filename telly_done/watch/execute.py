from typing import List

import os


def execute(args: List[str]):
    command = " ".join(args)
    return_value = os.system(command=command)
