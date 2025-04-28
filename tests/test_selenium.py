from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def test_form_submission():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://form-page-gcdebhh2a5d4euhz.centralindia-01.azurewebsites.net/")

        wait = WebDriverWait(driver, 10)

        # Wait until form fields are present
        firstname_input = wait.until(EC.presence_of_element_located((By.ID, "firstname")))
        lastname_input = driver.find_element(By.ID, "lastname")
        password_input = driver.find_element(By.ID, "pwd")
        gender_radio = driver.find_element(By.ID, "male")
        email_input = driver.find_element(By.ID, "email")

        # Fill the form
        firstname_input.send_keys("John")
        lastname_input.send_keys("Doe")
        password_input.send_keys("password123")
        gender_radio.click()
        email_input.send_keys("john.doe@example.com")

        # Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        submit_button.click()

        # Wait for confirmation (assuming the page shows some success text)
        time.sleep(2)  # You can also wait for a specific element

        assert "Form submitted successfully" in driver.page_source, "Success message not found!"

    except TimeoutException:
        print("Test failed due to timeout while waiting for page elements.")
    finally:
        driver.quit()

# Run the test
test_form_submission()
