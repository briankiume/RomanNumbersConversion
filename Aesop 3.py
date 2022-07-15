import numpy as np
import re


def roman(text):
    # Reference Dictionary
    ref = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ref_2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    # Splitting to obtain separate strings for comparison with each reference
    listy = re.split(r'(IV)|(IX)|(XL)|(XC)|(CD)|(CM)', text)
    for x in listy:
        if x == '':
            listy.remove(x)
    listy_2 = list(filter(None, listy))
    listy_3 = [x for x in listy_2 if (x == 'IV') | (x == 'IX') | (x == 'XL') |
               (x == 'XC') | (x == 'CD') | (x == 'CM')]
    list_compa1 = [x for x in listy_2 if x not in listy_3]
    list_compa2 = listy_3

    # Reference 1 comparison
    numbers = []
    for x in list_compa1:
        for char in x:
            for key in ref:
                if char == key:
                    numbers.append(ref[key])

    # Reference 2 comparison
    numbers_2 = []
    for x in list_compa2:
        for key in ref_2:
            if x == key:
                numbers_2.append(ref_2[key])

    # Summation
    all_numbers = numbers + numbers_2
    summed = np.sum(np.array(all_numbers))
    return summed


brian_tests = {
    'III': roman('III'),
    'LVIII': roman('LVIII'),
    'MDCCCXXIV': roman('MDCCCXXIV'),
    'MDCCCXXXC': roman('MDCCCXXXC'),
    'MMCCLXIV': roman('MMCCLXIV'),
    'MMMCCCXLIV': roman('MMMCCCXLIV'),
    'MMMCCLX': roman('MMMCCLX'),
    'MMMCCXC': roman('MMMCCXC'),
    'MMMVIII': roman('MMMVIII'),
    'MMMCDXVIII': roman('MMMCDXVIII'),
    'MMMDCCXLVI': roman('MMMDCCXLVI'),
    'MMMDCXIX': roman('MMMDCXIX'),
    'MDCCCXX': roman('MDCCCXX')
}

print(brian_tests)
