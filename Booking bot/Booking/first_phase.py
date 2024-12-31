from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# This file adding adult and searching for destination.
def first_phase(driver):
    try:
        pre_child_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-testid='occupancy-config-icon']"))
            )
        driver.execute_script("arguments[0].scrollIntoView(true);", pre_child_button) #scroll to view
        time.sleep(2)
        pre_child_button.click()
        # print("pre_child_button clicked successfully.")


        plus_parent = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "path[d='M20.25 11.25h-7.5v-7.5a.75.75 0 0 0-1.5 0v7.5h-7.5a.75.75 0 0 0 0 1.5h7.5v7.5a.75.75 0 0 0 1.5 0v-7.5h7.5a.75.75 0 0 0 0-1.5']")
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", plus_parent)
        time.sleep(2)
        plus_parent.click()
        time.sleep(2)
        
        done_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Done']]"))
        )
        done_button.click()

        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Where are you going?']"))
        )
        input_box.clear()
        destination = input("Please enter your destination: ")  # מבקש מהמשתמש להזין יעד
        input_box.send_keys(destination)
        # input_box.send_keys("New York")
        # input_box.send_keys(Keys.ENTER)

        time.sleep(2)
        result_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@id='autocomplete-result-0']"))
        )
        result_element.click()
        time.sleep(5)
        


    except Exception as e:
        print(f"No popup found or unable to dismiss it from first phase: {e}")

