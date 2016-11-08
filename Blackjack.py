import random
import math

from playing_cards import Card
from playing_cards import Deck

def blackjack():
    trick = Deck()
    trick.shuffle()
    player_hand = []
    dealer_hand = []
    player_hand.append(trick.give_top_card())
    dealer_hand.append(trick.give_top_card())
    player_hand.append(trick.give_top_card())
    dealer_hand.append(trick.give_top_card())
    print("Dealer has {}".format(dealer_hand[0]))
    print("You have {} and {}".format(player_hand[0], player_hand[1]))
    if calculate_hand(player_hand) == 21:
        if calculate_hand(dealer_hand) == 21:
            print("It's a tie! You both have blackjack")
            return 21
        else:
            print("You win! You got blackjack")
            return 21
    while calculate_hand(player_hand) < 22:
        turn = input("Hit or stand? H/s  ")
        if turn.lower() == 'h' or turn.lower() == 'hit':
            new_card = trick.give_top_card()
            player_hand.append(new_card)
            print("You got {}.".format(new_card))
            empty_deck = trick.check_deck()
            if empty_deck == True:
                done = compare_hands(player_hand, dealer_hand)
                if done == True:
                    print("There are no more cards. You win")
                    break
                else:
                    print("There are no more cards. The dealer is victorious")
                    break
        elif turn.lower() == 's' or turn.lower() == 'stand':
            while calculate_hand(dealer_hand) < 17:
                add_card = trick.give_top_card()
                dealer_hand.append(add_card)
                empty_deck2 = trick.check_deck()
                if empty_deck2 == True:
                    null_deck = compare_hands(player_hand, dealer_hand)
                    if null_deck == True:
                        print("The dealer took the rest of the cards. You win")
                        break
                    else:
                        print("The dealer took the rest of the cards. The dealer is victorious")
                        break
            end = compare_hands(player_hand, dealer_hand)
            if end == True:
                print("You win")
                break
            else:
                print("The dealer is victorious")
                break
        else:
            print("Choose hit if you want another card. Choose stand if you don't.")
    if calculate_hand(player_hand) > 21:
        print("You went over 21. The dealer is victorious")



def calculate_hand(hand):
    current_hand = hand
    calc_list = []
    thirteen_or_fourteen = 0
    for card in current_hand:
        if card.value == 'jack' or card.value == 'queen' or card.value == 'king':
            calc_list.append(10)
        elif card.value == 'ace':
            test = []
            ace_count = []
            for card3 in current_hand:
                if card3.value == 'jack' or card3.value == 'queen' or card3.value == 'king':
                    test.append(10)
                elif card3.value == 2 or card3.value == 3 or card3.value == 4 or card3.value == 5 or card3.value == 6 or card3.value == 7 or card3.value == 8 or card3.value == 9 or card3.value == 10:
                    test.append(card3.value)
                elif card3.value == 'ace':
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
            calc_list.append(card.value)
    total = sum(calc_list) + thirteen_or_fourteen
    return total

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
