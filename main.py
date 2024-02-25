import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
driver = chrome
driver.get("https://neal.fun/infinite-craft/")
driver.set_window_size(500, 3000)

paused = False

def toggle_pause():
    global paused
    paused = not paused
    if paused:
        print("Paused")
    else:
        print("Resumed")

keyboard.add_hotkey('ctrl+shift+p', toggle_pause)

base = 0
while True:
    if not paused:
        try:
            master = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[6]")
            children = master.find_elements(By.CLASS_NAME, "item")
            for i in range(len(children) - base):
                for x in range(len(children) - i - base):
                    try:
                        children[i].click()
                        children[i + x + base].click()
                        time.sleep(0.5)
                    except:
                        time.sleep(0.1)
            base = len(children)
        except:
            time.sleep(0.5)
    else:
        time.sleep(0.1)  # Sleep to avoid high CPU usage
