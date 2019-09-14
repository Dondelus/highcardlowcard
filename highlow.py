import random
from deck import Deck


def play():
    """
    Plays a game of high-card low-card
    """

    # Instantiate a new deck of cards
    deck = Deck(shuffled=True)

    # Hold whether the user has lost or not to determine an 'end-of-game' message
    user_lost = False

    # Draw a card to start the game
    current_card = deck.next_card()

    # Game will run as long as there are cards left in the deck and the user has not guessed incorrectly
    while deck.length() > 0:
        deck.discard_top()

        # Print current card and retrieve the user's guess
        print("Current card: %s of %s" %
              (current_card['name'], current_card['suit']))
        choice = input("Is the next card higher or lower? (H/L): ")

        # User chose higher
        if choice == 'H':

            # Get next card to compare and print it out
            next_card = deck.next_card()
            print("Next card: %s of %s" %
                  (next_card['name'], current_card['suit']))

            # Check if the user guessed correctly
            if next_card['real_value'] >= current_card['real_value']:
                print("You guessed it!\n---------------------------\n")
                current_card = next_card
            else:
                print("Incorrect!")
                user_lost = True
                break

        # User chose lower
        elif choice == 'L':

            # Get next card to compare and print it out
            next_card = deck.next_card()
            print("Next card: %s of %s" %
                  (next_card['name'], current_card['suit']))

            # Check if the user guessed correctly
            if next_card['real_value'] <= current_card['real_value']:
                print("You guessed it!\n---------------------------\n")
                current_card = next_card
            else:
                print("Incorrect!")
                user_lost = True
                break

        # User entered an incorrect option
        else:
            print("Your options are 'H' for Higher and 'L' for lower.")

    # Print game-over message
    if user_lost:
        print("GAME OVER!")
    else:
        print("Awesome job making it through 52 cards!")


if __name__ == "__main__":
    play()
