#Changed to show git commit and push
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")

driver.get("http://demo.guru99.com/popup.php")

driver.maximize_window()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://demo.guru99.com/test/delete_customer.php")

driver.find_element(By.NAME,"cusid").send_keys("53920")

driver.find_element(By.NAME,"submit").submit()

alert = driver.switch_to.alert

alert_message = alert.text

print("ALERT TEXT = ", alert_message)

alert.accept()

driver.quit()