"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from datetime import datetime   # O(1)
current_longest_time = 0        # O(1)
longest_call = None             # O(1)

for entry in calls:                                                                 # O(n)
    if float(entry[3]) > current_longest_time:                                  # +O(1)
        longest_call = entry                                                    # +O(1)
    #=> For Loop O() = O(n)

print(f"{longest_call[0]} spent the longest time, {int(longest_call[3])} seconds, on the phone during September 2016.") # O(1)

#RunTime analysis ~ O(n + 4) => O(n)
