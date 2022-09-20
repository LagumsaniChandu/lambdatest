import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_path = Service(r'C:\Drivers\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_path)

driver.get("https://www.lambdatest.com/selenium-playground/")
assert "Simple Form Demo" in "Simple Form Demo"
print("url is validated")
driver.find_element(By.PARTIAL_LINK_TEXT, "Simple Form Demo").click()
time.sleep(5)

string = "Welcome to LambdaTest"
driver.find_element(By.ID, "user-message").send_keys(string)
driver.find_element(By.ID, "showInput").click()

assert "Welcome to LambdaTest" in string
print("same text message is displayed")