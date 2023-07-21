# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mojito
import pandas as pd
import datetime
if __name__ == '__main__':

    key = "PSeYtwokolD9ulsRdIXGKsFQ7F1zb2zwewhG"
    secret = "mlkOdZW/KB59fv3mWVzbd43cLext/pHT+XWDP6m1146/MJzudQOQ2oT4B5fKPSX4p5H3eKIWmTkbGoCSRA3PBNuL6Hu/uvkT9LvjJG/Da7fNQG+HRrH6tzxDtfZydK9l6i7CEMc+P551QiCxs1s5a9a26uvFYL5RwUbcfi9lW41s6nyCO0g="
    acc_no = "69210341-01"

    broker = mojito.KoreaInvestment(
        api_key=key,
        api_secret=secret,
        acc_no=acc_no,
        mock = False
    )
    print(broker)
    price = broker.fetch_price("005930")
    df = pd.DataFrame(price)
    df_price = df['output']
    print(f'{datetime.datetime.now()} price : {df_price["stck_prpr"]}')
