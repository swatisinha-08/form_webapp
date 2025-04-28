import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Setup headless Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")  # Added for better headless compatibility

# Initialize the Chrome WebDriver with options
driver = webdriver.Chrome(options=options)

def test_form_submission():
    try:
        driver.get("https://form-page-gcdebhh2a5d4euhz.centralindia-01.azurewebsites.net/")

        # Wait until the first input element is visible before interacting
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname")))

        # Fill out the form
        driver.find_element(By.ID, "firstname").send_keys("John")
        driver.find_element(By.ID, "lastname").send_keys("Doe")
        driver.find_element(By.ID, "pwd").send_keys("password123")
        driver.find_element(By.ID, "male").click()
        driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Wait for confirmation message to appear after form submission
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "confirmationMessage")))

        # Validate the form submission
        confirmation_message = driver.find_element(By.ID, "confirmationMessage").text
        assert "Form submitted successfully" in confirmation_message, f"Form submission failed: {confirmation_message}"

    except TimeoutException as e:
        print("Timeout occurred while waiting for elements:", e)
    except NoSuchElementException as e:
        print("Element not found:", e)
    except AssertionError as e:
        print(f"Assertion error: {e}")
    finally:
        driver.quit()

test_form_submission()
