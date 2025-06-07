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
以下のコマンドを実行して、Selenium をインストールします：  
pip install selenium

### EdgeDriver の設定

#### 1. EdgeDriver をダウンロード  
EdgeDriverダウンロードページからお使いの Edge のバージョンに対応したドライバをダウンロード  
URL : https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH

#### 2.msedgedriver.exe を解凍  

#### 3. autofill.py 内の your_path = '...' に、msedgedriver.exe のパスを指定します



## 使用手順

### 1. コードのダウンロード

以下のいずれかの方法でコードを取得します：  
GitHub ページで
「Code」→「Download ZIP」

または Git を使う:  
git clone https://github.com/takky0215/shuukatsu-autofill-tool.git

### 2. autofill.py の編集

スクリプトの先頭部分に、以下の情報を入力してください：

your_path = 'C:/Users/yourname/Downloads/msedgedriver.exe'  # msedgedriver.exe のパスを入力
form_url = 'https://mypage.XXXX.i-webs.jp/YYYY/applicant/entry/index/entrycd/'  # 入力対象のフォームURL（企業ごとに異なります）

sei_kanji = '山田'  
mei_kanji = '太郎'  
sei_kana = 'ヤマダ'  
mei_kana = 'タロウ'  
birth_year = '2001'  
...  
email_account = 'yamada'  
email_domain = 'example.com'  


### 3. 実行

ターミナルまたは VSCode のターミナルで、スクリプトがあるフォルダに移動し、以下のコマンドを実行：  

python autofill.py

Microsoft Edge が自動で起動し、情報がフォームに入力されます。  

### 4. 手動確認

自動入力が完了したら、入力された情報を必ず確認し、「送信」ボタンは手動で押してください。  



## 注意

EdgeDriver のパスや URL は環境ごとに異なるため、必ず確認・修正してください  
フォームの仕様変更（HTML構造の変更）があると、正しく動作しない可能性があります  


#### 作者: takky0215
