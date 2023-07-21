# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mojito
import requests
import json
import datetime
import pandas as pd


if __name__ == '__main__':

    key = "PSeYtwokolD9ulsRdIXGKsFQ7F1zb2zwewhG"
    secret = "mlkOdZW/KB59fv3mWVzbd43cLext/pHT+XWDP6m1146/MJzudQOQ2oT4B5fKPSX4p5H3eKIWmTkbGoCSRA3PBNuL6Hu/uvkT9LvjJG/Da7fNQG+HRrH6tzxDtfZydK9l6i7CEMc+P551QiCxs1s5a9a26uvFYL5RwUbcfi9lW41s6nyCO0g="
    acc_no = "69210341-01"

    APP_KEY = key
    APP_SECRET = secret
    ACCESS_TOKEN = ''
    URL_BASE = "https://openapi.koreainvestment.com:9443"  # 실전투자


    # Auth
    def auth():
        headers = {"content-type": "application/json"}
        body = {
            "grant_type": "client_credentials",
            "appkey": APP_KEY,
            "appsecret": APP_SECRET
        }
        PATH = "oauth2/tokenP"
        URL = f"{URL_BASE}/{PATH}"
        res = requests.post(URL, headers=headers, data=json.dumps(body))

        global ACCESS_TOKEN
        ACCESS_TOKEN = res.json()["access_token"]


    # 주식현재가 시세
    def get_current_price(stock_no):
        PATH = "uapi/domestic-stock/v1/quotations/inquire-price"
        URL = f"{URL_BASE}/{PATH}"

        # 헤더 설정
        headers = {"Content-Type": "application/json",
                   "authorization": f"Bearer {ACCESS_TOKEN}",
                   "appKey": APP_KEY,
                   "appSecret": APP_SECRET,
                   "tr_id": "FHKST01010100"}

        params = {
            "fid_cond_mrkt_div_code": "J",
            "fid_input_iscd": stock_no
        }

        # 호출
        res = requests.get(URL, headers=headers, params=params)
        print(res.status_code)
        if res.status_code == 200 and res.json()["rt_cd"] == "0":
            return (res.json())
        # 토큰 만료 시
        elif res.status_code == 200 and res.json()["msg_cd"] == "EGW00123":
            auth()
            get_current_price(stock_no)
        else:
            print("Error Code : " + str(res.status_code) + " | " + res.text)
            return None


    auth()
    price = get_current_price("005930")
    df = pd.DataFrame(price)
    df_price = df['output']
    print(f'{datetime.datetime.now()} price : {df_price["stck_prpr"]}')