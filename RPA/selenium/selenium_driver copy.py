from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
service = Service(ChromeDriverManager().install())
options.add_experimental_option("detach", True)
print(options)

driver = webdriver.Chrome(service= service, options=options)
driver.get("https://www.daum.net")

keyword = '시청률'

driver.find_element(By.XPATH, '//*[@id="q"]').send_keys(keyword)

driver.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]').click()

time.sleep(1)



