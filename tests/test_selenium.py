import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup headless Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize the Chrome WebDriver with options
driver = webdriver.Chrome(options=options)

def test_form_submission():
    driver.get("http://localhost:8000/")

    # Wait until elements are visible before interacting
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname")))
    
    # Fill out the form
    driver.find_element(By.ID, "firstname").send_keys("John")
    driver.find_element(By.ID, "lastname").send_keys("Doe")
    driver.find_element(By.ID, "pwd").send_keys("password123")
    driver.find_element(By.ID, "male").click()
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # Submit the form
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Wait for the page to load after form submission
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "confirmationMessage")))

    # Validate the form submission
    assert "Form submitted successfully" in driver.page_source

    driver.quit()
