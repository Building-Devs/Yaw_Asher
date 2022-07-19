# My approach is to figure out the patterns and when I'm done work on the inputs
# I am not very experienced with functions so you will not see any.
# As a result I have to repeat a lot of code
num = 5 #int(input("Input any number from 1 to 5: "))
"""
for i in range(num):
    for j in range(i+1):
        print('*', end=' ')
    print()
"""
"""
if num < 6:
    for r in range(num-1):
        for c in range(r, num):
            print(' ', end=' ')
        for c in range(r+1):
            print('*', end=' ')
        for c in range(r):
            print('*', end=' ')

        #  for c in range(r):
       #     print('*', end=' ')

        print()
    for r in range(num):
        for c in range(r+1):
            print(' ', end=' ')
        for c in range(r, num):
            print('*', end=' ')
        for c in range(r, num-1):
            print('*', end=' ')
        print()

else:
    print("The input is out of range.")
"""


for r in range(num):
    for c in range(9):
        if (r + c == 4) or (c - r == 4):
            print('*', end=' ')
        elif (c == 4):
            print('1', end=' ')
        else:
            print(' ', end=' ')
    print()
