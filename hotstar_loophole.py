import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

url = "https://www.hotstar.com/in/movies/ms-dhoni-the-untold-story/1000162617/watch?filters=content_type%3Dmovie"
t = 300

datf = 'data'
add_path = os.path.join(datf, 'url.txt')
tm_path = os.path.join(datf, 'tm.txt')

if os.path.exists(add_path):
    with open(add_path, "r") as file:
        url = file.read()

if os.path.exists(tm_path):
    with open(tm_path, "r") as file:
        t = int(file.read())

change = input("Do you want to change the address or looptime? (Y/N): ")

if change.lower() == "y" or change.lower() == "yes":
    new_t = int(input("Enter the new value of looptime (Enter 0 to use previous value): "))
    if new_t:
        t = new_t
        with open(tm_path, "w") as file:
            file.write(str(t))
    new_url = input("Enter the new address (URL) (Enter # to use previous value): ")
    if len(new_url) > 1:
        url = new_url
        with open(add_path, "w") as file:
            file.write(str(url))

chrome_options = Options()

# Use chrome by default, or Change path to use your own web browser.
# chrome_options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Set the path to the ChromeDriver. Make sure to add correct driver path if the web browser is not chromium based.
chrome_path = '.\\chromedriver_win32\\chromedriver.exe'

def is_browser_closed(driver):
    try:
        driver.title
        return False
    except WebDriverException:
        return True

def check_volume_off(driver):
    elements = driver.find_elements(By.CSS_SELECTOR, 'i.icon-volume-off-line')
    return len(elements) > 0

while True:
    try:
        driver = webdriver.Chrome(service=Service(chrome_path), options=chrome_options)
        driver.get(url)
        driver.find_element(By.TAG_NAME,'body').send_keys('F')
        time.sleep(1)
        
        if check_volume_off(driver):
            driver.find_element(By.TAG_NAME,'body').send_keys('M')

        time.sleep(t)
        if is_browser_closed(driver):
            break
        
    except Exception as e:
        print("An error occurred:", str(e))
        break