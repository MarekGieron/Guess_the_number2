import random


def guess_number():
    """
    The function starts a game where the computer guesses a number between 1 and 1000 in 10 moves.
    The user responds with 'too small', 'too big', or 'you win', and the game continues until
    the user wins or the computer runs out of moves. The game can also be stopped at any time by
    the computer if it detects cheating.
    """
    # Display instructions for the user.
    print("Think of a number between 1 and 1000 and I'll try to guess it in 10 moves.")

    # Set the initial range of possible numbers, the number of guesses, and the number of attempts
    # to cheat by the user.
    low = 1
    high = 1000
    guesses = 0
    cheat_attempts = 0

    # Loop until the user wins, the computer runs out of moves, or the computer detects cheating.
    while True:
        # Guess a random number within the current range.
        guess = random.randint(low, high)
        print(f"My guess is {guess}.")

        # Ask the user if the guess is too small, too big, or correct.
        result = input("Is it too small, too big, or did I guess correctly? ").strip().lower()

        # If the user responds 'you win', end the game and display a message.
        if result == "you win":
            print("I win!")
            break

        # If the user responds 'too small', update the range from the low end.
        elif result == "too small":
            low = guess + 1

        # If the user responds 'too big', update the range from the high end.
        elif result == "too big":
            high = guess - 1

        # Increment the number of guesses.
        guesses += 1

        # Check if the user is trying to cheat by always responding 'too small' or 'too big'.
        # If the number of cheating attempts is greater than or equal to the number of remaining moves,
        # end the game and display a message.
        if result == "too small" or result == "too big":
            cheat_attempts += 1
            remaining_moves = 10 - guesses
            if cheat_attempts >= remaining_moves:
                print("You are cheating! Game over.")
                break

        # If the number of guesses reaches 10, end the game and display a message.
        if guesses == 10:
            print("I give up.")
            break


if __name__ == '__main__':
    guess_number()

