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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_tel = set()              # O(1)

for entry in texts:             # O(n)
    unique_tel.add(entry[0])    # +O(1)
    unique_tel.add(entry[1])    # +O(1)
#=> For loop O() = O(n)

for entry in calls:             # O(n)
    unique_tel.add(entry[0])    # +O(1)
    unique_tel.add(entry[1])    # +O(1)
#=> For loop O() = O(n)

print(f"There are {len(unique_tel)} different telephone numbers in the records.")   # O(1)

#RunTime analysis ~= O(2 + 2n) => O(n)
