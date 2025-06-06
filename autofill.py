from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# -----------------------------
# 入力値
# -----------------------------
form_url = 'https://mypage.3030.i-webs.jp/mec2027/applicant/entry/index/entrycd/'
（）
sei_kanji = '山田'
mei_kanji = '太郎'
sei_kana = 'ヤマダ'
mei_kana = 'タロウ'

birth_year = '2002'
birth_month = '04'
birth_day = '15'
gender = 'male'

zipcode1 = '111'
zipcode2 = '0000'
address1 = '千代田区丸の内1-1-1'
address2 = '日本マンション101'
current_pref = '東京都'
#○○都/道/府/県まで記入

tel1 = '03'
tel2 = '1111'
tel3 = '1111'

same_as_current_address = False
vacation_zip1 = '222'
vacation_zip2 = '0000'
vacation_addr1 = '港区芝公園2-2-2'
vacation_addr2 = '別荘ハウス302'
vacation_pref = '青森県'
vacation_tel1 = '080'
vacation_tel2 = '0123'
vacation_tel3 = '5678'

seminar_name = '国際経済学ゼミ'
circle_name = 'テニスサークル'
grad_year = '2027'
grad_month = '03'

#
#@の前と後で分離
email_account = 'yamada'
email_domain = 'example.com'

mobile_account = 'yamada.mobile'
mobile_domain = 'example.jp'




# -----------------------------
# ヘルパー
# -----------------------------
def click_dropdown_option_from(index, text):
dropdowns = driver.find_elements(By.CLASS_NAME, 'jqTransformSelectOpen')
if index >= len(dropdowns):
return
dropdowns[index].click()
time.sleep(0.5)

options = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//ul[@id="getlist" and not(contains(@style,"none"))]/li/a'))
)

for option in options:
    if option.text.strip() == text:
        driver.execute_script("arguments[0].scrollIntoView(true);", option)
        time.sleep(0.2)
        option.click()
        break

def safe_send(by, value, text):
elements = driver.find_elements(by, value)
if elements and text:
elements[0].send_keys(text)

def safe_click(by, value, index=0):
elements = driver.find_elements(by, value)
if len(elements) > index:
elements[index].click()



# -----------------------------
# Selenium設定
# -----------------------------
service = Service('C:/yourpath.../msedgedriver.exe')
driver = webdriver.Edge(service=service)
wait = WebDriverWait(driver, 10)

# -----------------------------
# 画面遷移
# -----------------------------
driver.get(form_url)
wait.until(EC.element_to_be_clickable((By.ID, 'first_access'))).click()
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_w160b'))).click()

# -----------------------------
# 入力
# -----------------------------
safe_send(By.NAME, 'kname1', sei_kanji)
safe_send(By.NAME, 'kname2', mei_kanji)
safe_send(By.NAME, 'yname1', sei_kana)
safe_send(By.NAME, 'yname2', mei_kana)

click_dropdown_option_from(0, birth_year)
click_dropdown_option_from(1, birth_month)
click_dropdown_option_from(2, birth_day)

radios = driver.find_elements(By.CLASS_NAME, 'jqTransformRadio')
if gender == 'male' and len(radios) >= 1:
radios[0].click()
elif gender == 'female' and len(radios) >= 2:
radios[1].click()

safe_send(By.NAME, 'gyubin1', zipcode1)
safe_send(By.NAME, 'gyubin2', zipcode2)
click_dropdown_option_from(3, current_pref)
safe_send(By.NAME, 'gadrs1', address1)
safe_send(By.NAME, 'gadrs2', address2)
safe_send(By.NAME, 'gtel1', tel1)
safe_send(By.NAME, 'gtel2', tel2)
safe_send(By.NAME, 'gtel3', tel3)

checkboxes = driver.find_elements(By.CLASS_NAME, 'jqTransformCheckbox')
if same_as_current_address and checkboxes:
checkboxes[0].click()
else:
safe_send(By.NAME, 'kyubin1', vacation_zip1)
safe_send(By.NAME, 'kyubin2', vacation_zip2)
click_dropdown_option_from(4, vacation_pref)
safe_send(By.NAME, 'kadrs1', vacation_addr1)
safe_send(By.NAME, 'kadrs2', vacation_addr2)
safe_send(By.NAME, 'ktel1', vacation_tel1)
safe_send(By.NAME, 'ktel2', vacation_tel2)
safe_send(By.NAME, 'ktel3', vacation_tel3)

safe_send(By.NAME, 'bikoa', seminar_name)
safe_send(By.NAME, 'bikob', circle_name)
click_dropdown_option_from(5, grad_year)
click_dropdown_option_from(6, grad_month)

safe_send(By.NAME, 'account1', email_account)
safe_send(By.NAME, 'domain1', email_domain)
safe_send(By.NAME, 'account2', email_account)
safe_send(By.NAME, 'domain2', email_domain)

safe_send(By.NAME, 'account3', mobile_account)
safe_send(By.NAME, 'domain3', mobile_domain)
safe_send(By.NAME, 'account4', mobile_account)
safe_send(By.NAME, 'domain4', mobile_domain)

input("Enterキーで終了します")
driver.find_element(By.NAME, 'domain3').send_keys(mobile_domain)
driver.find_element(By.NAME, 'account4').send_keys(mobile_account)
driver.find_element(By.NAME, 'domain4').send_keys(mobile_domain)

input("Enterキーで終了します")
