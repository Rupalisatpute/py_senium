import time
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


browser="chrome"
if browser.lower()=="chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
else:

   driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))



driver.get("http://www.seleniumframework.com/demo-sites/")

print("Page Title = ", driver.title)
print("Current URL = ", driver.current_url)
print("Page Source = ", driver.page_source)




driver.quit()


