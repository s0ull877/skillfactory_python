from exceptions import InvalidCoordinatesException

class Dot:

    _x: int
    _y: int
    # в зависимости от данный параметров будет выполнен принт на доске
    status: str 
    
    
    def __init__(self, x, y, status=None):
        """
        def __init__(self, x, y, status=None):
        status = 'strike' or 'miss' or 'ship'
        """

        self.x = y
        self.y = x
        self.status = status



    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __str__(self):

        # если корабаль подбит 
        if self.status == 'strike':
            return 'X |'

        # промах 
        if self.status == 'miss':
            return 'T |'

        # корабль 
        if self.status == 'ship':
            return '■ |'

        # обычная точка 
        return 'O |'

    # для дебага 
    def __repr__(self):
        return f'[{self.x}:{self.y}:{self.status}]'
    

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):

        if value not in range(0,6):

            raise InvalidCoordinatesException(f'\nНеверные координаты для x: {value}!\nВы вышли за пределы поля!')

        self._x = value

        
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):

        if value not in range(0,6):

            raise InvalidCoordinatesException(f'\nНеверные координаты для y: {value}!\nВы вышли за пределы поля!')

        self._y = value


