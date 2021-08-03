import time
#Constants
conjecturesTruth = True
foreverLoop = True
naughtyLoopNumbers = [1, -1, -5, -17]
#Variables
firstTime = True
x = 0
original = 0

def conj_loop(num):
    loop = True

    while loop:
        print(num)
        if (num in naughtyLoopNumbers) and (firstTime == True):
            print("You\'ll never prove the Collatz Conjecture that way. Let\'s try a different number.")
            loop = False

        if (num in naughtyLoopNumbers) and (firstTime == False):
            print("You\'ll never prove the Collatz Conjecture that way... Try again...")
            loop = False
        if (num % 2) == 0:
            num = int(x / 2)
        else:
            num = int(3 * x + 1)
            time.sleep(.125)






##while conjecturesTruth:
##    x = int(input("Please enter an integer: "))
##    original = x
##    conj_loop(x)
##    firstTime = False