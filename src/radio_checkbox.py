from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://demo.guru99.com/test/radio.html")
radio1 = driver.find_element(By.ID,"vfb-7-1")
#radio1 = driver.find_element(By.XPATH, "//input[@value='Option 1']")
radio2 = driver.find_element(By.ID,"vfb-7-2")

time.sleep(3)

# Select first radio button
radio1.click()

time.sleep(3)

# Select second radio button
radio2.click()

time.sleep(3)

# Select check box
option1 = driver.find_element(By.ID,"vfb-6-0")
option1.click()

time.sleep(3)

# Check whether the check box is toggled on
if option1.is_selected():
    print("Checkbox is toggled on")
else:
    print("Checkbox is toggled off")
time.sleep(3)

driver.get("http://demo.guru99.com/test/facebook.html")
time.sleep(3)

chkFBPersist = driver.find_element(By.ID,"persist_box")

time.sleep(3)

for _ in range(2):
    chkFBPersist.click()
    # time.sleep(3)

    print("Facebook Persists Checkbox Status is -  ",
          chkFBPersist.is_selected())

driver.close()
driver.quit()