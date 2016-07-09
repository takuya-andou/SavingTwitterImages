#概要
TwitterStreamingApiから画像付きのツイートを保存します

##保存する内容
-ユーザー名  
-ツイート  
-画像URL  

#必要なもの
mongodb(pymongo)
flask
twitter

#使いかた
##1.TwitterAPIの設定
`config-sample.ini`にあるTwitterAPIの四つの値を変更して`config.ini`として保存

##2.収集開始
`python main.py`

##3.保存された画像の確認
`python display.py`
で最新10件を表示するflaskサーバーが立ち上がります。(ポートは8080)
