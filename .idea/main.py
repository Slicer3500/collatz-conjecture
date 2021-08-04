import time

#Constants
conjecturesTruth = True
foreverLoop = True
naughtyLoopNumbers = [1, -1, -5, -17]

#Variables
firstTime = True
iterationCount = 0


def iterator(num, iterationCount):
    return num + iterationCount

#def firstTimeFalse(firstTime):
#    return firstTime = False

def conjLoop(num):
    loop = True
    while loop:
        print(num)
        if (num in naughtyLoopNumbers) and (firstTime == False):
            print("You\'ll never prove the Collatz Conjecture that way... Trying another number...")
            loop = False

        if (num in naughtyLoopNumbers) and (firstTime == True):
            print("You\'ll never prove the Collatz Conjecture that way. Let\'s try a different number.")
            loop = False

        if (num % 2) == 0:
            num = int(num / 2)

        else:
            num = int(3 * num + 1)
            time.sleep(.01)

def iteratorPositiveBruteForceLoop(num):
    while conjecturesTruth:
        iterationCount = 0
        conjLoop(num)
        iterationCount += 1
        num = iterator(num, iterationCount)
        time.sleep(.5)

def main():
    num = int(input("Please enter an integer: "))
    conjLoop(num)
    #firstTime = False
    num = int(input("Please enter an integer: "))
    iteratorPositiveBruteForceLoop(num)

main()