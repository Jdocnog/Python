##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random
import pandas
import smtplib

now = dt.datetime.now()
day = now.day
month = now.month
name = "Jordan"
text_to_remove = "[NAME]"
my_email = "jburkitt2296@gmail.com"
password= "cenvwgfvjdhqyrvl"

birthday_data = pandas.read_csv("birthdays.csv")

list_of_letters = {
    '1': "letter_templates/letter_1.txt",
    '2': "letter_templates/letter_2.txt",
    '3': "letter_templates/letter_3.txt"
}

random_num = random.randint(1, 3)

if month in birthday_data["month"].values:
    if day in birthday_data["day"].values:
        with open(list_of_letters[str(random_num)]) as letter:
            letter_text = letter.read()
            change_text = letter_text
            change_text = change_text.replace(text_to_remove, name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="jburkitt2296@gmail.com",
                msg=f"Subject:Happy Birthday\n\n{change_text}\n"
            )