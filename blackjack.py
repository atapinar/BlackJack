import random
import sys

# Initialize the deck of cards
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = [
    {"rank": "A", "value": 11},
    {"rank": "2", "value": 2},
    {"rank": "3", "value": 3},
    {"rank": "4", "value": 4},
    {"rank": "5", "value": 5},
    {"rank": "6", "value": 6},
    {"rank": "7", "value": 7},
    {"rank": "8", "value": 8},
    {"rank": "9", "value": 9},
    {"rank": "10", "value": 10},
    {"rank": "J", "value": 10},
    {"rank": "Q", "value": 10},
    {"rank": "K", "value": 10},
]

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append({"suit": suit, "rank": rank["rank"], "value": rank["value"]})
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = sum(card['value'] for card in hand)
    # Adjust for Aces if value is over 21
    aces = sum(1 for card in hand if card['rank'] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(hand, name):
    cards = [f"{card['rank']} of {card['suit']}" for card in hand]
    print(f"{name}'s hand: {', '.join(cards)} (Value: {calculate_hand_value(hand)})")

def blackjack_game():
    while True:
        # Create and shuffle deck
        deck = create_deck()

        # Initial dealing
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Display hands
        display_hand(player_hand, "Player")
        print(f"Dealer's hand: {dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}, [Hidden]")

        # Player's turn
        while calculate_hand_value(player_hand) < 21:
            move = input("Do you want to 'hit' or 'stand'? ").lower()
            if move == 'hit':
                player_hand.append(deck.pop())
                display_hand(player_hand, "Player")
            elif move == 'stand':
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")

        player_value = calculate_hand_value(player_hand)
        if player_value > 21:
            print("Player busts! Dealer wins.")
        else:
            # Dealer's turn
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())

            # Display final hands
            display_hand(player_hand, "Player")
            display_hand(dealer_hand, "Dealer")

            dealer_value = calculate_hand_value(dealer_hand)

            # Determine winner
            if dealer_value > 21:
                print("Dealer busts! Player wins.")
            elif dealer_value > player_value:
                print("Dealer wins.")
            elif dealer_value < player_value:
                print("Player wins!")
            else:
                print("It's a tie!")

        # Ask if the player wants to continue
        continue_playing = input("Do you want to continue playing? (yes/no): ").lower()
        if continue_playing in ['no', 'n']:
            print("Thanks for playing! Goodbye!")
            sys.exit(0)
        elif continue_playing in ['yes', 'y']:
            continue
        else:
            print("Invalid input. Exiting the game.")
            sys.exit(0)

# Start the game
if __name__ == "__main__":
    blackjack_game()
