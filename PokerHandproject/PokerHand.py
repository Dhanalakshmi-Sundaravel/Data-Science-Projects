#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:47:22 2018

@author: uxac007
"""

import copy
from Card import Card, Hand, Deck

class ThreeCardPokerDeck(Deck):
    """
    Three-Card Poker deck
    """
    
    def deal_hand(self, name=""):
        """
        Creates a new instance of ThreeCardPokerHand
        hand and initializes it with 3 cards from the deck.
        An optional name argument can be used to specify the 
        name of the player.
        Returns the instance of ThreeCardPokerHand thus created
        """
        hand = ThreeCardPokerHand(self.pop_cards(3), name)
        return hand

class ThreeCardPokerHand(Hand):
    """
    Three-Card Poker hand
    """
    
    all_labels = ['Nothing', 'Pair', 'Flush', 'Straight', 'Three of a Kind',
                  'Straight Flush']
    rank = 0
    
#   Question 2
    def _compute_rank(self):
        """
        self, this instance of ThreeCardPokerHand
        Computes the ranking of self and stores it 
        in the self.rank attribute according to the 
        rules described in Question 2 of the project brief.
        Returns None
        """
        rankCount = []
        suiteCount = [] 
        seqCount = 0
        for i in range (len(Card.ranks)):
            rankCount.append(self.ranks.count(i))
                               
        for i in range (len(Card.suits)):
            suiteCount.append(self.suits.count(i))
            
        for i in range (len(Card.ranks)): 
            if ( i == 0):
                if(self.ranks.count(12)>=1):
                    seqCount = seqCount + 1 
            
            if(self.ranks.count(i)>=1):
                seqCount = seqCount + 1  
            else:
                if(seqCount < 3):
                    seqCount = 0
        
        #print(self.ranks)
        #print(self.suits)
        #print(rankCount)
        #print(suiteCount)
        #print(seqCount)
        #print(self.get_rank())
        sameSuite = "False"
        #Logic for finding Same Suite
        # Unsorted Rank
        s0 = []
        s1 = []
        s2 = []
        s3 = []
        seqCountS0 = 0
        seqCountS1 = 0
        seqCountS2 = 0
        seqCountS3 = 0
        for card in self.cards:
            if(card.get_suit()==0):
                s0.append(card.get_rank())
            if(card.get_suit()==1):
                s1.append(card.get_rank())
            if(card.get_suit()==2):
                s2.append(card.get_rank())
            if(card.get_suit()==3):
                s3.append(card.get_rank())
         
        for i in range (len(Card.ranks)):   
            if ( i == 0):
                if(s0.count(12)>=1):
                    seqCountS0 = seqCountS0 + 1 
            if(s0.count(i)>=1):
                seqCountS0 = seqCountS0 + 1  
            else:
                if(seqCountS0 < 3):
                    seqCountS0 = 0
                    
        for i in range (len(Card.ranks)):    
            if ( i == 0):
                if(s1.count(12)>=1):
                    seqCountS1 = seqCountS1 + 1 
            if(s1.count(i)>=1):
                seqCountS1 = seqCountS1 + 1  
            else:
                if(seqCountS1 < 3):
                    seqCountS1 = 0
                    
        for i in range (len(Card.ranks)):    
            if ( i == 0):
                if(s2.count(12)>=1):
                    seqCountS2 = seqCountS2 + 1 
            
            if(s2.count(i)>=1):
                seqCountS2 = seqCountS2 + 1  
            else:
                if(seqCountS2 < 3):
                    seqCountS2 = 0
                    
        for i in range (len(Card.ranks)):  
            if ( i == 0):
                if(s3.count(12)>=1):
                    seqCountS3 = seqCountS3 + 1         
            if(s3.count(i)>=1):
                seqCountS3 = seqCountS3 + 1  
            else:
                if(seqCountS3 < 3):
                    seqCountS3 = 0
        if (seqCountS0>=3) or (seqCountS1>=3) or (seqCountS2>=3) or (seqCountS3>=3):
            sameSuite = "True"
       
        
        if sameSuite=="True": 
            self.rank = 5
        elif max(rankCount)>=3:
            self.rank = 4
        elif seqCount >= 3:
            self.rank = 3
        elif max(suiteCount)>=3:
            self.rank = 2
        elif max(rankCount)>=2:
            self.rank = 1
        else:
            self.rank = 0
        return

#   Question 3    
    def _compare(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Implements the comparison rules for two ThreeCardPoker
        hands as per the description in Question 3 of the project brief.
        Returns -1 if other is a winning hand, 1 if self is the winning hand,
        and 0 if self and other are tied up.
        """
        r1 = self.get_rank()
        r2 = other.get_rank()
        #print(self.ranks)
        highestRank1 = 0
        highestRank2 = 0
        if(r1 == r2):
            # Straight Flush and Straight 
            if (r1 == 5 or r1 == 4):
                if self.ranks.__contains__(12) :
                    highestRank1 = 3
                else:
                    highestRank1 = max(self.ranks)
                if other.ranks.__contains__(12) :
                    highestRank2 = 3
                else:
                    highestRank2 = max(other.ranks)
                    
                if  highestRank1 > highestRank2 :
                    return 1
                elif highestRank1 < highestRank2 :
                    return -1
                else:
                    return 0
            # Three of a kind
            if (r1 ==  3):
                 if  max(self.ranks) > max(other.ranks) :
                    return 1
                 else:
                    return -1
            # Flush or nothing
            if (r1 == 2 or r1 == 0):
                for i in range (len(self.ranks)):
                    if (self.ranks[i] > other.ranks[i]):
                        return 1
                    else:
                        return -1
                return 0    
            # pair 
            if (r1 == 1):
                pairRank1 = 0 
                pairRank2 = 0
                for i in range (len(Card.ranks)):
                    if (self.ranks.count(i) == 2):
                        pairRank1 = i
                    if (other.ranks.count(i) == 2):
                        pairRank2 = i
                if pairRank1 > pairRank2:
                    return 1
                elif pairRank1 < pairRank2:
                    return -1
                else:
                    if max(self.ranks) > max(other.ranks):
                        return 1
                    elif max(self.ranks) < max(other.ranks):
                        return -1
                    else:
                        return 0
        elif r1 > r2:
            return 1
        else:
            return -1
    
    def get_rank(self):
        """
        getter method for the 
        rank attribute
        Returns 0, 1, 2, 3, 4, 5 if the
        self's rank is respectively Nothing, 
        Pair, Flush, Straight, Three of a Kind, and Straight Flush
        """
        return self.rank
    

    def __init__(self, cards, name=""):
        Hand.__init__(self, name)
        self.cards = copy.deepcopy(cards)
        self.ranks = [card.get_rank() for card in self.cards]
        self.ranks.sort(reverse = True)
        self.suits = [card.get_suit() for card in self.cards]
        self._compute_rank()

    def __lt__(self, other):
        return True if self._compare(other) < 0 else False
    
    def __le__(self, other):
        return True if self._compare(other) <= 0 else False

#   Question 3
    def __gt__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self is the winning hand, False otherwise
        """
        return True if self._compare(other) > 0 else False

#   Question 3    
    def __ge__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self is the winning hand or
        self and other are tied; False otherwise
        """
        return True if self._compare(other) >= 0 else False

#   Question 3    
    def __eq__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self and other are tied; 
        False otherwise
        """
        return True if self._compare(other) == 0 else False

#   Question 3    
    def __ne__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self and other are not tied; 
        False otherwise
        """
        return True if self._compare(other) != 0 else False

    def get_label(self):
        """
        self, this instance of ThreeCardPokerHand
        Returns a string representation of self.
        """
        return ThreeCardPokerHand.all_labels[self.rank]
    
    def get_full_label(self):
        """
        self, this instance of ThreeCardPokerHand
        Returns a string representation of self replacing
        the Nothing ranking with the highest ranking card.
        Used internally by __str__().
        """
        return  Card.ranks[self.ranks[0]] + '-High' if self.rank == 0 else \
            self.get_label()
        
    def __str__(self):
        """
        self, this instance of ThreeCardPokerHand
        Returns a string representation of self that 
        includes the list of the cards, and the rank.
        """
        return Hand.__str__(self) + '\nHand Rank: ' + self.get_full_label()
        
          
if __name__ == '__main__':
    """
    Test cases
    """
#   Queen-high
    hand1 = ThreeCardPokerHand([Card(10, 0), Card(1, 1), Card(0, 2)])
    print(hand1)
    print()

#   Straight Flush with Ace  - need to correct
    hand2 = ThreeCardPokerHand([Card(12, 0), Card(1, 0), Card(0, 0)])
    print(hand2)
    print()
  
    print(hand1 < hand2) # True
    print(hand1 > hand2) # False
    print(hand1 <= hand2) # True
    print(hand1 >= hand2) # False
    print(hand1 == hand2) # False
    print(hand1 != hand2) # True
    print()
    
#   3-Pair + Jack
    hand1 = ThreeCardPokerHand([Card(1, 0), Card(1, 1), Card(9, 2)])
    print(hand1)
    print()

#   2-Pair + Ace
    hand2 = ThreeCardPokerHand([Card(12, 0), Card(0, 1), Card(0, 0)])
    print(hand2)
    print()
    
    print(hand1 < hand2) # False
    print(hand1 > hand2) # True
    print(hand1 <= hand2) # False
    print(hand1 >= hand2) # True
    print(hand1 == hand2) # False
    print(hand1 != hand2) # True
    print()


  
#   Straight Flush    
    print()
    hand3 = ThreeCardPokerHand([Card(0, 0), Card(1, 0), Card(12, 0)], 'Ruben')
    print(hand3)

#   Straight    
    print()
    hand3 = ThreeCardPokerHand([Card(0, 1), Card(12, 2), Card(1, 0)], 'Greg')
    print(hand3)  

#   Straight Flush    
    print()
    hand3 = ThreeCardPokerHand([Card(12, 1), Card(10, 1), Card(11, 1)], 'Dealer')   
    print(hand3)                      
    
#   Flush
    print()
    hand3 = ThreeCardPokerHand([Card(0, 1), Card(1, 1), Card(11, 1)], 'Player')   
    print(hand3)                      