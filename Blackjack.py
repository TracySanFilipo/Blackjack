import random
import math

from playing_cards import Card
from playing_cards import Deck

def blackjack():
    trick = [('heart', 'ace'), ('heart', 2), ('heart', 3), ('heart', 4), ('heart', 5), ('heart', 6), ('heart', 7), ('heart', 8), ('heart', 9), ('heart', 10), ('heart', 'jack'), ('heart', 'queen'), ('heart', 'king'), ('diamond', 'ace'), ('diamond', 2), ('diamond', 3), ('diamond', 4), ('diamond', 5), ('diamond', 6), ('diamond', 7), ('diamond', 8), ('diamond', 9), ('diamond', 10), ('diamond', 'jack'), ('diamond', 'queen'), ('diamond', 'king'), ('spade', 'ace'), ('spade', 2), ('spade', 3), ('spade', 4), ('spade', 5), ('spade', 6), ('spade', 7), ('spade', 8), ('spade', 9), ('spade', 10), ('spade', 'jack'), ('spade', 'queen'), ('spade', 'king'), ('club', 'ace'), ('club', 2), ('club', 3), ('club', 4), ('club', 5), ('club', 6), ('club', 7), ('club', 8), ('club', 9), ('club', 10), ('club', 'jack'), ('club', 'queen'), ('club', 'king')]
    # trick = shuffle(playlist)
    player_hand = []
    dealer_hand = []
    print(trick)
    four_cards = deal_initial_hands(trick)
    player_hand.append(four_cards[0])
    dealer_hand.append(four_cards[1])
    player_hand.append(four_cards[2])
    dealer_hand.append(four_cards[3])
    print("Dealer has {}".format(dealer_hand[0]))
    print("You have {} and {}".format(player_hand[0], player_hand[1]))
    if calculate_hand(player_hand) == 21:
        if calculate_hand(dealer_hand) == 21:
            print("It's a tie!")
            return 21
        else:
            print("You win!")
            return 21
    while calculate_hand(player_hand) < 22:
        turn = input("Hit or stand? H/s  ")
        if turn.lower() == 'h' or turn.lower() == 'hit':
            new_card = give_top_card(trick)
            player_hand.append(new_card)
            check_deck(trick)
        elif turn.lower() == 's' or turn.lower() == 'stand':
            while calculate_hand(dealer_hand) < 17:
                add_card = give_top_card(trick)
                dealer_hand.append(add_card)
            end = compare_hands(player_hand, dealer_hand)
            if end == True:
                print("You win")
                break
            else:
                print("The dealer is victorious")
                break
        else:
            print("Choose hit if you want another card. Choose stand if you don't.")
    if calculate_hand(player_hand) > 22:
        print("The dealer is victorious")

# def shuffle(group):
#     bridges = random.shuffle(group)
#     return bridges

def calculate_hand(hand):
    current_hand = hand
    calc_list = []
    thirteen_or_fourteen = 0
    for card in current_hand:
        if card[1] == 'jack' or card[1] == 'queen' or card[1] == 'king':
            calc_list.append(10)
        elif card[1] == 'ace':
            test = []
            ace_count = []
            for card3 in current_hand:
                if card3[1] == 'jack' or card3[1] == 'queen' or card3[1] == 'king':
                    test.append(10)
                elif card3[1] == 2 or card3[1] == 3 or card3[1] == 4 or card3[1] == 5 or card3[1] == 6 or card3[1] == 7 or card3[1] == 8 or card3[1] == 9 or card3[1] == 10:
                    test.append(card3[1])
                elif card3[1] == 'ace':
                    ace_count.append(1)
            list_no_aces = sum(test)
            number_aces = sum(ace_count)
            if list_no_aces >= 11:
                 calc_list.append(1)
            if list_no_aces == 10:
                if number_aces == 1:
                    calc_list.append(11)
                if number_aces > 1:
                    calc_list.append(1)
            if list_no_aces <= 9:
                if number_aces == 1:
                    calc_list.append(11)
                if number_aces == 2:
                    calc_list.append(6)
                if number_aces == 3:
                    if list_no_aces == 9:
                        calc_list.append(1)
                    if list_no_aces <= 8:
                        thirteen_or_fourteen = 13
                if number_aces == 4:
                    if list_no_aces > 7:
                        calc_list.append(1)
                    if list_no_aces <= 7:
                        thirteen_or_fourteen = 14
        else:
            calc_list.append(card[1])
    total = sum(calc_list) + thirteen_or_fourteen
    return total


def deal_initial_hands(deck1):
    base_deck = deck1
    print(base_deck)
    clover = []
    clover.append(base_deck.pop(0))
    clover.append(base_deck.pop(1))
    clover.append(base_deck.pop(2))
    clover.append(base_deck.pop(3))
    return clover


def give_top_card(deck1):
    print("The card is {}".format(deck1[0]))
    return deck1.pop(0)


def check_deck(deck1):
    height = len(deck1)
    if height < 1:
        print('empty deck')


def compare_hands(hand1, hand2):
    points1 = calculate_hand(hand1)
    points2 = calculate_hand(hand2)
    if points2 <= points1 <= 21:
        return True
    elif points1 > 21:
        return False
    elif points1 <= points2 <= 21:
        return False
    elif points1 <= 21 < points2:
        return True


def main():
    while True:
        question = input("Care to play a hand? Y/n  ")
        if question.lower() == 'y' or question.lower() == 'yes':
            blackjack()
        elif question.lower() == 'n' or question.lower() == 'no':
            print("Goodbye")
            quit()
        else:
            print("Please answer yes or no")


if __name__ == "__main__":
    main()
