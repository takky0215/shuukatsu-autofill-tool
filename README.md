# 自動入力ツール (Shuukatsu Autofill Tool)

このツールは、i-web などの就職活動フォームに自動で情報を入力する Python スクリプトです。  
Microsoft Edge ブラウザを対象としています。  
同じ情報を何度も入力する手間を省けます。  

## 使用前の準備

### 必須環境

Python 3.9 以上

Microsoft Edge ブラウザ

Selenium ライブラリ

EdgeDriver

### ライブラリインストール

pip install selenium

### EdgeDriver の設定

EdgeDriver をダウンロード  
"https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH"

msedgedriver.exe を解凍

ファイルパスをコード内の service = Service(...) に設定

## 使用手順

### 1. コードのダウンロード

GitHub ページで

「Code」→「Download ZIP」か

または Git を使う:

git clone https://github.com/takky0215/shuukatsu-autofill-tool.git

### 2. autofill.py の編集

スクリプトの先頭部分に、以下の情報を入力してください：

sei_kanji = '山田'  
mei_kanji = '太郎'  
sei_kana = 'ヤマダ'  
mei_kana = 'タロウ'  
birth_year = '2001'  
...  
email_account = 'yamada'  
email_domain = 'example.com'  
...  
formurl = 'https ://mypage/○○...'  
(情報を入力したいサイトのＵＲＬを入力)  

### 3. 実行

ターミナルや VSCode のターミナルで、ファイルのあるフォルダまで cd し、以下を実行:

python autofill.py

Microsoft Edge が立ち上がり、フォームに情報が自動入力されます。

### 4. 手動確認

最後に表示されたフォームの入力内容を確認し、送信ボタンは必ず自分で押してください。

## 注意

EdgeDriver のパスや URL は環境によって変わるので要確認

フォームがアップデートされると動かなくなることがあります

GitHub に公開する場合、個人情報を含めないよう注意


#### 作者: takky0215
