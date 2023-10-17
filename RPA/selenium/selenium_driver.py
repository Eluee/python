from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
print(chrome_options)

chrome_driver = ChromeDriverManager().install()
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.get("https://www.daum.net")

keyword = '시청률'

driver.find_element(By.XPATH, '//*[@id="q"]').send_keys(keyword)
D



