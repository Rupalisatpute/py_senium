from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("http://demo.guru99.com/test/newtours/")

# link_Home = driver.find_element(By.LINK_TEXT,"Home")
# td_Home = driver.find_element(By.XPATH,"/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")
#
# actions = ActionChains(driver)
# actions.move_to_element(link_Home).perform()
#
# Combining actions
# actions.move_to_element(link_Home)
# actions.click(td_Home)
# actions.perform()

driver.get("https://www.facebook.com")
actions = ActionChains(driver)
txtUsername = driver.find_element(By.ID,"email")

# actions.move_to_element(txtUsername).click(txtUsername).key_down(Keys.SHIFT, txtUsername).send_keys("hello").key_up(Keys.SHIFT, txtUsername).double_click(txtUsername).context_click(txtUsername).perform()

actions.move_to_element(txtUsername)
actions.click(txtUsername)
actions.key_down(Keys.SHIFT, txtUsername)
actions.send_keys("hello")
actions.key_up(Keys.SHIFT, txtUsername)
actions.double_click(txtUsername)
actions.context_click(txtUsername)
actions.perform()

driver.quit()