import pywinmacro as pw
import time


location1 = (185, 64)   # 주소창
location2 = (245, 125)  # 검색창
location3 = (334, 555)  # Historical Data
location4 = (641, 739)  # Download


# 조회 대상 종목의 티커 코드를 기록한 리스트
stocks = ["FB", "MSFT", "APPL", "TSLA", "AMZN"]


# 역대 주가 정보 다운 함수
def price(ticker):
    # 검색창 클릭
    pw.click(location2)
    time.sleep(3)
    # 티커코드 입력
    pw.type_in(ticker)
    time.sleep(3)
    # enter
    pw.key_press_once("enter")
    time.sleep(3)
    # Historical Data 클릭
    pw.click(location3)
    time.sleep(3)
    # Download 클릭
    pw.click(location4)
    time.sleep(3)


# stocks 리스트에 저장된 종목들의 주가 조회
def get_price_data(stocks):
    # 반복문
    for stock in stocks:
        # 개별 종목 주가 조회
        price(stock)
        time.sleep(3)


# YAHOO FINANCE 접속 함수
def go_to_yfinance():
    # 주소창 클릭
    pw.click(location1)
    time.sleep(1)
    # 주소 입력
    pw.type_in("https://finance.yahoo.com")
    time.sleep(1)
    # enter
    pw.key_press_once("enter")


# YAHOO FINANCE 접속
go_to_yfinance()


# 주가들을 검색
get_price_data(stocks)