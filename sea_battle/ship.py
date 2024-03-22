from dot import Dot
from exceptions import InvalidCoordinatesException, InvalidRouteException

class Ship:

    lenght: int
    start: Dot
    _route: str
    hp = int

    def __init__(self, lenght, start, route):
        
        self.lenght = lenght
        self.start = start
        self._route = route
        self.hp = lenght


    # для дебага
    def __repr__(self):
        resp = ''

        resp = f"{self.dots} | {self.hp}"

        return resp


    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, value):

        if value in ['x','X','х','Х']:
            self._route = 'x'

        elif value in ['y','Y','y','Y']:
            self._route = 'y'

        else:
            raise InvalidRouteException(f'Недопустимое значение: {value}!')


    @property
    def dots(self) -> list:

        dot_list = []
        dot = Dot(self.start.x,self.start.y)

        if self.route == 'x':

            for i in range(0, self.lenght):


                dot_list.append(Dot(dot.x,dot.y, status='ship'))

                if i != self.lenght - 1:
                    dot.x += 1


        elif self.route == 'y':

            for i in range(0, self.lenght):
                
                dot_list.append(Dot(dot.x,dot.y, status='ship'))

                if i != self.lenght - 1:
                    dot.y += 1

        return dot_list

    
    @property
    def ship_countour(self) -> list:

        contour_list = []

        for dot in self.dots:

            for x in range(-1,2):
                for y in range(-1,2):

                    try:
                        countour = Dot(dot.y + y, dot.x + x)

                        if countour not in contour_list and countour not in self.dots:

                            countour.status = 'miss'
                            contour_list.append(countour)

                        if countour not in contour_list and countour in self.dots:

                            countour.status = 'strike'
                            contour_list.append(countour)

                    except InvalidCoordinatesException:
                        pass

        return contour_list


