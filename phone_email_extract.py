#!python3
#phone_email_extact.py - Finds phone numbers (ph) and email address
#on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{2, 3}|\(\+?\d{2,3}\)|\+?\d{2}|0?)   #area_code
    (\s|-|\.)?                          #separator
    (\d{3})?                             #first 3 digits
    (\s|-|\.)?                           #separator
    (\d{3})                             #2nd 3 digits
    (\s|-|\.)?                           #separator
    (\d{4})                             #last 4 digits
    )''', re.VERBOSE)


#E-mail regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   #username
    @                                      #@symbol
    [a-zA-Z0-9.-]+                      #domain
    (\.[a-zA-Z]{2,4})                   #top-level domain
    )''', re.VERBOSE)

#Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5], groups[7]])
    if groups[7] != '':
        phoneNum += 'x' + groups[7]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard.


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
