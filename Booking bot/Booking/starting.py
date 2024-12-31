from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

# This file handling popup window to be closed if apear.
def starting(driver):
    try:
        exit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Dismiss sign-in info.']"))
        )
        time.sleep(2)
        exit_button.click()
        time.sleep(1)
        # print("Popup dismissed successfully.")
    except TimeoutException:
        # אם ה-popup לא מופיע תוך 10 שניות
        print("No popup found. Continuing... (starting)")
    except Exception as e:
        print(f"No popup found or unable to dismiss it: (starting) {e}")