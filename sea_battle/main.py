from board import Board
from player import Player, BotPlayer
from game import Game

def main():
    bot_board = Board(hid=True)
    user_board = Board(hid=False)

    user = Player(user_board, bot_board)
    bot = BotPlayer(bot_board, user_board)

    game = Game(user, bot)

    game.start()

if __name__ == '__main__':
    main()
