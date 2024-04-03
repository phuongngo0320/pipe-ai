from enum import Enum

class Shape(Enum):
    DEADEND = 0
    STRAIGHT = 1
    CORNER = 2
    TJOIN = 3