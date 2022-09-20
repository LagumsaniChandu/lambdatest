from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

chrome_path = Service(r'C:\Drivers\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_path)
driver.get("https://www.lambdatest.com/selenium-playground/")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click()
time.sleep(4)

elem = driver.find_element(By.XPATH, "//*[@id='slider3']/div/input")
ActionChains(driver).drag_and_drop_by_offset(elem,120, 0).perform()

slidder=driver.find_element(By.XPATH, "//*[@id='rangeSuccess']").text
assert "95" in slidder