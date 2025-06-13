""" Motivational quotes """
import smtplib
import datetime as dt
import random
import os

# Get current folder path
current_dir = os.path.dirname(__file__)

MY_EMAIL = input("Enter your email address: ")
PASSWORD = input("Enter your password: ")
QUOTE_FILE = os.path.join(current_dir, "quotes.txt")

with open(QUOTE_FILE, "r", encoding="utf-8") as file:
    quotes = file.readlines()
    QUOTE = random.choice(quotes)

today = dt.datetime.now()
day_of_week = today.weekday()
if day_of_week == 2:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="shanwratten@gmail.com",
            msg=f"Subject:Wednesday Motivational Quote\n\n{QUOTE}"
            )
