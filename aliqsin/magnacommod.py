from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.example.com Wait for the settings button to be clickable
wait = WebDriverWait(driver, 10)
settings_button = wait.until(EC.element_to_be_clickable((By.XPATH, SETTINGS)))

# Click the settings button
settings_button.click()
