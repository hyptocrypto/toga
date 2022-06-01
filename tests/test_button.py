import time
import pyautogui
from utils import EXAMPLE_DIRS, run_example_app
import pytest


def test_button():
    def _test_button():
        time.sleep(5)
        cords = pyautogui.locateCenterOnScreen("imgs/button.png")
        breakpoint()
        pyautogui.click(cords.x, cords.y)
        time.sleep(2)
        new_cords = pyautogui.locateCenterOnScreen("imgs/button2.png")
        print(f"{cords} VS {new_cords}")
        assert (cords.x, cords.y) != (new_cords.x, new_cords.y)

    assert run_example_app("button", _test_button)
