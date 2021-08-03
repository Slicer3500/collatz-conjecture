import time
#Constants
conjecturesTruth = True
naughtyLoopNumbers = [1, -1, -5, -17]
#Variables
firstTime = True
x = 0

def conj_loop():
    loop = True
    x = int(input("Please enter an integer: "))
    while loop:
        print(x)
        if (x in naughtyLoopNumbers) and (firstTime == True):
            print("You\'ll never prove the Collatz Conjecture that way. Let\'s try a different number.")
            loop = False
        if (x in naughtyLoopNumbers) and (firstTime == False):
            print("You\'ll never prove the Collatz Conjecture that way... Try again...")
            loop = False
        if (x % 2) == 0:
            x = int(x / 2)
        else:
            x = int(3 * x + 1)
            time.sleep(.125)

while conjecturesTruth:
    conj_loop()
    firstTime = False
