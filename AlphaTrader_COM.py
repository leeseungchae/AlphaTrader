import mojito
import pandas as pd
import datetime
from my_settings import key, secret, acc_no
import datetime

class Alpha_COM:
    def __init__(self, key: str, secret: str, acc_no: str):
        """
        클래스의 생성자입니다.

        :param key: api의 key
        :type key: str
        :param secret: api의 비밀번호
        :type secret: str
        :param acc_no: api의 계좌변호
        :type acc_no: str
        """
        self.key = key
        self.secret = secret
        self.acc_no = acc_no

    def call_api(self, start_date: str, end_date: str, ticker_symbol: str) -> pd.DataFrame:
        """
        메서드의 설명을 추가하세요.

        :param start_date: 조회 시작일
        :type start_date: str
        :param end_date: 죄회 종료일
        :type end_date: str
        :param ticker_symbol: 조회 티커
        :type ticker_symbol: str
        :return: 반환값에 대한 설명을 추가하세요.
        :rtype: 반환값의 타입을 추가하세요.
        """

        broker = mojito.KoreaInvestment(
            api_key=self.key,
            api_secret=self.secret,
            acc_no=self.acc_no,
            mock=False
        )

        price = broker.fetch_price(ticker_symbol)
        df = pd.DataFrame(price)
        df_price = df['output']
        print(f'{datetime.datetime.now()} price : {df_price["stck_prpr"]}')

        Raw_Data = broker.fetch_ohlcv_domestic(symbol=ticker_symbol, start_day=start_date, end_day=end_date)
        df_day = pd.DataFrame(Raw_Data['output2'])
        # df_day['stck_bsop_date'] = pd.to_datetime(df_day['stck_bsop_date'], format='%Y%m%d')
        # df_day.set_index('stck_bsop_date', inplace=True)
        # last_date = df_day['stck_bsop_date'].tail(1).values[0]
        # print(last_date)
        df = pd.DataFrame(Raw_Data['output1'], index=['0'])
        return df_day
