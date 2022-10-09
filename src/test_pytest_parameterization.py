import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


test_data = [["user1", "pass1"],
             ["user2", "pass2"],
             ["user3", "pass3"],
             ["user4", "pass4"],
             ["user5", "pass5"],
             ["user6", "pass6"],
             ]


@pytest.mark.parametrize("username, password", test_data)
def test_login(username, password):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(2)
    driver.quit()

