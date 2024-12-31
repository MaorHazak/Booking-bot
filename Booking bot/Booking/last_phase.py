from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# This file clicks on sort from low to high and export the data from the page.

def last_phase(driver):
    try:
        # Click on the "Sort by: Top Picks for Groups" button
        sort_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='sorters-dropdown-trigger']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", sort_button) #scroll to view
        sort_button.click()
        time.sleep(2)
        # print("Clicked on the sort button.")
        
        #click on sort from low to high price
        price_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-id='price']"))
        )
        price_button.click()
        time.sleep(5)
        # print("Clicked on the 'Price (lowest first)' button.")
        
        
        hotels = driver.find_elements(By.CSS_SELECTOR, '[data-testid="property-card"]')
        table = PrettyTable(["Name", "Location", "Price", "Rating"])
        table.hrules = 1
        
        # If hotel divs are found
        if hotels:
            for index, hotel in enumerate(hotels[:10]):
                try:
                    # Retrieve hotel name
                    name = hotel.find_element(By.CSS_SELECTOR, '[data-testid="title"]').text

                    # Retrieve hotel location
                    try:
                        location = hotel.find_element(By.CSS_SELECTOR, '[data-testid="address"]').text
                    except Exception:
                        location = "N/A"

                    # Retrieve hotel price
                    try:
                        price = hotel.find_element(By.CSS_SELECTOR, '[data-testid="price-and-discounted-price"]').text
                    except Exception:
                        price = "N/A"

                    # Retrieve hotel rating
                    try:
                        rating = hotel.find_element(By.CSS_SELECTOR, '[data-testid="review-score"]').text
                    except Exception:
                        rating = "N/A"
                        
                    # try:
                    #     stars_element = hotel.find_element(By.CSS_SELECTOR, "div[data-testid='rating-stars']")
                    #     stars = stars_element.get_attribute("aria-label")  # Get the aria-label that describes the stars
                    # except Exception:
                    #     stars = "N/A"

                    # Add the data to the table
                    table.add_row([name, location, price, rating])
                except Exception as e:
                    print(f"Error occurred: {e}")
            
            # Print the table
            print(table)
        else:
            print("No hotels found.")
            

    except Exception as e:
        print(f"Error occurred in last phase: {e}. Retrying...")
        time.sleep(2)  # Brief pause before retrying
