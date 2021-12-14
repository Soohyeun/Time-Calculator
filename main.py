import time_calculator as tc

while True:
    pytest = input('Input \'pytest\' to run: ')

    if pytest == 'pytest':
        break

tc.add_time("3:00 PM", "3:10")
print('\n')
tc.add_time("11:30 AM", "2:32", "Monday")
print('\n')
tc.add_time("11:43 AM", "00:20")
print('\n')
tc.add_time("10:10 PM", "3:30")
print('\n')
tc.add_time("11:43 PM", "24:20", "tueSday")
print('\n')
tc.add_time("6:30 PM", "205:12")
