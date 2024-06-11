import requests
import numpy as np
import pandas as pd
import pprint
import configparser
from pathlib import Path
import os
from dotenv import load_dotenv
import json

# .envファイルの内容を読み込む
load_dotenv()
APP_ID_env = os.environ["APP_ID"]
APP_ID=APP_ID_env
print(APP_ID)

#リクエストURL指定
url="https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch"

#検索キーワード
keyword="アシックス　DSライト"

#変数定義
i=0
detail_list=[]

#パラメーター指定
params={
    'appid':APP_ID,
    'query':keyword,
    'start':1,
    'results':10
}

#json取得
r=requests.get(url,params)
r_json=r.json()

#for文で商品詳細取得、辞書型格納、リスト格納
for i in range(len(r_json["hits"])):
    name=r_json["hits"][i]["name"]
    url=r_json["hits"][i]["url"]
    price=r_json["hits"][i]["price"]
    shop_name=r_json["hits"][i]["seller"]["name"]
    rate=r_json["hits"][i]["review"]["rate"]
    i=i+1

    d_detail={'商品名':name,'URL':url,'価格':price,'店名':shop_name,'評価':rate}
    detail_list.append(d_detail)

#データフレームに変換、エクセル出力
df=pd.DataFrame(detail_list)
df.to_excel(f"yahoo_shopping_deta_{keyword}.xlsx")
