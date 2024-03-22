import os
from board import Board
from player import Player, BotPlayer



class Game:

    user: Player
    bot: BotPlayer


    def __init__(self, user: Player, bot: BotPlayer):
        
        self.user = user
        self.bot = bot


    # заполнение досок
    def _fill_boards(self):

        self.bot.fill_with_ships()
        self.user.fill_with_ships()

    #! чтобы скипнуть ручное заполнение 
    # def _test_fill_boards(self):

    #     self.bot.fill_with_ships()
    #     self.user.self_board = self.bot._create_test_board()


    # реализация последовательных ходов игроков
    def _game(self) -> bool:

        winner = False

        os.system('cls')

        # стартовое поле поле
        print('ДОСКА БОТА:')
        self.bot.self_board.show_board()
        print('ВАША ДОСКА:')
        self.user.self_board.show_board()

        # игра идет, дтбо пока у игрока есть корабли
        while self.user.self_board._alife_ships:

            self.user.move()

            # либо пока у бота не кончатся корабли
            if not self.bot.self_board._alife_ships:
                winner = True
                break

            self.bot.move()


        return winner


    def start(self) -> None:
        
        self._fill_boards()

        # победитель ли настоящий человек
        winner = self._game()

        if winner:
            print('Вы победили!')

        else:
            os.system('cls')    

            # захотел, при поражении игрока, показать ему состояние доски бота
            # без спрятанных кораблей
            self.bot.self_board.hid = True

            print('ДОСКА БОТА:')
            self.bot.self_board.show_board()
            print('ВАША ДОСКА:')
            self.user.self_board.show_board()

            print('Вы проиграли!')
