#Eddie Beloiu
#Cs 161
#project 4b

def fib(pos_int):
    """Function that takes a positive integer parameter and returns the number at that position of the Fibonacci sequence."""
    num_x = 1
    num_y = 1
    if pos_int == 1:            #the first and 2nd numbers in the sequence are both 1.
        return 1
    elif pos_int == 2:
        return 1
    else:
        while pos_int > 2:          #loop for all positive integers
            sum = num_x + num_y
            num_x = num_y
            num_y = sum
            pos_int = pos_int -1
        return sum
answer = fib(int(input()))
print(answer)