from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import winsound
import json


# ---- SETTINGS ----
URL = json.load(open("urls.json"))["new-orders-notifier"]
CHECK_INTERVAL = 5
# ------------------
options = Options()
options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(URL)

print("Monitoring started...")

last_value = 0

while True:
    try:
        print("Checking for new orders...")
        time.sleep(2)

        badge = driver.find_element(By.CSS_SELECTOR, "button span.text-xs.font-bold")
        current_value = int(badge.text.strip())

        print("Current:", current_value, "| Last:", last_value)

        # 🚨 Only alert if it increased
        if current_value > last_value:
            print("🚨 NEW ORDER DETECTED!")
            winsound.Beep(1500, 700)

        # If it reset to 0, just update silently
        last_value = current_value

        driver.refresh()
        time.sleep(CHECK_INTERVAL)

    except Exception as e:
        print("Error:", e)
        time.sleep(CHECK_INTERVAL)