import pyautogui
import time
import random
import math

RUNNING_TIME = 3600
MAX_INTERVAL = 10   # maximum interval between clicks
pyautogui.FAILSAFE = True
MODE = 1    # 13s: mode=1; 23s: mode=2


def _uniform_click(center_x, center_y, radius=5):
    r = radius * math.sqrt(random.uniform(0, 1))
    theta = random.uniform(0, 2 * math.pi)
    x = int(center_x + r * math.cos(theta))
    y = int(center_y + r * math.sin(theta))
    pyautogui.click(x, y)
    # TODO


def _gaussian_click(center_x, center_y, radius=5):
    sigma = radius / 3
    r = min(abs(random.normalvariate(0, sigma)), radius)
    theta = random.uniform(0, 2 * math.pi)
    x = int(center_x + r * math.cos(theta))
    y = int(center_y + r * math.sin(theta))
    pyautogui.click(x, y)
    # TODO


def fight_scenario():
    button_location = pyautogui.locateCenterOnScreen('fight.png')
    if button_location:
        button_center = pyautogui.center(button_location)
        decision = abs(random.normalvariate(0, 1))
        if decision > 1:
            _gaussian_click(button_center.x, button_center.y)
        else:
            _uniform_click(button_center.x, button_center.y)

        time.sleep(13) if MODE == 1 else time.sleep(23)
    else:
        print("No button found. Restarting...")
        time.sleep(random.random())
        fight_scenario()

    pass


def _handling_overload():
    """
    When exceeding the amount, one essential click must be deployed.
    :return: click THAT button
    """
    pass


def _click_series():
    decision = random.randint(0, 1)
    screen_width, screen_height = pyautogui.size()
    sgm = 10
    _bias_x, _bias_y = min(abs(random.normalvariate(0, sgm)), 30), min(abs(random.normalvariate(0, sgm)), 30)
    _rect_x = random.randint(screen_width / 2 - 200, screen_width / 2 + 200)
    _rect_y = random.randint(screen_height * 2 / 3 - 100, screen_height * 2 / 3 + 100)
    _final_x = min(abs(random.normalvariate(_rect_x, 2 * sgm)), 60) + _bias_x
    _final_y = min(abs(random.normalvariate(_rect_y, 2 * sgm)), 60) + _bias_y
    if decision > 0.6:
        pyautogui.click(_final_x, _final_y)
    elif decision > 0.2:
        for _ in range(2):
            pyautogui.click(_final_x, _final_y)
    elif decision > 0.1:
        for _ in range(3):
            pyautogui.click(_final_x, _final_y)
    else:
        for _ in range(4):
            pyautogui.click(_final_x, _final_y)

    # TODO


def end_scenario():

    pass


def run():
    print("Start")
    print(f"Duration: {RUNNING_TIME / 60} min")
    for i in range(3, 0, -1):
        print(f"Starting in {i} s", end="\r")
        time.sleep(1)
    print("Start now")
    screen_width, screen_height = pyautogui.size()
    start_time = time.time()

    try:
        while time.time() - start_time < RUNNING_TIME:
            fight_scenario()
            end_scenario()
    except KeyboardInterrupt:
        print("Ctrl+C")
    except pyautogui.FailSafeException:
        print("Safe Exception")
    print("\nOver")


if __name__ == "__main__":
    run()
