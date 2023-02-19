import requests
import os
from twilio.rest import Client

STOCK_NAME = "IBM"
COMPANY_NAME = "IBM"
account_sid = 'ACfe31166cf23c89f3cc55d6af4d24ee63'
auth_token = '64eeaa31b27ee9e3439e2796470afd38'
client = Client(account_sid, auth_token)

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

Stock_API = 'S7KC6JGL14FTFFUV'
stocks_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
    'outputsize': 'compact',
    'apikey': Stock_API
}
News_API = '043f0661c3fd4ff88420b259e0567301'
News_params = {
    'q': COMPANY_NAME,
    'from': '2023-02-01',
    'to': '2023-02-03',
    'sortBy': 'popularity',
    'language': 'en',
    'apiKey': News_API
}


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def market_change():
    """
    let's assume we invested billion and even > 0.1% impacts us
    :return:
    """
    response = requests.get(url=STOCK_ENDPOINT, params=stocks_params).json()
    daily_data = response['Time Series (Daily)']
    yesterdays_closing = float(daily_data['2023-02-02']['4. close'])
    todays_closing = float(daily_data['2023-02-03']['4. close'])
    percentage = ((todays_closing - yesterdays_closing) / yesterdays_closing) * 100
    return percentage


def get_news():
    response = requests.get(url=NEWS_ENDPOINT, params=News_params).json()
    articles = response['articles']
    news_dict = {}
    try:
        for num in range(3):
            news_dict[articles[num]['title']] = articles[num]['description']
    except IndexError as e:
        pass
    return news_dict


def send_message(news):
    msg = ''
    keys = [key for key in news]
    for key in keys:
        msg += f'Headline: {key} \n Brief: {news[key]} \n'

    message = client.messages \
        .create(
        body=msg,
        from_='+16507191660',
        to='+918840981096'
    )
    print(message.status)


if __name__ == '__main__':
    if abs(market_change()) > 0.1:
        send_message(get_news())


