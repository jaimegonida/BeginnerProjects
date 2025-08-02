#Date detection

import re

#Create Regex for date.
dateRegex = re.compile(r'''(
        ([0-2]\d|3[0-1])                  #month
        (\-|\/|\.|\s|\,)                  #separator
        (0\d|1[0-2])                      #month
        (\-|\/|\.|\s|\,)                  #separator
        ([1-2](\d{3}))                    #year
        )''', re.VERBOSE)


#Create a function for extracting dates in data.
def date_extract(data_input):
    date_out = dateRegex.search(data_input).group()
    return date_validation(date_out)



#Create a function to detect correct days for each month of leap years.
def date_validation(date_to_validate):
    separators = ['-', '/', '.', ',', ' ']
    date_only_30 = ['02', '04', '06', '09', '11']

    #Define the separator. I'm stubborn so i refuse to use re.split()
    #I use this only because i can.
    for sep in separators:
        if sep in date_to_validate:
            parts = date_to_validate.split(sep)
            separator = sep
            if len(parts) == 3:
                date, month, year = parts


    #Create a validation for correct days for each month of leap years.
    #Checks for month without 31.
    if month in date_only_30:
        if int(date) > 30:
            return 'Date is invalid!'

    #Checks for February leap years.
    is_leap = int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0)
    if int(date) > (29 if is_leap else 28):
        return 'Date is invalid!'

    valid_date = [date, month, year]
    return separator.join(valid_date)

print(date_extract('My birthday is on 31-11-2023'))
