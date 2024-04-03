from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

def toRight(dir):
    if dir == Direction.UP:
        return Direction.RIGHT
    if dir == Direction.RIGHT:
        return Direction.DOWN
    if dir == Direction.DOWN:
        return Direction.LEFT
    if dir == Direction.LEFT:
        return Direction.UP

def flip(dir):
    if dir == Direction.UP:
        return Direction.DOWN
    if dir == Direction.RIGHT:
        return Direction.LEFT
    if dir == Direction.DOWN:
        return Direction.UP
    if dir == Direction.LEFT:
        return Direction.RIGHT
    
def toLeft(dir):
    if dir == Direction.UP:
        return Direction.LEFT
    if dir == Direction.RIGHT:
        return Direction.UP
    if dir == Direction.DOWN:
        return Direction.RIGHT
    if dir == Direction.LEFT:
        return Direction.DOWN

