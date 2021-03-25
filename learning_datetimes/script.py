# Name:     learning_datetimes/script.py
# Author:   Phillip Douglas

# Importing the 'datetime' module
from datetime import datetime

# Creating a date using year, month, day as arguments
birthday = datetime(1986, 2, 4, 3, 53)
print(f"Birth Date:\t{birthday}") # print birthday
print(f"Birth Year:\t{birthday.year}") # print birthday year
print(f"Birth Month:\t{birthday.month}") # print birthday month
print(f"Birth Day:\t{birthday.day}") # print birthday day
print(f"Birth Week Day:\t{birthday.weekday()}") # print birthday time
print()

# Creating a date using datetime.now()
now = datetime.now()
print(f"Now: {now}")
print()

# Parsing a date using strptime
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print(f"Parsed Date:\t{parsed_date}")
print(f"Parsed Month:\t{parsed_date.month}")
print(f"Parsed Day:\t{parsed_date.day}")
print(f"Parsed Year:\t{parsed_date.year}")
print()

# Rendering a date as a string using strftime
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(f"Date String: {date_string}")