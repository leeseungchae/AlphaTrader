# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mojito
import pandas as pd
import datetime
from my_settings import key, secret, acc_no


if __name__ == '__main__':

    key = key
    secret = secret
    acc_no = acc_no

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
