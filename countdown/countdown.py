import sys, time
import sevseg   # Import our sevseg.py program.

# (!) Change it to any numbere of seconds:
secondsLeft = 30

try:
    while True:
        # Clear the screen by printing several newlines:
        print('\n' * 60)

        # Get the hours/minutes/seconds from secondLeft:
        # For example: 7265 is 2 hours, 1 minutes, 5 seconds.
        # So 7265 // 3600 is 2 hour.
        hours = str(secondsLeft // 3600)
        # So 7265 % 36000 is 65, and 65 // 60 is 1 minute:
        minutes = str((secondsLeft % 3600) // 60)
        # And 7265 % 60 is 5 seconds:
        seconds = str(secondsLeft % 60)

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow , mBottomRow = mDigits.splitlines()


