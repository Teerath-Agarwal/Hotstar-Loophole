import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui

# Define the URL you want to open
url = "https://www.hotstar.com/in/movies/chhichhore/1260012713/watch?filters=content_type%3Dmovie"

# Configure Chrome options to open a private window
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Set the path to the ChromeDriver executable
chrome_path = 'C:\\Users\\teera\\OneDrive\\Desktop\\chrm_ext\\chromedriver_win32\\chromedriver.exe'


def check_volume_off(driver):
    # Find the <i> elements with the specified class
    # elements = driver.find_elements_by_css_selector('i.icon-volume-off-line')
    elements = driver.find_elements(By.CSS_SELECTOR, 'i.icon-volume-off-line')
    # Return True if any matching element is found, otherwise False
    return len(elements) > 0

# Loop indefinitely
while True:
    try:
        # Launch the web browser with the specified URL
        driver = webdriver.Chrome(service=Service(chrome_path), options=chrome_options)
        driver.get(url)
        
        # Simulate pressing the F key using pyautogui
        pyautogui.press('f')

        # Check if the stream is mute by default
        is_volume_off = check_volume_off(driver)
        print(is_volume_off)
        if check_volume_off(driver):
            pyautogui.press('m')

        t = 10
        # Sleep for t seconds
        time.sleep(t)

        
    except Exception as e:
        print("An error occurred:", str(e))
        break


# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys

# # Define the URL you want to open
# url = "https://www.hotstar.com/in/movies/chhichhore/1260012713/watch?filters=content_type%3Dmovie"
# # url = "https://www.hotstar.com/in/home?ref=%2Fin"
# # url = "https://www.hotstar.com/in/sports/cricket/icc-world-test-championship-2023/988/final-australia-vs-india-day-4/1540023554/m-708280/live/watch?filters=content_type%3Dsport_live"
# # url = "https://fast.com"

# # Configure Chrome options to open a private window
# chrome_options = Options()
# # brave_options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
# chrome_options.add_argument("--incognito")

# # Set the path to the BraveDriver executable
# chrome_path = 'C:\\Users\\teera\\OneDrive\\Desktop\\chrm_ext\\chromedriver_win32\\chromedriver.exe'

# # Loop indefinitely
# while True:
#     try:
#         # Launch the web browser with the specified URL
#         # driver = webdriver.Chrome(service=Service(brave_path), options=brave_options)
#         driver = webdriver.Chrome(service=Service(chrome_path), options=chrome_options)
#         driver.get(url)

#         # driver.find_element_by_tag_name('body').send_keys(Keys.F)
#         # body_element = driver.find_element_by_tag_name('body')
#         # body_element.send_keys(Keys.F)
#         body_element = driver.find_element_by_tag_name('body')
#         actions = ActionChains(driver)
#         actions.move_to_element(body_element).send_keys(Keys.F).perform()

    
#         t = 20
#         # Sleep for t seconds
#         time.sleep(t)
        
#         # Terminate the web browser
#         # driver.quit()
        
#         # Exit the loop
#         # break
    
#     except Exception as e:
#         # Handle any exceptions that occur
#         print("An error occurred:", str(e))
#         # Optionally, you can choose to retry or exit the loop on error
#         break