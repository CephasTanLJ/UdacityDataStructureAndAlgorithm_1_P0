"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# Helper
def is_telemarketer(number: str) -> bool:       # O(1)
    return number[:3] == '140'

# Main
telemarketer_numbers = list()                   # O(1)

for entry in calls:                             # O(n)
    '''Create list of incoming calls phone numbers who are telemarkters (start with 140).'''
    if is_telemarketer(entry[0]):               # *O(1)
        telemarketer_numbers.append(entry[0])   # *O(1)
#=> Function O() = O(n)

telemarketer_numbers.sort()                     # O(n.log(n))
telemarketer_numbers = sorted(set(telemarketer_numbers))    # O(n.log(n))

def test():
    # assert is_telemarketer(calls[1779][0]) == True, "Telemarketer not detected"
    # assert is_telemarketer(calls[1778][0]) == False, "non-Telemarketer detected"
    # assert all(map(is_telemarketer, telemarketer_numbers)), "There's non-Telemarketer in telemarketer_list"
    # print('Test okay.')

    print(f'These numbers could be telemarketers:')         # O(1)
    for number in telemarketer_numbers:                     # O(n)
        print(number)                                       # *O(1)
    #=> for loop O() = O(n)
test()

#RunTime Analysis ~ O(1) + O(n) + 2 * O(n.log(n)) + O(1) + O(n) =>     O(n + n.log(n))