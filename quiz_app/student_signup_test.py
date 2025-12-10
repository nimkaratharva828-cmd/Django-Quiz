from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/path/to/chromedriver.exe")
driver.get("http://127.0.0.1:8000/signup/")

# Fill in signup fields
driver.find_element(By.NAME, "email").send_keys("newstudent@example.com")
driver.find_element(By.NAME, "username").send_keys("newstudent")
driver.find_element(By.NAME, "password").send_keys("newpassword123")

# Submit the form
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)
print("Page after signup:", driver.title)
driver.quit()
