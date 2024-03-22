
def main():
    bot_board = Board(hid=True)
    user_board = Board(hid=False)

    user = Player(user_board, bot_board)
    bot = BotPlayer(bot_board, user_board)

    game = Game(user, bot)

    game.start()

if __name__ == '__main__':
    main()