from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import pywhatkit
import pyjokes

chrome_driver_path = r"C:\Users\ADMIN\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

chrome_options = Options()
chrome_options.binary_location = brave_path

chrome_service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://web.whatsapp.com")

time.sleep(20)

search_box = driver.find_element("xpath", "//div[@contenteditable='true'][@data-tab='3']")
search_box.click()
time.sleep(2)

search_box.send_keys("AASH")
search_box.send_keys(Keys.ENTER)
time.sleep(2)

message = driver.find_elements("xpath", "//div[contains(@class, 'message-in') or contains(@class, 'message-out')]")[-1].find_element("xpath", ".//span[contains(@class, 'selectable-text')]").text

print(message)
if message == 'joke':
    pywhatkit.sendwhatmsg_to_group_instantly('B5DwS0EUxR52wi2F8aqGXf', pyjokes.get_joke(), wait_time=7)