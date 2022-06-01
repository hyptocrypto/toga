import os
import signal
import time
import subprocess
from typing import Callable
import pyautogui
from pathlib import Path

EXAMPLE_DIRS = {
    example: os.path.join(os.path.join(Path.cwd().parent, "examples"), example)
    for example in os.listdir(os.path.join(Path.cwd().parent, "examples"))
    if example
    in [
        "button",
        "box",
    ]
}


def _kill_example(pid: int):
    os.killpg(os.getpgid(pid), signal.SIGTERM)


def run_example_app(example_name: str, test: Callable):
    proc = None
    try:
        proc = subprocess.Popen(
            ["/bin/bash", "run_example.sh", example_name], start_new_session=True
        )
        test()
    finally:
        if proc:
            _kill_example(proc.pid)
