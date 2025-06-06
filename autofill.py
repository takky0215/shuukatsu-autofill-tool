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
sei_kanji = '山田'
mei_kanji = '太郎'
sei_kana = 'ヤマダ'
mei_kana = 'タロウ'

birth_year = '2001'
birth_month = '03'
birth_day = '15'
gender = 'male'

zipcode1 = '111'
zipcode2 = '0000'
address1 = '千代田区丸の内1-1-1'
address2 = '日本マンション101'
current_pref = '東京都'

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

email_account = 'yamada'
email_domain = 'example.com'
mobile_account = 'yamada.mobile'
mobile_domain = 'example.jp'




# -----------------------------
# ヘルパー
# -----------------------------
def click_dropdown_option_from(index, text):
    dropdowns = driver.find_elements(By.CLASS_NAME, 'jqTransformSelectOpen')
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

def click_dropdown_by_xpath(dropdown_xpath, text):
    driver.find_element(By.XPATH, dropdown_xpath).click()
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
driver.find_element(By.NAME, 'kname1').send_keys(sei_kanji)
driver.find_element(By.NAME, 'kname2').send_keys(mei_kanji)
driver.find_element(By.NAME, 'yname1').send_keys(sei_kana)
driver.find_element(By.NAME, 'yname2').send_keys(mei_kana)

click_dropdown_option_from(0, birth_year)
click_dropdown_option_from(1, birth_month)
click_dropdown_option_from(2, birth_day)

if gender == 'male':
    driver.find_elements(By.CLASS_NAME, 'jqTransformRadio')[0].click()
else:
    driver.find_elements(By.CLASS_NAME, 'jqTransformRadio')[1].click()

driver.find_element(By.NAME, 'gyubin1').send_keys(zipcode1)
driver.find_element(By.NAME, 'gyubin2').send_keys(zipcode2)
click_dropdown_option_from(3, current_pref)
driver.find_element(By.NAME, 'gadrs1').send_keys(address1)
driver.find_element(By.NAME, 'gadrs2').send_keys(address2)
driver.find_element(By.NAME, 'gtel1').send_keys(tel1)
driver.find_element(By.NAME, 'gtel2').send_keys(tel2)
driver.find_element(By.NAME, 'gtel3').send_keys(tel3)

if same_as_current_address:
    driver.find_element(By.CLASS_NAME, 'jqTransformCheckbox').click()
else:
    driver.find_element(By.NAME, 'kyubin1').send_keys(vacation_zip1)
    driver.find_element(By.NAME, 'kyubin2').send_keys(vacation_zip2)
    click_dropdown_option_from(4, vacation_pref)
    driver.find_element(By.NAME, 'kadrs1').send_keys(vacation_addr1)
    driver.find_element(By.NAME, 'kadrs2').send_keys(vacation_addr2)
    driver.find_element(By.NAME, 'ktel1').send_keys(vacation_tel1)
    driver.find_element(By.NAME, 'ktel2').send_keys(vacation_tel2)
    driver.find_element(By.NAME, 'ktel3').send_keys(vacation_tel3)

driver.find_element(By.NAME, 'bikoa').send_keys(seminar_name)
driver.find_element(By.NAME, 'bikob').send_keys(circle_name)
click_dropdown_option_from(5, grad_year)  # 年
click_dropdown_option_from(6, grad_month)  # 月

# E-mailアドレス
driver.find_element(By.NAME, 'account1').send_keys(email_account)
driver.find_element(By.NAME, 'domain1').send_keys(email_domain)
driver.find_element(By.NAME, 'account2').send_keys(email_account)
driver.find_element(By.NAME, 'domain2').send_keys(email_domain)

# 携帯アドレス
driver.find_element(By.NAME, 'account3').send_keys(mobile_account)
driver.find_element(By.NAME, 'domain3').send_keys(mobile_domain)
driver.find_element(By.NAME, 'account4').send_keys(mobile_account)
driver.find_element(By.NAME, 'domain4').send_keys(mobile_domain)

input("Enterキーで終了します")
