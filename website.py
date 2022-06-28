from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create the webdriver object. Here the 
# chromedriver is present in the driver 
# folder of the root directory.
driver = webdriver.Chrome("chromedriver")


# get https://pnrtscr.com/n7umrk/
driver.get("https://pnrtscr.com/n7umrk")

# Maximize the window and let code stall 
# for 10s to properly maximise the window.
driver.maximize_window()
time.sleep(2)

# Obtain button by link text and click.
button = driver.find_element(By.ID,'accept-button')
button.click()
