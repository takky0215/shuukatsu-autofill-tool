import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import time

form_url = ""

def autofill_form(data):
    global form_url
    if not form_url:
        messagebox.showerror("URL未設定", "フォームのURLが入力されていません")
        return

    service = Service('C:/Users/takky/Downloads/edgedriver_win64/msedgedriver.exe')
    driver = webdriver.Edge(service=service)
    wait = WebDriverWait(driver, 10)

    driver.get(form_url)
    wait.until(EC.element_to_be_clickable((By.ID, 'first_access'))).click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_w160b'))).click()

    def safe_send(name, value):
        elem = driver.find_elements(By.NAME, name)
        if elem and value:
            elem[0].send_keys(value)

    def click_dropdown(index, text):
        dropdowns = driver.find_elements(By.CLASS_NAME, 'jqTransformSelectOpen')
        if index >= len(dropdowns):
            return
        dropdowns[index].click()
        time.sleep(0.5)
        options = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//ul[@id="getlist" and not(contains(@style,"none"))]/li/a')))
        for option in options:
            if option.text.strip() == text:
                driver.execute_script("arguments[0].scrollIntoView(true);", option)
                time.sleep(0.2)
                option.click()
                break

    safe_send('kname1', data['姓（漢字）'])
    safe_send('kname2', data['名（漢字）'])
    safe_send('yname1', data['姓（カナ）'])
    safe_send('yname2', data['名（カナ）'])

    click_dropdown(0, data['生年'])
    click_dropdown(1, data['生月'])
    click_dropdown(2, data['生日'])

    radios = driver.find_elements(By.CLASS_NAME, 'jqTransformRadio')
    if data['性別'] == 'male' and len(radios) >= 1:
        radios[0].click()
    elif data['性別'] == 'female' and len(radios) >= 2:
        radios[1].click()

    safe_send('gyubin1', data['郵便番号（前半）'])
    safe_send('gyubin2', data['郵便番号（後半）'])
    click_dropdown(3, data['都道府県'])
    safe_send('gadrs1', data['住所1'])
    safe_send('gadrs2', data['住所2'])
    safe_send('gtel1', data['電話番号1'])
    safe_send('gtel2', data['電話番号2'])
    safe_send('gtel3', data['電話番号3'])

    checkboxes = driver.find_elements(By.CLASS_NAME, 'jqTransformCheckbox')
    if data['休暇先と同一（True/False）'].lower() == 'true' and checkboxes:
        checkboxes[0].click()
    else:
        safe_send('kyubin1', data['休暇先 郵便番号（前半）'])
        safe_send('kyubin2', data['休暇先 郵便番号（後半）'])
        click_dropdown(4, data['休暇先 都道府県'])
        safe_send('kadrs1', data['休暇先 住所1'])
        safe_send('kadrs2', data['休暇先 住所2'])
        safe_send('ktel1', data['休暇先 電話番号1'])
        safe_send('ktel2', data['休暇先 電話番号2'])
        safe_send('ktel3', data['休暇先 電話番号3'])

    safe_send('bikoa', data['ゼミ名'])
    safe_send('bikob', data['クラブ・サークル名'])
    click_dropdown(5, data['卒業年'])
    click_dropdown(6, data['卒業月'])

    safe_send('account1', data['メールアカウント'])
    safe_send('domain1', data['メールドメイン'])
    safe_send('account2', data['メールアカウント'])
    safe_send('domain2', data['メールドメイン'])
    safe_send('account3', data['携帯メールアカウント'])
    safe_send('domain3', data['携帯メールドメイン'])
    safe_send('account4', data['携帯メールアカウント'])
    safe_send('domain4', data['携帯メールドメイン'])

    input("Enterでブラウザを閉じます")

def open_url_input():
    url_window = tk.Toplevel(root)
    url_window.title("自動入力URLの設定")

    tk.Label(url_window, text="フォームURLを入力してください：").pack(padx=10, pady=5)
    url_entry = tk.Entry(url_window, width=60)
    url_entry.pack(padx=10, pady=5)

    def set_url_and_start():
        global form_url
        form_url = url_entry.get()
        url_window.destroy()
        autofill_form(saved_data)

    tk.Button(url_window, text="開始", command=set_url_and_start).pack(pady=10)

def confirm():
    global saved_data
    saved_data = {label: entry.get() for label, entry in zip(labels, entries)}

    with open("userdata.json", "w", encoding="utf-8") as f:
        json.dump(saved_data, f, ensure_ascii=False, indent=2)

    messagebox.showinfo("保存完了", "入力情報を保存しました。次に自動入力先のURLを指定してください。")
    open_url_input()

root = tk.Tk()
root.title("就活フォーム入力")
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

labels = [
    "姓（漢字）", "名（漢字）", "姓（カナ）", "名（カナ）", "生年", "生月", "生日", "性別",
    "郵便番号（前半）", "郵便番号（後半）", "都道府県", "住所1", "住所2",
    "電話番号1", "電話番号2", "電話番号3", "休暇先と同一（True/False）",
    "休暇先 郵便番号（前半）", "休暇先 郵便番号（後半）", "休暇先 都道府県",
    "休暇先 住所1", "休暇先 住所2", "休暇先 電話番号1", "休暇先 電話番号2", "休暇先 電話番号3",
    "ゼミ名", "クラブ・サークル名", "卒業年", "卒業月",
    "メールアカウント", "メールドメイン", "携帯メールアカウント", "携帯メールドメイン"
]

entries = []
for i, label in enumerate(labels):
    tk.Label(scrollable_frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=3)
    entry = tk.Entry(scrollable_frame, width=30)
    entry.grid(row=i, column=1, padx=5, pady=3)
    entries.append(entry)

# 前回の入力を復元
if os.path.exists("userdata.json"):
    with open("userdata.json", "r", encoding="utf-8") as f:
        loaded = json.load(f)
    for i, label in enumerate(labels):
        entries[i].insert(0, loaded.get(label, ""))

tk.Button(scrollable_frame, text="確定", command=confirm).grid(row=len(labels), column=0, columnspan=2, pady=10)
root.mainloop()
