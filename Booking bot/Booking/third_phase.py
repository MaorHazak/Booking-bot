from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# This file clicks on specific days in a month and clicks on search.

def third_phase(driver):
    try:
        # קבלת תאריכי התחלה וסיום מהמשתמש
        start_date = input("Please enter the start date (format: YYYY-MM-DD): ").strip()
        end_date = input("Please enter the end date (format: YYYY-MM-DD): ").strip()

        # Click on the first date
        first_date = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[@data-date='{start_date}']"))
        )
        time.sleep(2)
        first_date.click()
        # print(f"Clicked on the first date: {start_date}")

        # Click on the second date
        second_date = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[@data-date='{end_date}']"))
        )
        time.sleep(2)
        second_date.click()
        # print(f"Clicked on the second date: {end_date}")
        
        # Click on the search button
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and .//span[text()='Search']]"))
        )
        search_button.click()
        # print("Clicked on the search button.")
        time.sleep(2)

    except Exception as e:
        print(f"Error occurred in third phase: {e}. Retrying...")
        time.sleep(2)  # Brief pause before retrying

