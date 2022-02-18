"""
Loop through the numbers from 1 to 70 and print each number, except
for the numbers by seven print "BEEP"
See the FizzBuzz problem on the homework
"""

# Range can take a first argument that specifies the starting value
# of the range
#
# range(1, 71) loops through the numbers starting at 1 and going up
# to but not including 71, i.e. the range 1 to 70, inclusive

for i in range(1, 71):
    if i % 7 == 0:
        print('BEEP')
    else:
        print(i)
