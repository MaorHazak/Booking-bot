from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Booking.starting import starting  # ייבוא הפונקציה מקובץ starting.py
from Booking.first_phase import first_phase  
from Booking.second_phase import second_phase 
from Booking.third_phase import third_phase 
from Booking.last_phase import last_phase

# from first_phase import search_destination
# from second_phase import select_month
# from third_phase import select_dates

def main():
    # הגדרות הדרייבר
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    # options.add_argument("--headless")
    options.add_experimental_option("detach", True)    # משאיר את הדפדפן פתוח אחרי הרצה
    
    # יצירת דרייבר עם WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get("https://www.booking.com")  # החלף ב-URL של האתר הרצוי
        starting(driver)  
        first_phase(driver)  
        second_phase(driver)
        third_phase(driver)
        last_phase(driver)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pass  

if __name__ == "__main__":
    main()
