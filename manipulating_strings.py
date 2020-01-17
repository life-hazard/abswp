"""
    dictionary - reminder
"""
import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}


def display_inventory(inventory):
    total_items = 0

    print('Inventory: ')
    for k in inventory:
        print(inventory[k], k)
        total_items += inventory[k]

    print('Total items: ', total_items)


def add_to_inventory(inventory, add_items):
    for i in add_items:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)


"""
    MANIPULATING STRINGS
"""

def string_methods():
    word = 'Hello world!'
    print(word.isupper())
    print(word.islower())
    print(word.upper().isupper())
    print(word.lower())
    print(word.upper())

    print('Hello'.isalpha())
    print('Hello123'.isalpha())
    print('Hello123'.isalnum())
    print('123'.isalnum())
    print('Helo'.isalnum())
    print('123'.isdecimal())
    print(' '.isspace())
    print('H e l l o'.isspace())
    print('This Is Title Case'.istitle())
    print('this is not Title Case'.istitle())
    print('This Is NOT Title Case'.istitle())
    print(word)
    print(word.startswith('He'))
    print(word.endswith('ld!'))

    nou = ['cats', 'bats', 'rats']
    print(', '.join(nou))
    print('\t'.join(nou))
    print('OoOoO'.join(nou))

    print('And now I\'m saying goodbye!'.split())
    print('And now I\'m saying goodbye!'.split('y'))
    print('And1now1I\'m1saying1goodbye!'.split('1'))


def print_picnic(items_dict, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))


picnic_items = {'sandwitches': 4, 'apples': 12, 'cups': 4, 'cookies': 300}
print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)


import pyperclip

#pyperclip.copy('Hello World!')
#copy = pyperclip.paste()

#print(copy)
print(pyperclip.paste())