from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

print("Starting...")

chrome_options = Options()
chrome_options.add_argument("--headless")

with open("stories.txt") as file:
    for item in file:
        try:
            item.replace("\n","")
            url = item.split(" ")[0]
            slides = int(item.split(" ")[1])
            driver = webdriver.Edge()
            driver.get(url)
            driver.set_window_size(720, 650)
            time.sleep(8*slides+5)
            driver.refresh()
            driver.quit()
        except:
            continue

print("Finished")
