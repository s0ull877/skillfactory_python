import time
from dot import Dot
from ship import Ship
from exceptions import CoordinatesIsBusyException

class Board:

    ships: list
    _board: list
    hid: bool
    _alife_ships: int 
    _busy_dots: list


    def __init__(self, hid):

        self.hid = hid
        self.ships = []
        self._board = self.create_board()
        self._alife_ships = 0
        self._busy_dots = []

    # показывает состояние доски на поле
    def show_board(self) -> None:

        print('  | 0 | 1 | 2 | 3 | 4 | 5 | x')

        if  not self.hid:

            for i in range(0,6):
            
                row = self._board[i]
                print(f'{i} |', *row)

        # если доска опонента то прячем корабли
        else:

            for i in range(0,6):
            
                row = self._board[i]
                row = [str(dot) for dot in row]
                print(f'{i} |', ' '.join(row).replace('■', 'O'))
            
        print("y")


    # создает стартовую пустую доску
    def create_board(self) -> list:

        board = []

        for x in range(0,6):
            row = []
            
            for y in range(0,6):

                dot = Dot(x, y)
                
                row.append(Dot(x, y))

            board.append(row)

        return board


    def add_ship(self, ship: Ship) -> None:

        for ship_dot in ship.dots:

            if ship_dot in self._busy_dots: 

                raise CoordinatesIsBusyException('\nВы не можете ставить корабли так близко!')

        self._append_ship(ship)
        self._append_busy_dots(ship)


    # перед добавлением корабля, меняю доску в актуальное положение 
    def _append_ship(self,ship: Ship) -> None:

        for dot in ship.dots:

            self._board[dot.x][dot.y] = dot

        self._alife_ships += 1
        self.ships.append(ship)


    # и вместе с функцией выше, обновляю занятые координаты
    def _append_busy_dots(self, ship) -> None:

        for busy_dot in ship.ship_countour:
            if busy_dot not in self._busy_dots:
                self._busy_dots.append(busy_dot)


    # выстрел по доске, возвращает True, если дозволен еще один выстрел
    def on_shot(self, dot: Dot) -> bool:

        current_dot = self._board[dot.x][dot.y]

        if current_dot.status is None:

            self._board[dot.x][dot.y] = Dot(dot.x, dot.y, status='miss')
            print(f"Промах! По координатам x: {dot.y} y: {dot.x}")
            return False
        
        # при выстреле в одну и ту же точку
        if current_dot.status == 'miss' or current_dot.status == 'strike':
            
            raise CoordinatesIsBusyException(f'\nВы не можете стрелять в эту точку x:{dot.y} y:{dot.x}!')

        if current_dot.status == 'ship':
            self.shot_to_ship(current_dot)
            self._board[dot.x][dot.y] = Dot(dot.x, dot.y, status='strike')
            return True


    #  проверка состояния корабля
    def shot_to_ship(self, dot:Dot) -> None:


        for i in range(0, len(self.ships)):
            
            # если выстрел убил корабль
            if dot in self.ships[i].dots and self.ships[i].hp == 1:
            
                ship = self.ships.pop(i)
                self._alife_ships -= 1

                for dead_dot in ship.ship_countour:
                    self._board[dead_dot.x][dead_dot.y] = dead_dot

                print(f'Убил! По координатам x: {dot.y} y: {dot.x}')            
                break
            
            # если выстрел попал в корабль, но не убил
            elif dot in self.ships[i].dots:
                print(f"Попадание! По координатам x: {dot.y} y: {dot.x}")
                self.ships[i].hp -= 1
                break
            
