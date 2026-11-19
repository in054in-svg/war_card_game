import time
from classes.game import Game, Player

# # יצירת חפיסה
# game = Game()
# deck = game.make_deck()
# # for d in deck:
# #     print(d)
    
# # ערבוב
# game.Shuffling_a_deck(deck)
# # for d in deck:
# #     print(d)

# computer = Player('computer')
# player = Player('player')

# game.dealing_a_deck(deck, computer, player)

# # for card in computer.cards:
# #     print(card)
# # for card in player.cards:
# #     print(card)

# print(game.make_turn(computer, player))

def main():
    game = Game()
    while True:
        print(game.show_main_menu())
        choice = input('Choose an option:')
        match choice:
            case '1':
                deck = game.make_deck()
                game.Shuffling_a_deck(deck)
                computer = Player('computer')
                player = Player('player')
                game.dealing_a_deck(deck, computer, player)
                
                while True:
                    print(game.show_menu())
                    choice = input('Choose an option:')
                    match choice:
                        case '1':
                            print(game.make_turn(computer, player))
                        case '2':
                            print(game.show_results(computer, player))
                            break
                        case _:
                            print('Enter 1 or 2 only!')
                    time.sleep(1)
                    
            case '2':
                break
            case _:
                print('Enter 1 or 2 only!')
        time.sleep(1)
                
                
if __name__ == '__main__':
    main()