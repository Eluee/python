from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.daum.net")


keyword = '시청률'

driver.find_element(By.XPATH, '//*[@id="q"]').send_keys(keyword)

driver.find_element(By.XPATH, '//*[@id="jupTvRatingColl"]/div/div/button[2]').click()
time.sleep(1)



