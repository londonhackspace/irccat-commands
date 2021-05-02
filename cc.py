#!/usr/bin/python3

"""
gencc: A simple program to generate credit card numbers that pass the MOD 10 check
(Luhn formula).
Usefull for testing e-commerce sites during development.

Copyright 2003 Graham King

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

import random
from random import Random
import sys
import copy

visaPrefixList = [  ['4', '5', '3', '9'], 
                    ['4', '5', '5', '6'], 
                    ['4', '9', '1', '6'],
                    ['4', '5', '3', '2'], 
                    ['4', '9', '2', '9'],
                    ['4', '0', '2', '4', '0', '0', '7', '1'],
                    ['4', '4', '8', '6'],
                    ['4', '7', '1', '6'],
                    ['4'] ]

mastercardPrefixList = [    ['5', '1'],
                            ['5', '2'],
                            ['5', '3'],
                            ['5', '4'],
                            ['5', '5'] ]

amexPrefixList = [  ['3', '4'],
                    ['3', '7'] ]
                    

"""
'prefix' is the start of the CC number as a string, any number of digits.
'length' is the length of the CC number to generate. Typically 13 or 16
"""
def completed_number(prefix, length):

    ccnumber = prefix

    # generate digits

    while len(ccnumber) < (length - 1):
        digit = generator.choice(['0',  '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        ccnumber.append(digit)


    # Calculate sum 

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int( reversedCCnumber[pos] ) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):

            sum += int( reversedCCnumber[pos+1] )

        pos += 2

    # Calculate check digit

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append( str(checkdigit) )
    
    return ''.join(ccnumber)

def credit_card_number(generator, prefixList, length):

    ccnumber = copy.copy( generator.choice(prefixList) )
    return completed_number(ccnumber, length)


generator = Random()
generator.seed()

try:
    type = sys.argv[5]
except IndexError:
    type = random.choice(['mastercard', 'visa', 'amex'])

cvv_length = 3

if (type == 'mastercard'):
    prefix = mastercardPrefixList
elif (type == 'visa'):
    prefix = visaPrefixList
elif (type == 'amex'):
    prefix = amexPrefixList
    cvv_length = 4
else:
    type = 'mastercard'
    prefix = mastercardPrefixList

ccv = []
for i in range(cvv_length):
    ccv.append(generator.choice(['0',  '1', '2', '3', '4', '5', '6', '7', '8', '9']))

number = credit_card_number(generator, prefix, 16)
print ("%s: %s, ccv: %s" % (type, number, ''.join(ccv)))
        
