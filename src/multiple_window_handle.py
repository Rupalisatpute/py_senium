from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")

driver.get("http://demo.guru99.com/popup.php")

driver.maximize_window()

driver.find_element(By.XPATH,"//*[contains(@href,'popup.php')]").click()

windows = driver.window_handles

for window in windows:
    time.sleep(2)
    driver.switch_to.window(window)
    time.sleep(2)
    try:
        driver.find_element(By.NAME, "emailid").send_keys("kapil@gmail.com")
        time.sleep(2)
        driver.find_element(By.NAME, "btnLogin").click()
        time.sleep(2)
    except Exception:
        pass
    time.sleep(2)
    driver.close()


driver.quit()