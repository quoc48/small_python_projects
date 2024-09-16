import copy, sys

TOTAL_DISKS = 5

# Start with all disks on tower A:
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))

def main():
    print(""" Move the tower of disks, one disk at a time, to another tower.
        Larger disks cannot rest on top of a smaller disk.""")

    # Set up the towers. The end of the list is the top of the tower.
    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}

    while True:
        # Display the towers and disks:
        displayTowers(towers)

        # Ask the user for a move:
        fromTower, toTower = askForPlayerMove(towers)

        # Move the top disk from fromTower to toTower:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # Check if the user has solved the puzzle:
        if COMPLETE_TOWER in (towers['B'], towers['C']):
            displayTowers(towers)
            print('You have solved the puzzle! Well done!')
            sys.exit()

def askForPlayerMove(towers):
    """Ask the player for a move. Returns (fromTower, toTower)."""

    while True:
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print('(e.g AB to move a disk from tower A to tower B.)')
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thank for playing!')
            sys.exit()

        # Make sure the user entered valid tower letters:
        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Enter one of AB, AC, BA, BC, CA, or CB.')
            continue    # Ask player again for their move.