from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import datetime

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10) 
#webをロードする
driver.get('http://0810.atat.jp/i/f.php')

#8時まで待つ
now = datetime.datetime.now()
today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
while now < today8am:
    now = datetime.datetime.now()
    print(now)

#診察ボタンクリック
element0 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/a[3]")))
driver.execute_script('arguments[0].click()', element0)

#予約ボタンクリック
element1 = wait.until(EC.presence_of_element_located((By.ID, "aTRN")))
element1.click()

#入力
element2 = wait.until(EC.presence_of_element_located((By.NAME, "HOSID")))
element2.send_keys("19485")
element3 = driver.find_element_by_name("b_date")
element3.send_keys("1012")
element4 = driver.find_element_by_xpath("/html/body/form/input[17]")
element4.click()

#決定する
element5 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/a[1]")))
element5.click()
element6 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/input[24]")))
element6.click()

#終了
driver.quit()
 