'''
File: Modules Unit Homework
Name: Rylan Rivers
'''
import dice_roller

def main():
    """Calculates and displays statistics from multiple dice rolls."""

    num_rolls = int(input('Enter the number of dice rolls: '))
    num_sides = int(input('Enter the number of sides on the die, between 4 and 6: '))

    roll_counts = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}  # Initialize roll count dictionary

    #Use a loop to roll the die (using dice_roller.roll_die) the specified number of times.
    #Increment the count for the rolled side in the dictionary.
    for roll in range(num_rolls):
        roll = dice_roller.roll_die(num_sides)
        roll_counts[roll] += 1

    for side, count in roll_counts.items():
        probability = (count / num_rolls) * 100
        print(f'{side}\t{count}\t{probability:.2f}%')

    #Print a formatted table showing the side, number of rolls, and probability for each side.

if __name__ == "__main__":
    main()

