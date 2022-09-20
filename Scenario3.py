from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

chrome_path = Service(r'C:\Drivers\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_path)
driver.get("https://www.lambdatest.com/selenium-playground/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='seleniumform']/div[6]/button").click()

driver.find_element(By.XPATH, "//*[@id='seleniumform']/div[6]/button").click()
msg = driver.find_element(By.XPATH, "//input[@id='name']").get_attribute(name="validationMessage")
print(msg)
assert "Please fill out this field." in msg
time.sleep(2)

driver.find_element(By.NAME, "name").send_keys("chandu")
time.sleep(1)
driver.find_element(By.ID, "inputEmail4").send_keys("chandu@gmail.com")
time.sleep(1)
driver.find_element(By.ID, "inputPassword4").send_keys("12345")
time.sleep(1)
driver.find_element(By.ID, "company").send_keys("chandu")
time.sleep(1)
driver.find_element(By.ID,"websitename").send_keys("lambdtest")
time.sleep(1)
country = Select(driver.find_element(By.NAME, "country"))
country.select_by_visible_text("United States")
driver.find_element(By.ID, "inputCity").send_keys("city")
time.sleep(1)
driver.find_element(By.ID,"inputAddress1").send_keys("aaaaa")
time.sleep(1)
driver.find_element(By.ID,"inputAddress2").send_keys("Aaaaa")
time.sleep(1)
driver.find_element(By.ID,"inputState").send_keys("Andhra Pradesh")
time.sleep(1)
driver.find_element(By.ID,"inputZip").send_keys("524555")
time.sleep(2)
#driver.find_element(By.CSS_SELECTOR, "#seleniumform > div.text-right.mt-20 > button").click()
driver.find_element(By.XPATH, "//*[@id='seleniumform']/div[6]/button").click()

messag = driver.find_element(By.XPATH, "//*[@id='__next']/div/section[3]/div/div/div[2]/div").text
assert "Thanks for contacting us, we will get back to you shortly." in messag