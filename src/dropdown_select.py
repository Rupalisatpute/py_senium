
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("http://demo.guru99.com/test/newtours/register.php")
#
# drpCountry = Select(driver.find_element(By.NAME,"country"))
# time.sleep(2)
# drpCountry.select_by_visible_text("ANTARCTICA")
# time.sleep(2)
# drpCountry.select_by_index(4)
# time.sleep(2)
# Selecting Items in a multiple select elements

driver.get("http://jsbin.com/osebed/2")

fruits = Select(driver.find_element(By.ID,"fruits"))
time.sleep(2)

assert fruits.is_multiple
time.sleep(2)
fruits.select_by_visible_text("Banana")
time.sleep(2)
fruits.deselect_by_visible_text("Banana")
time.sleep(2)
fruits.deselect_by_visible_text("Apple")
time.sleep(2)
fruits.select_by_index(2)
time.sleep(2)
driver.quit()

