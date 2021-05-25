"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# PART A

num_recieved_bangalore_set = set()      # O(1)
num_recieved_bangalore_list = list()    # O(1)
# codes_recieved_bangelore_set = set()
bangalore_to_bangalore = 0              # O(1)

##Helper functions:
def get_codes(number: str) -> str:
    '''
    Returns the area code of a phone number,
    if no area code,
        :return None
    '''
    ind = number.find(')') + 1      # O(1)
    code = number[:ind]             # O(1)
    if code != "":                  # O(1)
        return code                 # O(1)
    else:
        return None
#=> Function O() = O(1)

## main
for entry in calls:                                     # O(n)
    '''Append people who recieved calls from a bangalore telephone number into num_received_bangalore list.'''
    if get_codes(entry[0]) == '(080)':                  # +O(1)
        num_recieved_bangalore_list.append(entry[1])    # +O(1)
        if get_codes(entry[1]) == '(080)':              # +O(1)
            bangalore_to_bangalore += 1                 # +O(1)
#=> For loop O() = O(n)

num_recieved_bangalore_list.sort()                                      # O(n log(n))
num_recieved_bangalore_set = sorted(set(num_recieved_bangalore_list))   # O(n log(n))

## Just in case I misinterpreted part A
## Uncertain if I need to print all telephone numbers or just unique fixed line codes
# codes_recieved_bangelore_set = set(map(get_codes, num_recieved_bangalore_list))
# codes_recieved_bangelore_set.remove(None)

#Part B
total_calls_from_bangalore = len(num_recieved_bangalore_list)                                   # O(1)
percentage_bangalore_to_bangalore = bangalore_to_bangalore / total_calls_from_bangalore * 100   # O(n^2) * O(n^2) according to https://stackoverflow.com/questions/44020182/time-complexity-of-operation-python/44020262


def test():
    '''Testing codes.'''
    # assert get_codes(calls[6][0]) == '(080)', "Not correct area_code"
    # assert get_codes(calls[31][0]) == None, "Not correct area_code"
    #
    # print('\n\n')
    # print(f'Part A:')
    print(f'The numbers called by people in Bangalore have codes:' )    # O(1)
    for number in num_recieved_bangalore_set:                           # O(n)
        print(number)                                                   # +O(1)
    #=>For loop O() = O(n)
    #
    # print('No problem in A')
    #
    # assert total_calls_from_bangalore == 1080, "Not correct total number of calls from bangalore!"
    # assert bangalore_to_bangalore <= total_calls_from_bangalore, "Number of B to B calls cannot be more than total number of calls from Bangelore!"
    #
    # print('\n\n')
    # print(f'Part B:')
    print(f'{percentage_bangalore_to_bangalore:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.' )  # O(1)
    # print('No problem in B')

test()

#RunTime analysis ~= O(n) + 2 * O(n log(n)) + O(1) + 2 * O(n^2) + O(1) + O(n) + O(1) => O(n^2 + n + n.log(n))