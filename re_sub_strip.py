import re

str_regex = re.compile(r'[\d\w]{1,}')

def str_strip(str1, *str2):


    #remove str2[0] in str1
    if len(str2) <= 0:
        return ''.join(str_regex.findall(str1))    #return str1 and value str2-0
    else:

        if ''.join(str2[0])in str1:
            str2_regex = re.compile(f'[^{str2[0]}]')
            strip_str = ''.join(str2_regex.findall(str1))
            return str_strip(strip_str, *str2[1:])

        else:
            return str_strip(str1, *str2[1,])

print(str_strip('   jaime  '))
