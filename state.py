# coding=utf-8
"""
State module : specifies mower position and orientation
"""


class State:
    """
    State Class
    info relative to position, orientation and lawn boundaries
    """

    def __init__(self,
                 x: int = None,
                 y: int = None,
                 orientation: str = None,
                 x_max: int = None,
                 y_max: int = None,
                 x_min: int = 0,
                 y_min: int = 0,
                 ):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def __repr__(self):
        output = str(self.x) + str(self.y)
        output += self.orientation
        return output

    def is_on_lawn(self) -> bool:
        """
        checks if current state lays on the lawn
        :param:
        :return bool:
        """
        if not self.x_min <= self.x <= self.x_max:
            return False
        if not self.y_min <= self.y <= self.y_max:
            return False
        return True
