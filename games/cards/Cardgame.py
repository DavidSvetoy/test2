from games.cards.Deckofcards import *
from games.cards.Card import Card
from games.cards.Player import Player
import random
class Card_Game:
    def __init__(self,player1,player2,NumofCards=10):
        self.NumofCards=NumofCards
        self.Deck=DeckOfCards()
        self.player1=Player(player1)
        self.player2=Player(player2)
        self.new__game()
    def __str__(self):
         return f"{self.Deck}"

    def new__game(self):
        self.Deck.shuffle()
        self.player1.set_hand(self.Deck)
        self.player2.set_hand(self.Deck)
        # return ( self.player2.set_hand(self.Deck))

    def get_winner(self):
        if len(self.player1.player_deck)>len(self.player2.player_deck):
            return f"{self.player2.name} won the match!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        elif len(self.player1.player_deck)==len(self.player2.player_deck):
            return None
        else:
            return f"{self.player1.name} won the match!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"




deck1=DeckOfCards()
deck1.shuffle()

# print(deck1)


