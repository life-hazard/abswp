"""
    REGEX
"""
import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo = phone_num_regex.search('My number is 333-234-572')
gr = mo.group()
print('Phone number found: ' + gr)

hero_regex = re.compile('Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = hero_regex.search('Tina Fey and Batman')
print(mo2.group())

