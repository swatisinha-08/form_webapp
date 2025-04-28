import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_form_submission():
    driver = webdriver.Chrome()  # Assumes chromedriver is installed
    driver.get("http://localhost:8000/")

    driver.find_element(By.ID, "firstname").send_keys("John")
    driver.find_element(By.ID, "lastname").send_keys("Doe")
    driver.find_element(By.ID, "pwd").send_keys("password123")
    driver.find_element(By.ID, "male").click()
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    time.sleep(1)  # Just to see before submission
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    time.sleep(2)  # Wait to observe the result
    assert "Form submitted successfully" in driver.page_source

    driver.quit()
