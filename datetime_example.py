'''
using date time module/class
'''
import datetime as dt

# today's date
current_date = dt.date.today()
print(current_date)

# make specific date
date1 = dt.date(2021, 3, 15)
print(date1)
# printing Year, Month and day of specific date variable
print('Year: ', date1.year)
print('Month: ', date1.month)
print('Day: ', date1.day)

# making specific time variable
time1 = dt.time(10, 45, 30, 45667)
print(time1)
# printing Hour, Minutes, Seconds and Microseconds from time variable
print('Hour: ', time1.hour)
print('Minutes: ', time1.minute)
print('Seconds: ', time1.second)
print('Microseconds: ', time1.microsecond)

# creating date time object containg both date and time
datetime_obj = dt.datetime(2021, 11, 28, 23, 55, 39)
print(datetime_obj)
# date part of datime object
print(datetime_obj.date())
# time part of datetime object
print(datetime_obj.time())

# current date and time
current_datetime = dt.datetime.now()
print(current_datetime)

# checking difference between two dates
new_year = dt.datetime(2022, 1, 1)
time_remaining = new_year - current_datetime
print(time_remaining)

# converting specific date in specific format using strftime function
string_date = current_datetime.strftime("%A, %B %d, %Y")
print(string_date)

# converting a date string to date object
date_string = "21 June, 2021"
date_obj = dt.datetime.strptime(date_string, "%d %B, %Y")
print(date_obj)

'''
different formats

%a	Abbreviated weekday name.	Sun, Mon, ...
%A	Full weekday name.	Sunday, Monday, ...
%w	Weekday as a decimal number.	0, 1, ..., 6
%d	Day of the month as a zero-padded decimal.	01, 02, ..., 31
%-d	Day of the month as a decimal number.	1, 2, ..., 30
%b	Abbreviated month name.	Jan, Feb, ..., Dec
%B	Full month name.	January, February, ...
%m	Month as a zero-padded decimal number.	01, 02, ..., 12
%-m	Month as a decimal number.	1, 2, ..., 12
%y	Year without century as a zero-padded decimal number.	00, 01, ..., 99
%-y	Year without century as a decimal number.	0, 1, ..., 99
%Y	Year with century as a decimal number.	2013, 2019 etc.
%H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
%-H	Hour (24-hour clock) as a decimal number.	0, 1, ..., 23
%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12
%-I	Hour (12-hour clock) as a decimal number.	1, 2, ... 12
%p	Locale’s AM or PM.	AM, PM
%M	Minute as a zero-padded decimal number.	00, 01, ..., 59
%-M	Minute as a decimal number.	0, 1, ..., 59
%S	Second as a zero-padded decimal number.	00, 01, ..., 59
%-S	Second as a decimal number.	0, 1, ..., 59
%f	Microsecond as a decimal number, zero-padded on the left.	000000 - 999999
%z	UTC offset in the form +HHMM or -HHMM.
%Z	Time zone name.
%j	Day of the year as a zero-padded decimal number.	001, 002, ..., 366
%-j	Day of the year as a decimal number.	1, 2, ..., 366
%U	Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, ..., 53
%W	Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, ..., 53
%c	Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013
%x	Locale’s appropriate date representation.	09/30/13
%X	Locale’s appropriate time representation.	07:06:05
%%	A literal '%' character.	%

'''
