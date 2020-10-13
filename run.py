import random
def diceRoll():
    """
    A function that simulates three dice roll.
    :return: sum of three dice roll
    """
    dice1 = random.randint(1,6)  # since all the sides of a dice have an equal likelihood, so we can just use randint to simulate a dice throw
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)

    return dice1 + dice2 + dice3
goodOutcomes = {9,11,13,17,18,8,5,3,14,7} # asked from the koenyer. legit source

numberOfSimulations = int(input("Enter number of simulations you want to try (has to be an integer greater than 0): "))
diceRollOutcomes = {'shoZangmi': 0, 'shoMazangmi': 0}
for everySimulation in range(numberOfSimulations):
    for eachShoRoll in range(3): # since we roll the dice 3 times until we hit a lucky num
        diceOutcome = diceRoll()
        if diceOutcome in goodOutcomes:
            diceRollOutcomes['shoZangmi'] += 1
            if diceOutcome not in diceRollOutcomes.keys(): # if its the first time we are getting the number in this simulation then need to add it
                diceRollOutcomes[diceOutcome] = 1
                break
            else: # if not then just increment the count
                diceRollOutcomes[diceOutcome] += 1
                break
        elif eachShoRoll == 2: # that is we are on the third sho roll and we havent gotten any of the good numbers
            diceRollOutcomes['shoMazangmi'] += 1
            if diceOutcome not in diceRollOutcomes.keys():
                diceRollOutcomes[diceOutcome] = 1
            else:
                diceRollOutcomes[diceOutcome] += 1
print(diceRollOutcomes)