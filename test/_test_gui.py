import os
import signal
import time
import subprocess
import pyautogui
from pathlib import Path

EXAMPLES_DIR = os.path.join(Path.cwd().parent, "examples")
EXAMPLES = [os.path.join(EXAMPLES_DIR, example) for example in os.listdir("../examples")]


def _kill_example(pid: int):
    os.killpg(os.getpgid(pid), signal.SIGTERM)

def _open_example_app(example_path: str, example_name: str):
    try:        
        proc = subprocess.Popen(["/bin/bash", "run_example.sh", example_name], start_new_session=True)
        time.sleep(2)
        cords = pyautogui.locateCenterOnScreen("imgs/button.png")
        pyautogui.click(cords.x, cords.y)
        time.sleep(2)
        new_cords = pyautogui.locateCenterOnScreen("imgs/button2.png")
        print(f"{cords} VS {new_cords}")
        assert (cords.x, cords.y) != (new_cords.x, new_cords.y)
    finally:
        _kill_example(proc.pid)

for example in EXAMPLES:
    example_name = example.split("/")[-1]
    if example_name != "button":
        continue
    _open_example_app(example, example_name)
    
