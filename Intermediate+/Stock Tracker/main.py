import os
import smtplib
import requests
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")
ALPHA_API = os.environ.get("ALPHA_VANTAGE_API")
NEWS_API = os.environ.get("NEWS_API_KEY")
STOCK_CHANGE = 1


def format_msg(dif, news):
    """ Create message content """
    news_list = []
    for t, d in news.items():
        news_list.append(f"Headline: {t}\nBrief: {d}\n")
    if dif > 0:
        stock = f"🔺 {round(dif)}%"
        return f"TSLA: {stock}\n\n" + "\n".join(news_list)
    else:
        stock = f"🔻 {abs(round(dif))}%"
        return f"TSLA: {stock}\n\n" + "\n".join(news_list)


# Parameters for Alphavantage API
alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API
    }

today = dt.datetime.now()
DATE = today.date() - dt.timedelta(days=30)

# Parameters for News API
news_parameters = {"q": COMPANY_NAME,
                   "from": DATE,
                   "sortBy": "publishedAt",
                   "language": "en",
                   "apiKey": NEWS_API
                   }

try:
    response = requests.get(
        "https://www.alphavantage.co/query",
        params=alpha_parameters,
        timeout=10
        )
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("Timed out")

alpha_data = response.json()
lst_two_ents = list(alpha_data['Time Series (Daily)'])[0: 2]
alpha_day_before = float(
    alpha_data['Time Series (Daily)'][lst_two_ents[1]]['4. close']
    )
alpha_yest = float(
    alpha_data['Time Series (Daily)'][lst_two_ents[0]]['4. close']
    )

# Check the difference between the two most recent close values
alpha_difference = (
    ((alpha_yest - alpha_day_before)/alpha_yest)*100
    )

# If the difference is greater than a set amount get news
if alpha_difference > STOCK_CHANGE or alpha_difference < STOCK_CHANGE:
    try:
        tesla_news = requests.get(
            "https://newsapi.org/v2/everything",
            params=news_parameters,
            timeout=10
            )
    except requests.exceptions.Timeout:
        print("Timed out")

    news_data = tesla_news.json()
    articles = sorted(
        news_data["articles"], key=lambda x: x["publishedAt"], reverse=True
        )
    last_three_reports = {
        a["title"]: a["description"]
        for a in articles[:3]
        }
    # Send email with the change in stock values and news articles
    EMAIL_BODY = format_msg(alpha_difference, last_three_reports)
    MSG = f"Subject: Tesla Stocks Alert 📉\n\n{EMAIL_BODY}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=MSG.encode('utf-8')
            )
