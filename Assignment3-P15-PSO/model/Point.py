class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, other):
        self._x = other

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, other):
        self._y = other

    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ")"
