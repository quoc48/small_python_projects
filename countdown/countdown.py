import sys, time
import sevseg   # Import our sevseg.py program.

# (!) Change it to any numbers of seconds:
secondsLeft = 30

try:
    while True: # main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)

        # Get the hours/minutes/seconds from secondLeft:
        # For example: 7265 is 2 hours, 1 minutes, 5 seconds.
        # So 7265 // 3600 is 2 hour.
        hours = str(secondsLeft // 3600)
        # And 7265 % 36000 is 65, and 65 // 60 is 1 minute:
        minutes = str((secondsLeft % 3600) // 60)
        # And 7265 % 60 is 5 seconds:
        seconds = str(secondsLeft % 60)

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits:
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(sBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print('   * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl+C to quit.')

        time.sleep(1)   # Insert a one-second pause.
        secondsLeft -= 1

except KeyboardInterrupt:
    print('Countdown, by AI Sweigart')
    sys.exit()  # When Ctr-C is pressed, end the program.



