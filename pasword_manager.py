#! python3
# password_manager.py - not secure password holder

import pyperclip
import re
import sys

PASSWORDS = {'email': 'JIkahiNHHYjalohHGghbrzwQERUAoV',
             'blog': 'hiJGYBhfGdZZAWpobnwUGbyVAV',
             'suitcase': '2241'}


if len(sys.argv) < 2:
    print('Usage: python password_manager [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There\'s no account named ' + account)

