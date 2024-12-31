from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# This file move forward the month to get the specific month we want.
        
def second_phase(driver):
    """Checks for February 2025 and March 2025 in the calendar and clicks next if not found."""
    target_month = input("Please enter month (e.g., 'February 2025'): ").strip()
    while True:
        try:
            # Handle popup if it appears
            # handle_popup(driver)

            # Find and validate the left month
            left_month_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//h3[@class='e1eebb6a1e ee7ec6b631'])[1]"))
            )
            left_month = left_month_element.text.strip()

            # Find and validate the right month
            right_month_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//h3[@class='e1eebb6a1e ee7ec6b631'])[2]"))
            )
            right_month = right_month_element.text.strip()

            # print(f"Left month: '{left_month}', Right month: '{right_month}'")

            # Check if the target months are found
            if left_month == target_month:
                # print("Found February on the left and March on the right! Exiting loop.")
                break

            # Click next button to navigate
            # print("Target months not found. Clicking next...")

            next_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Next month']"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            time.sleep(2)
            next_button.click()
            


        except Exception as e:
            print(f"Error occurred on second phase: {e}. Retrying...")
            time.sleep(2)  # Brief pause before retrying

