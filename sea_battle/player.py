import os
import time
import random

from dot import Dot
from ship import Ship
from board import Board

from consts import RULES

from exceptions import InvalidCoordinatesException, CoordinatesIsBusyException, InvalidRouteException



class AbstractPlayer:

    self_board: Board
    enemy_board: Board

    def __init__(self):
        pass


    def get_coordinates(self):

        dot = Dot(0,0)

        while True:

            try:

                dot.x = ...
                dot.y = ...

            except ValueError:
                ...

            except InvalidCoordinatesException as ex:
                ...

            else:

                return dot


    def move(self):

        additional_move = True

        while additional_move:

            x,y = self.get_coordinates()
        
        try:
            additional_move = self.enemy_board.on_shot(current_dot)

        except CoordinatesIsBusyException as ex:
            ...


    def fill_with_ships(self):
        pass



# класс Юзера
class Player(AbstractPlayer):

    self_board: Board
    enemy_board: Board

    def __init__(self,self_board:Board, enemy_board: Board):

        self.self_board = self_board
        self.enemy_board = enemy_board


    def get_coordinates(self) -> Dot:

        dot = Dot(0,0)

        while True:

            try:
                dot.y = int(input('Введите координату x: '))
                dot.x = int(input('Введите координату y: '))

            except ValueError:

                print('Значение должно быть числом!')
                time.sleep(2)
            
            except InvalidCoordinatesException as ex:

                print(ex)
                time.sleep(2)

            else:

                return dot


    # функция хода 
    def move(self) -> None:

        # нужен ли дополнительных ход
        additional_move = True

                                #  если кораблей больше нет, то и ходить не нужно
        while additional_move and self.enemy_board._alife_ships:

            current_dot = self.get_coordinates()

            try:
                additional_move = self.enemy_board.on_shot(current_dot)
                time.sleep(1)

            except CoordinatesIsBusyException as ex:
                
                additional_move = True
                print(ex)
                time.sleep(2)

            finally:
                os.system('cls')
                print('ДОСКА БОТА:')
                self.enemy_board.show_board()
                print('ВАША ДОСКА:')
                self.self_board.show_board()



    # заполнение доски кораблями
    def fill_with_ships(self) -> None:

        ships_count = {'big': 1, 'mid': 2, 'tin': 4}

        ship_leng = {'big': 3, 'mid': 2, 'tin': 1}

        while ships_count['big'] or ships_count['mid'] or ships_count['tin']:

            os.system('cls')
            
            # правила, состояние доски и панель выбора 
            print(RULES, '\n')
            self.self_board.show_board()
            print(
'\nbig | трехпалубный: осталось {}\n\
mid | двухпалобный: осталось {}\n\
tin | однопалубный корабль: осталось {}\n'.format(*list(ships_count.values()))
)

            answer = input('Выберите какой корабль хотите поставить(big/mid/tin): ')

            # для сброса состояния доски
            if answer == 'reset':
                
                ships_count = {'big': 1, 'mid': 2, 'tin': 4}
                self.self_board._board = self.self_board.create_board()
                self.self_board.ships = []
                self.self_board._busy_dots = []
                self.self_board._alife_ships = 0

                continue


            try:
                # если человек захочет поставить больше кораблей, чем нужно
                if ships_count[answer] == 0:

                    print('У вас не осталось данных кораблей!')
                    time.sleep(1)
                    continue

            # при невалидном ответе выпадет ошибка
            except KeyError:
                print('Нет такого варинта ответа!')
                time.sleep(1)
                continue

            # блок конструктора корабял
            print('\nДавайте выберем стартовую точку корабля.')
            
            ship_start_dot = self.get_coordinates()
            self.self_board.show_board()

            try:

                route = input('Выберите направление корабля вертикальное(напишите y) или горизонтальное(x): ')
                ship = Ship(lenght=ship_leng[answer],start=ship_start_dot,route=route)

            except InvalidRouteException as ex:

                print(ex)
                time.sleep(2)
                continue
                

            try:

                self.self_board.add_ship(ship)
                # при правильном конструкторе убавляю колво кораблей
                ships_count[answer] -= 1
            
            except Exception as ex:
                print(ex)
                time.sleep(2)


            



# класс Бота
class BotPlayer(AbstractPlayer):

    self_board: Board
    enemy_board: Board

    def __init__(self,self_board: Board ,enemy_board: Board):

        self.self_board = self_board
        self.enemy_board = enemy_board


    def get_coordinates(self) -> Dot:

        dot = Dot(0,0)

        dot.y = random.randint(0,5)
        dot.x = random.randint(0,5)

        return dot
            


    def move(self) -> bool:

        os.system('cls')
        additional_move = True
        print("Бот:")

        while additional_move and self.enemy_board._alife_ships:

            current_dot = self.get_coordinates()

            try:
                additional_move = self.enemy_board.on_shot(current_dot)
                time.sleep(1)

            except CoordinatesIsBusyException as ex:
                
                additional_move = True

        # блок вывода информации, для вывода актульного состояния игровых досок
        print('ДОСКА БОТА:')
        self.self_board.show_board()
        print('ВАША ДОСКА:')
        self.enemy_board.show_board()




    def fill_with_ships(self) -> None:
        # суть функции в том, что при прохождении 1 итерации без ошибок из списка pop`ается корабль,
        # при какой-лтбо ошибке я возвращаю корабль обратно в начало и так, пока список не станет пустой
        ships = ['big', 'mid', 'mid', 'tin', 'tin', 'tin', 'tin']

        ship_leng = {'big': 3, 'mid': 2, 'tin': 1}

        while ships:


            answer = ships.pop(0)

            # если не останется места для корабял
            if answer == 'tin' and len(self.self_board._busy_dots) == 36:
                
                ships = ['big', 'mid', 'mid', 'tin', 'tin', 'tin', 'tin']
                self.self_board._board = self.self_board.create_board()
                self.self_board._busy_dots = []
                self.self_board.ships = []
                continue



            ship_start_dot = self.get_coordinates()

            try:

                route = random.choice(['x', 'y'])
                ship = Ship(lenght=ship_leng[answer],start=ship_start_dot,route=route)

            except InvalidRouteException as ex:
                
                ships.insert(0, answer)
                continue

            try:

                self.self_board.add_ship(ship)

            except CoordinatesIsBusyException:
                ships.insert(0, answer)

            except InvalidCoordinatesException:
                ships.insert(0, answer)


        # имеется ошибка с рандомный значением данного аргумента,
        # рлэтому рещил просто указать, что кораблей 7
        self.self_board._alife_ships = 7  

        self.self_board.show_board()



    #! Для тестов, чтобы самому не заполнять доску
    # def _create_test_board(self):

    #     board = Board(hid=False)

    #     ships = ['big', 'mid', 'mid', 'tin', 'tin', 'tin', 'tin']

    #     ship_leng = {'big': 3, 'mid': 2, 'tin': 1}

    #     while ships:


    #         answer = ships.pop(0)

    #         if answer == 'tin' and len(board._busy_dots) == 36:
                
    #             ships = ['big', 'mid', 'mid', 'tin', 'tin', 'tin', 'tin']
    #             board._board = board.create_board()
    #             board._busy_dots = []
    #             continue



    #         ship_start_dot = self.get_coordinates()

    #         try:

    #             route = random.choice(['x', 'y'])
    #             ship = Ship(lenght=ship_leng[answer],start=ship_start_dot,route=route)

    #         except InvalidRouteException as ex:
                
    #             ships.insert(0, answer)
    #             continue

    #         try:

    #             board.add_ship(ship)

    #         except Exception as ex:

    #             ships.insert(0, answer)

    #     return board