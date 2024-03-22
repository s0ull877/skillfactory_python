class InvalidCoordinatesException(Exception):

    message: str

    def __init__(self, message=None):

        self.message = message
        super().__init__(message)


class CoordinatesIsBusyException(Exception):
    
    message: str

    def __init__(self, message=None):

        self.message = message
        super().__init__(message)


class InvalidRouteException(Exception):

    message: str

    def __init__(self, message=None):

        self.message = message
        super().__init__(message)
