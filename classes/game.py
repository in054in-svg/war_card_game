import random
from classes.card import Card
from classes.player import Player
from classes.validation import Validation

class Game:
    def make_deck(self):
        deck = []
        flag = 4
        types = ('♥', '♠', '♦', '♣')
        while flag:
            type = types[flag - 1]
            for num in range(2,15):
                new_card = Card(num, type)
                deck.append(new_card)
            flag -= 1
        return deck
    
    
    def Shuffling_a_deck(self, deck):
        for mix in range(1000):
            i1 = random.randint(0, len(deck) - 1)
            i2 = random.randint(0, len(deck) - 1)
            while i1 == i2:
                i2 = random.randint(0, len(deck) - 1) 
            deck[i1], deck[i2] = deck[i2], deck[i1]
            
    
    def dealing_a_deck(self, deck, computer, player):
        get_card_turn = computer
        for card in deck:
            get_card_turn.cards.append(card)
            get_card_turn = player if get_card_turn == computer else computer
            
    
    def make_turn(self, computer, player):
        player_card = f'{Validation.edit_special_cards(player.cards[0].value)} {player.cards[0].type}'
        computer_card = f'{Validation.edit_special_cards(computer.cards[0].value)} {computer.cards[0].type}'
        return f"""========== TURN ==========
player: {player_card}
computer: {computer_card}
{self.check_winner(computer, player)}
Player cards: {len(player.cards)} | Computer cards: {len(computer.cards)}
=========================="""
    
            
    def check_winner(self, computer, player):
        if computer.cards[0].value > player.cards[0].value:
            computer.cards.append(player.cards.pop(0))
            computer.cards.append(computer.cards.pop(0))
            return 'Computer won the round!'
        
        elif computer.cards[0].value < player.cards[0].value:
           player.cards.append(computer.cards.pop(0))
           player.cards.append(player.cards.pop(0))
           return 'Player won the round!'

        else:
            return "It's a draw!"
        
    
    def show_main_menu(self):
        return """1. New game
2. Exit
"""
    
    
    def show_menu(self):
        return """1. Play turn
2. Exit
"""


    def show_results(self, computer, player):
        if len(player.cards) > len(computer.cards):
            winner = 'Player won the game!'
        
        elif len(computer.cards) > len(player.cards):
            winner = 'Computer won the game!'
            
        else:
            winner = "It's a draw!"
            
        return f"""====== GAME RESULTS ======
{winner}
Player cards: {len(player.cards)} | Computer cards: {len(computer.cards)}
==========================
"""