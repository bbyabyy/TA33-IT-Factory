import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# creeem un nou obiect chrome al clasei chrome din libraria webdriver
chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com")
time.sleep(2)


#cautam "Shifting Content"

chrome.find_element(By.LINK_TEXT, 'Shifting Content').click()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Example 3: List").click()
time.sleep(2)
# chrome.back()
# chrome.back()
chrome.execute_script("window.history.go(-2)")
time.sleep(2)


chrome.find_element(By.LINK_TEXT, "Checkboxes").click()
time.sleep(2)

input_list = chrome.find_element(By.TAG_NAME, "input")
input_list[1].click()
time.sleep(2)

input_list[0].click()
time.sleep(2)

chrome.back()

chrome.find_element(By.LINK_TEXT, 'Inputs').click()
time.sleep(2)

chrome.find_element(By.LINK_TEXT, 'input').send_keys(2222)
time.sleep(2)
