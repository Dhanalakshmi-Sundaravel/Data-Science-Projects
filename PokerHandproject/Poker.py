#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:25:20 2018

@author: uxac007
"""


from PokerHand import ThreeCardPokerDeck, ThreeCardPokerHand
from Card import Card

# Question 4
def make_dist(n):
    """
    n, a positive integer
    Runs n trials of comprising of dealing 
    a Three-Card Poker hand from a randomly shuffled
    deck, and summarizing the percentage probabilities 
    of the possible hand ranks represented as strings.
    Returns a dictionary mapping the hand tring labels to 
    float percentages.
    """
    
    thisdict =	{
            "Pair": 0,
            "Nothing": 0,
            "Flush": 0,
            "Straight": 0,
            "Straight Flush": 0,
            "Three of a Kind": 0
            }
    
    
    for i in range(n):
        deck = ThreeCardPokerDeck()  
        deck.shuffle()
        player_hand = deck.deal_hand("Player")
        playerLabel = player_hand.get_label();
        #print(playerLabel)
        str1 = "Nothing"
        str2 = "Pair"
        str3 = "Flush"
        str4 = "Straight"
        str5 = "Three of a Kind"
        str6 = "Straight Flush"
        if playerLabel is str1:
            thisdict["Nothing"] = thisdict["Nothing"] + 1;
        if playerLabel is str2:
            thisdict["Pair"] = thisdict["Pair"] + 1;
        if playerLabel is str3:
            thisdict["Flush"] = thisdict["Flush"] + 1;
        if playerLabel is str4:
            thisdict["Straight"] = thisdict["Straight"] + 1;
        if len(playerLabel) == len(str5):
            thisdict["Three of a Kind"] = thisdict["Three of a Kind"] + 1;
        if len(playerLabel) == len(str6):
            thisdict["Straight Flush"] = thisdict["Straight Flush"] + 1;
    thisdict["Nothing"]         = float("{0:.2f}".format((thisdict["Nothing"] / n) * 100));
    thisdict["Pair"]            = float("{0:.2f}".format((thisdict["Pair"] / n) * 100));
    thisdict["Flush"]           = float("{0:.2f}".format((thisdict["Flush"] / n)*100));
    thisdict["Straight"]        = float("{0:.2f}".format((thisdict["Straight"] / n)*100));
    thisdict["Three of a Kind"] = float("{0:.2f}".format((thisdict["Three of a Kind"] / n)*100));
    thisdict["Straight Flush"]  = float("{0:.2f}".format((thisdict["Straight Flush"] / n)*100));
    return thisdict


# A ThreeCardPokerHand object initialized with the 
# smallest hand that can be played by the dealer. 
# Use it to determine if the dealer's hand can play
# in your play_round code 
min_dealer_hand = ThreeCardPokerHand([Card(10, 0), Card(1, 1), Card(0, 2)])

# Question 5
def play_round(dealer_hand, player_hand, cash, get_ante, is_playing):
    """
    dealer_hand, an instance of ThreeCardPokerHand holding the
    hand dealt to the dealer at the beginning of the round
    player_hand, an instance of ThreeCardPokerHand holding the
    hand dealt to the dealer at the beginning of the round
    cash, a positive integer, the amount of cash available to the 
    player at the beginning of the round
    get_ante, a function, takes cash as argument and returns 
    the player's ante bet
    is_playing, a function, takes the player's hand as arugment
    and returns True if the player plays, and False if the player folds.
    Returns: tuple (ante, outcome), ante is the ante bet
    returned by get_ante, and outcome is  
    -2 if the dealer qualifies, the player plays and loses,
    -1 if the player folds
    0 if the dealer qualifies, the player plays, and the hands tie up
    1 if the dealer does not qualify, and the player plays.
    """
    betAmount = get_ante(cash);
    Playing = is_playing(player_hand);
    result = 0 
    if Playing is True:
        dealerHand = dealer_hand.get_label()
        if dealerHand == "Queen-High":
           if player_hand._compare(dealer_hand) == 0:
               result = 0
           elif player_hand._compare(dealer_hand) == -1:
               result = -2      
        else:
            result = 1
    else:
        result = -1     
    tupleReturn = (betAmount, result)
    return tupleReturn

    
def get_ante(cash):
    """
    A sample get_ante function.
    Feel free to customize as needed
    """
    return int(input('Enter your ante bet (Cash=' + str(cash) + '): '))
    
def is_playing(player_hand):
    """
    A sample is_playing function.
    Feel free to customize as needed.
    """
    print(player_hand)
    return True if input("Play or fold  (p/f): ") == 'p' else False

def proc_outcome(outcome, ante, dealer_hand):
    """
    A sample function to process the outcome
    of the round. 
    Feel free to customize as needed.
    """
    out = ['Tie', 'Dealer does not qualify', 'You won', 'You lost', 'You folded']
    payoff = outcome * ante
    print(dealer_hand)
    print(out[outcome] + ': ' + ('+' if payoff > 0 else '') + str(payoff))
    return payoff

def play(trials, stake, goal):
    """
    trials, positive integer, the number of trial game runs
    stake, positive integer, the initial amount of cash available to the player
    goal, the amount of cash the player is hoping to have by the end of each trial game
    Runs the trials number of trial games of Three-Hand Poker. Each trial run
    proceeds as long as the amount of cash available to the player is 
    both positive and below the goal. Each round is implemented by 
    calling the play_round() function below. 
    Prints various stats upon termination.
    """
    wins, gain, rounds, win_rounds, tie_rounds, lose_rounds = 0, 0, 0, 0, 0, 0
    for _ in range(trials):
        cash = stake
        while cash > 0 and cash < goal:
            deck = ThreeCardPokerDeck()
            deck.shuffle()
            player_hand = deck.deal_hand("Player")
            dealer_hand = deck.deal_hand("Dealer")
#           Invoke your implementation of play_round
            (ante, outcome) = \
                play_round(dealer_hand, player_hand, cash, get_ante, is_playing)
            cash += proc_outcome(outcome, ante, dealer_hand)
            rounds += 1
            win_rounds += 1 if outcome > 0 else 0
            tie_rounds += 1 if outcome == 0 else 0
            lose_rounds += 1 if outcome < 0 else 0
        wins += 1 if cash >= goal else 0
        gain += cash - stake
    print('Finished', trials, 'trial games')
    print('Winning games (%)', 100 * wins / trials)
    print('Average gain per game', gain / trials)
    print('Average number of rounds per game:', rounds / trials)
    print('Average number of winning rounds per game:', win_rounds / trials)
    print('Average number of tied rounds per game:', tie_rounds / trials)
    print('Average number of losing rounds per game:', lose_rounds / trials)

if __name__ == '__main__':
#   Estimate Three-Card Poker hand probabilities by running 
#   10000 random hand deals
    print(make_dist(10000))
    
#   This will play a single game of Three-Card Poker with the
#   initial stake of 100, and a goal to turn it into 200.
    play(1, 100, 200)
 