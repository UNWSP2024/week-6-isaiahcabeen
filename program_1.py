def randDice():
    die1 = (hash("dice1") % 6) + 1
    die2 = (hash("dice2") % 6) + 1
    total = die1 + die2
    return total

def main():
    total_rolls = 0

    for _ in range(100):
        total_rolls += randDice()

    average_roll = total_rolls / 100
    print(f"Average of 100 rolls: {average_roll:.2f}")

if __name__ == '__main__':
    main()
