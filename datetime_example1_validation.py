'''
validating whether given date is in proper formats
'''

from datetime import datetime as dt

def validate(date_text):
    try:
        date = dt.strptime(date_text, '%Y-%m-%d')
        print("Date is in correct format")
        print("Date is:",date)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


validate('2003-Dec-23')
#validate('2003-12-32')
