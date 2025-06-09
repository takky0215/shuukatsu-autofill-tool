# 自動入力ツール (Shuukatsu Autofill Tool)

このツールは、i-web などの就職活動フォームに自動で情報を入力する Python スクリプトです。  
Microsoft Edge ブラウザを対象としています。  
同じ情報を何度も入力する手間を省けます。  
（大学名等の入力は現在開発中です）

---

## 🔧 使用前の準備

### 必須環境
- Python 3.9 以上
- Microsoft Edge ブラウザ
- Selenium ライブラリ
- EdgeDriver

### ライブラリインストール

pip install selenium

---

### EdgeDriver の設定

1. EdgeDriver ダウンロードページ  
   お使いの Edge のバージョンに対応したドライバをダウンロード  
   URL: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH

2. msedgedriver.exe を解凍

3. autofill.py または autofill_re.py 内の以下の変数を編集：

your_path = 'C:/Users/yourname/Downloads/msedgedriver.exe'

---

## 📝 使用手順

### ① コードのダウンロード

GitHub ページで「Code」→「Download ZIP」または：

git clone https://github.com/takky0215/shuukatsu-autofill-tool.git

---

### ② autofill.py（初期バージョン）の使い方

#### 記入内容をスクリプト上で直接入力して実行

スクリプトの先頭に以下を記入：

form_url = 'https://mypage.XXXX.i-webs.jp/YYYY/applicant/entry/index/entrycd/'
sei_kanji = '山田'
mei_kanji = '太郎'
...

#### 実行コマンド：

python autofill.py

Microsoft Edge が自動で起動し、情報がフォームに入力されます。  
入力後は「送信」ボタンを手動で押してください。

---

## 🆕 Version 2：GUI入力＆情報保存付きバージョン（autofill_re.py）

### 📌 特徴

- GUIフォームから視覚的に情報を入力できる（Tkinter使用）
- スクロール対応で長いフォームにも対応
- 入力情報は自動で userdata.json に保存
- 次回起動時に前回の入力情報を自動復元
- 確定ボタン後に「URL入力画面」→ フォームに自動入力
- 休暇先住所が同一かどうかで分岐入力も自動処理

---

### ✅ 実行方法

1. 必要ライブラリのインストール（上記と同じ）

2. autofill_re.py を実行：

python autofill_re.py

3. 起動後の流れ：

- フォームに情報を入力  
- 「確定」ボタンを押す  
- 次に現れる画面で「i-webフォームのURL」を入力  
- 自動的にEdgeが起動し、自動入力を実行  

---

## 💾 入力データの保存について

- 入力情報は userdata.json に保存されます（自動生成）
- 次回起動時に自動でフォームに反映されます
- プライバシー保護のため、Gitへコミットする際は .gitignore に追加することを推奨：

echo userdata.json >> .gitignore

---

## 📁 ファイル構成

📁 shuukatsu-autofill-tool/  
├── autofill.py         # 旧バージョン（手動で記入）  
├── autofill_re.py      # 新バージョン（GUI＋自動保存つき）  
├── userdata.json       # 入力内容を保存（自動生成）  
└── README.md  

---

## ⚠️ 注意事項

- EdgeDriver のパスや URL は環境ごとに異なるため、必ずご自身で確認・修正してください
- フォームの構造が変化した場合、スクリプトが正しく動作しない可能性があります
- 大学名や学部情報などの自動入力は現在開発中です

---

## 👤 作者

https://github.com/takky0215
```
