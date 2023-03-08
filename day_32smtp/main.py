import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day_of_week = now.weekday()
my_email = ""
password= ""

if day_of_week == 0:
    with open("quotes.txt") as q_list:
        quotes = q_list.readlines()#creates a list of all motivational quotes
        random_quote = random.choice(quotes)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="",
                msg=f"Subject:Motivational Quote\n\n{random_quote}\n."
            )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.weekday()
# print(day)
#
#
# date_of_birth = dt.datetime(year=1996, month=2, day=22)
# print(date_of_birth)

