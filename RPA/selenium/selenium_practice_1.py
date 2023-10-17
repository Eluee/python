from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
service = Service(ChromeDriverManager().install())
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service= service, options=options)
driver.get("https://www.daum.net")

keyword = '시청률'

driver.find_element(By.XPATH, '//*[@id="q"]').send_keys(keyword)

driver.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]').click()
day_text = driver.find_element(By.XPATH, '//*[@id="jupTvRatingColl"]/div[2]/div[1]/div[3]/div/table/tbody' ).text
time.sleep(0.3)

driver.find_element(By.XPATH, '//*[@id="jupTvRatingColl"]/div[2]/div[1]/div[1]/ul/li[2]').click()
week_text = driver.find_element(By.XPATH, '//*[@id="jupTvRatingColl"]/div[2]/div[1]/div[3]/div/table/tbody' ).text
time.sleep(0.3)

driver.find_element(By.XPATH, '//*[@id="jupTvRatingColl"]/div[2]/div[1]/div[1]/ul/li[3]').click()
month_text = driver.find_element(By.XPATH, '//*[@id="jupTvRatingColl"]/div[2]/div[1]/div[3]/div/table/tbody' ).text


def recompose_string(recomposable_string):
    composed_list = [i.split() for i in recomposable_string.split('\n')]
    composed_list = [composed_list[i] + composed_list[i+1] for i in range(0, len(composed_list), 2)]
    composed_list = [[composed_list[i][0], ' '.join(composed_list[i][1:-2]), composed_list[i][-2], composed_list[i][-1]]for i in range(len(composed_list))]
    return composed_list


day_list = recompose_string(day_text)
week_list = recompose_string(week_text)
month_list = recompose_string(month_text)

# 문자열 까지 가공 끝난 상태 여기서 이제 pandas로 작업하면 끝


time.sleep(1)



