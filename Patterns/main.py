"""
Asher,
     I am not very experienced with functions so you will not see any.
    As a result I have to repeat a lot of code.
"""
# This takes input from the user within the range 1 to 5.
num = int(input("Input any number from 1 to 5: "))

# This starts the conditions for the defined range.
if num < 6: # This block will be executed only if the input falls within the specified range.

    if num == 1: # This is for when the input is 1.
        # Asher, I will need your help with this pattern.
        print("This pattern is still under construction.")

    elif num == 2: # This is for when the input is 2.
        for row in range(5):
            for col in range(row + 1):
                print('*', end=' ')
            print()

    elif num == 3: # This is for when the input is 3.
        for row in range(5):
            for col in range(9):
                if (row + col == 4) or (col - row == 4):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()

    elif num == 4: # This is for when the input is 4.
        # Asher, I will also need your help here.
        print("This pattern is still under construction.")

    elif num == 5: # This is for when the input is 5.
        for row in range(5):
            for col in range(9):
                if (row + col == 4) or (col - row == 4):
                    print('*', end=' ')
                elif (col == 4):
                    print(row, end=' ')
                else:
                    print(' ', end=' ')
            print()

# This message appears when the input is out of range.
else:
    print("This input is out of range.")
