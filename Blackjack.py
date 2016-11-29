import random
import math
from playing_cards import Card
from playing_cards import Deck


def blackjack():
    deck_cards = Deck()
    deck_cards.shuffle()
    dealt_hands = deal_hand(deck_cards)
    player_hand = dealt_hands[0]
    dealer_hand = dealt_hands[1]
    if calculate_hand(player_hand) == 21:
        initial_blackjack(dealer_hand)
        return 21
    while calculate_hand(player_hand) < 22:
        turn = input("Hit or stand? h/s  ")
        if turn.lower() in ['h', 'hit']:
            new_card = deck_cards.give_top_card()
            player_hand.append(new_card)
            print("You got {}.".format(new_card))
            empty_deck = deck_cards.check_deck_has_cards()
            if empty_deck is True:
                game_over_empty_deck(player_hand, dealer_hand)
                break
        elif turn.lower() in ['s', 'stand']:
            while calculate_hand(dealer_hand) < 17:
                add_card = deck_cards.give_top_card()
                dealer_hand.append(add_card)
                empty_deck = deck_cards.check_deck_has_cards()
                if empty_deck is True:
                    game_over_empty_deck(player_hand, dealer_hand)
                    break
            end = compare_hands(player_hand, dealer_hand)
            if end is True:
                print("You win")
                break
            else:
                print("The dealer is victorious")
                break
        else:
            print("Choose hit if you want another card. Choose stand if you don't.")
    if calculate_hand(player_hand) > 21:
        print("You went over 21. The dealer is victorious")


def deal_hand(deck_cards):
    player_hand = []
    dealer_hand = []
    player_hand.append(deck_cards.give_top_card())
    dealer_hand.append(deck_cards.give_top_card())
    player_hand.append(deck_cards.give_top_card())
    dealer_hand.append(deck_cards.give_top_card())
    print("Dealer has {}".format(dealer_hand[0]))
    print("You have {} and {}".format(player_hand[0], player_hand[1]))
    return [player_hand, dealer_hand]


def initial_blackjack(dealer_hand):
    if calculate_hand(dealer_hand) == 21:
        print("It's a tie! You both have blackjack")
    else:
        print("You win! You got blackjack")


def game_over_empty_deck(player_hand, dealer_hand):
    done = compare_hands(player_hand, dealer_hand)
    if done is True:
        print("There are no more cards. You win")
    else:
        print("There are no more cards. The dealer is victorious")


def calculate_hand(hand):
    current_hand = hand
    calc_list = []
    thirteen_or_fourteen = 0
    for card in current_hand:
        if card.value in ['jack', 'queen', 'king']:
            calc_list.append(10)
        elif card.value == 'ace':
            test = []
            ace_count = 0
            for card3 in current_hand:
                if card3.value in ['jack', 'queen', 'king']:
                    test.append(10)
                elif card3.value in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
                    test.append(card3.value)
                elif card3.value == 'ace':
                    ace_count += 1
            total_minus_aces = sum(test)
            if total_minus_aces >= 11:
                calc_list.append(1)
            if total_minus_aces == 10:
                if ace_count == 1:
                    calc_list.append(11)
                if ace_count > 1:
                    calc_list.append(1)
            if total_minus_aces <= 9:
                if ace_count == 1:
                    calc_list.append(11)
                if ace_count == 2:
                    calc_list.append(6)
                if ace_count == 3:
                    if total_minus_aces == 9:
                        calc_list.append(1)
                    if total_minus_aces <= 8:
                        thirteen_or_fourteen = 13
                if ace_count == 4:
                    if total_minus_aces > 7:
                        calc_list.append(1)
                    if total_minus_aces <= 7:
                        thirteen_or_fourteen = 14
        else:
            calc_list.append(card.value)
    total = sum(calc_list) + thirteen_or_fourteen
    return total


def compare_hands(hand1, hand2):
    points1 = calculate_hand(hand1)
    points2 = calculate_hand(hand2)
    if points2 < points1 <= 21:
        return True
    elif points1 > 21:
        return False
    elif points1 <= points2 <= 21:
        return False
    elif points1 <= 21 < points2:
        return True


def main():
    while True:
        question = input("Care to play a hand? y/n  ")
        if question.lower() in ['y', 'yes']:
            blackjack()
        elif question.lower() in ['n', 'no']:
            print("Goodbye")
            quit()
        else:
            print("Please answer yes or no")


if __name__ == "__main__":
    main()
