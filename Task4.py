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

out_call_num = set()                        # O(1)
non_telemarkerter_num = set()               # O(1)

for entry in calls:                         # O(n)
    out_call_num.add(entry[0])              # +O(1)
    non_telemarkerter_num.add(entry[1])     # +O(1)

for entry in texts:                         # O(n)
    non_telemarkerter_num.add(entry[0])     # +O(1)
    non_telemarkerter_num.add(entry[1])     # +O(1)

possible_telemarketer = out_call_num - non_telemarkerter_num    # O(n)
possible_telemarketer = sorted(possible_telemarketer)           # O(nlog(n))

# Test
# def test():
#     assert possible_telemarketer.issubset(out_call_num), "Contains numbers not in out_call_num"
#     assert possible_telemarketer.isdisjoint(non_telemarkerter_num), "Contains non_telemarketer_num"
#     print('test done')
# #
# test()

print(f'These numbers could be telemarketers:')         # O(1)
for number in possible_telemarketer:                     # O(n)
    print(number)                                       # *O(1)
#RunTime Analysis ~ 3 * O(n) + O(nlog(n)) =>     O(3n + n.log(n))