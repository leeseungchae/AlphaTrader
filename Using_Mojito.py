# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mojito
import pandas as pd
import datetime
from my_settings import key, secret, acc_no
import datetime

current_date = datetime.datetime.now()
start_date = "20200101"


def call_api(key: str, secret: str, acc_no: str) -> pd.DataFrame:

    broker = mojito.KoreaInvestment(
        api_key=key,
        api_secret=secret,
        acc_no=acc_no,
        mock=False
    )
    print(broker)
    price = broker.fetch_price("005930")
    df = pd.DataFrame(price)
    df_price = df['output']
    print(f'{datetime.datetime.now()} price : {df_price["stck_prpr"]}')

    Raw_Data = broker.fetch_ohlcv_domestic(symbol="005930", start_day=start_date, end_day=today)
    df_day = pd.DataFrame(Raw_Data['output2'])
    # df_day['stck_bsop_date'] = pd.to_datetime(df_day['stck_bsop_date'], format='%Y%m%d')
    # df_day.set_index('stck_bsop_date', inplace=True)
    # last_date = df_day['stck_bsop_date'].tail(1).values[0]
    # print(last_date)
    df = pd.DataFrame(Raw_Data['output1'], index=['0'])
    return df_day


if __name__ == '__main__':
    key = key
    secret = secret
    acc_no = acc_no

    # 원하는 날짜 범위 설정
    desired_start_date = pd.to_datetime('2023-01-01')
    desired_end_date = pd.to_datetime('2023-12-31')

    # 데이터를 저장할 빈 DataFrame 생성
    result_df = pd.DataFrame()

    # API를 호출하여 원하는 날짜까지 데이터를 가져오기
    current_date = desired_start_date
    while current_date <= desired_end_date:

        data = call_api(current_date, end_date)

        # 가져온 데이터를 result_df에 추가
        result_df = pd.concat([result_df, data])

        # 다음 API 요청을 위해 current_date 업데이트
        current_date = end_date + pd.Timedelta(days=1)

    # 인덱스를 '날짜' 열로 설정
    result_df.set_index('날짜', inplace=True)
    today = current_date.strftime("%Y%m%d")
