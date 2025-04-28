from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_form_submission():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get("https://form-page-gcdebhh2a5d4euhz.centralindia-01.azurewebsites.net/")

    # Wait for the page to load and the elements to be interactable
    time.sleep(2)  # Can be replaced with WebDriverWait for better control

    # Find the form elements (adjust element locators if necessary)
    firstname_input = driver.find_element(By.ID, "firstname")  # Adjust the ID as per the form
    lastname_input = driver.find_element(By.ID, "lastname")
    password_input = driver.find_element(By.ID, "pwd")
    gender_radio = driver.find_element(By.ID, "male")  # Select male (adjust if different)
    email_input = driver.find_element(By.ID, "email")
    
    # Fill out the form
    firstname_input.send_keys("John")
    lastname_input.send_keys("Doe")
    password_input.send_keys("password123")
    gender_radio.click()  # Assuming 'male' is selected
    email_input.send_keys("john.doe@example.com")

    # Submit the form
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    submit_button.click()

    # Wait for a few seconds to allow submission to process
    time.sleep(3)  # Adjust as necessary based on response time

    # Validate successful form submission (adjust validation logic if needed)
    assert "Form submitted successfully" in driver.page_source

    driver.quit()

# Call the test function
test_form_submission()
