import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import pyautogui

# Define the URL you want to open, by default, it is set for the live stream of ICC WTC Final India vs Australia 2023
# url = "https://www.example.com/"
url = "https://www.hotstar.com/in/movies/ms-dhoni-the-untold-story/1000162617/watch?filters=content_type%3Dmovie"
# url = "https://www.hotstar.com/in/sports/cricket/icc-world-test-championship-2023/988/final-australia-vs-india-day-4/1540023554/m-708280/live/watch?filters=content_type%3Dsport_live"

chrome_options = Options()

# Use chrome by default, or Change path to use your own web browser. 
chrome_options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Set the path to the ChromeDriver. Make sure to add correct driver path if the web browser is not chromium based.
chrome_path = 'C:\\Users\\teera\\OneDrive\\Desktop\\Hotstar_Loophole\\chromedriver_win32\\chromedriver.exe'

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
        pyautogui.press('f')
        if check_volume_off(driver):
            pyautogui.press('m')

        # Relaunch after 't' seconds, here, 5 minutes.
        t = 300
        time.sleep(t)

        if is_browser_closed(driver):
            break
        
    except Exception as e:
        print("An error occurred:", str(e))
        break