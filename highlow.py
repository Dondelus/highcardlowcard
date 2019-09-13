import random
from deck import Deck

def play():
    deck = Deck(shuffled=True)
    
    user_lost = False
    while deck.length() > 0:
        current_card = deck.next_card()
        deck.discard_top()

        print("Current card: %s of %s" % (current_card['name'], current_card['suit']))
        choice = input("Is the next card higher or lower? (H/L): ")

        if choice == 'H':
            # User chose higher
            next_card = deck.next_card()
            print("Next card: %s of %s" % (next_card['name'], current_card['suit']))
            if next_card['real_value'] >= current_card['real_value']:
                print("You guessed it!\n---------------------------\n")
            else:
                print("Incorrect!")
                user_lost = True
                break
        elif choice == 'L':
            # User chose lower
            next_card = deck.next_card()
            print("Next card: %s of %s" % (next_card['name'], current_card['suit']))
            if next_card['real_value'] <= current_card['real_value']:
                print("You guessed it!\n---------------------------\n")
            else:
                print("Incorrect!")
                user_lost = True
                break
        else:
            print("Your options are 'H' for Higher and 'L' for lower.")
    
    if user_lost:
        print("GAME OVER!")
    else:
        print("Awesome job making it through 52 cards!")


if __name__ == "__main__":
    play()
    

