from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set path to your chromedriver
driver = webdriver.Chrome(executable_path="C:/path/to/chromedriver.exe")

# 1. Open Django login page
driver.get("http://127.0.0.1:8000/login/")

# 2. Fill in email and password
driver.find_element(By.NAME, "email").send_keys("student@example.com")
driver.find_element(By.NAME, "password").send_keys("student123")

# 3. Click the login button (button[type='submit'])
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# 4. Wait and print the resulting title
time.sleep(3)
print("Page after login:", driver.title)

# 5. Quit
driver.quit()
