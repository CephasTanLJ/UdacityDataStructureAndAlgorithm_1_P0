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
call_time = dict()  # O(1)

for entry in calls:                                 # O(n)
    phone_numbers = [entry[0], entry[1]]            # *O(1)
    for phones in phone_numbers:                    # *O(2)
        if phones not in call_time:                 # *O(1)
            call_time[phones] = float(entry[3])     # +O(1)
        else:
            call_time[phones] += float(entry[3])

longest_call_num = max(call_time, key=call_time.get)    # O(n) - assuming it checks every element

#Test
# def test():
#     assert call_time[
#                '78130 00821'] == 26368.0, f"Not correct calculations {call_time['78130 00821']} instead of 26368.0"
#
#     sorted_dictionary = dict(sorted(call_time.items(), key=lambda item: item[1]))
#     assert longest_call_num == sorted_dictionary.popitem()[0], f"longest_call_num {longest_call_num} is not correct"
#
# test()

print(f"{longest_call_num} spent the longest time, {call_time[longest_call_num]} seconds, on the phone during September 2016.")  # O(1)

# RunTime analysis ~ O(n)
