from src.shape import Shape
from src.direction import Direction, flip, toLeft, toRight
import src.symbol as sym

class Cell:
    
    def __init__(self, shape, direction, valve: bool = False) -> None:
        self.shape = shape
        self.direction = direction
        self.valve = valve
        
    def rotate(self, right = True):
        
        if right:
            self.direction = toRight(self.direction)
        else:
            self.direction = toLeft(self.direction)
    
    def endpoints(self) -> list[Direction]:
        
        if self.shape == Shape.DEADEND:
            return [self.direction]
        
        if self.shape == Shape.STRAIGHT:
            return [self.direction, flip(self.direction)]
            
        if self.shape == Shape.CORNER:
            return [self.direction, toRight(self.direction)]
        
        if self.shape == Shape.TJOIN:
            return [self.direction, toLeft(self.direction), toRight(self.direction)]
        
    def toSymbol(self):
        
        if self.shape == Shape.DEADEND:
            if self.direction == Direction.UP:
                return sym.DEADEND_UP
            if self.direction == Direction.DOWN:
                return sym.DEADEND_DOWN
            if self.direction == Direction.LEFT:
                return sym.DEADEND_LEFT
            if self.direction == Direction.RIGHT:
                return sym.DEADEND_RIGHT
            
        if self.shape == Shape.STRAIGHT:
            if self.direction in [Direction.UP, Direction.DOWN]:
                return sym.STRAIGHT_VERTICAL
            if self.direction in [Direction.LEFT, Direction.RIGHT]:
                return sym.STRAIGHT_HORIZONTAL
            
        if self.shape == Shape.CORNER:
            if self.direction == Direction.UP:
                return sym.CORNER_UP
            if self.direction == Direction.DOWN:
                return sym.CORNER_DOWN
            if self.direction == Direction.LEFT:
                return sym.CORNER_LEFT
            if self.direction == Direction.RIGHT:
                return sym.CORNER_RIGHT
            
        if self.shape == Shape.TJOIN:
            if self.direction == Direction.UP:
                return sym.TJOIN_UP
            if self.direction == Direction.DOWN:
                return sym.TJOIN_DOWN
            if self.direction == Direction.LEFT:
                return sym.TJOIN_LEFT
            if self.direction == Direction.RIGHT:
                return sym.TJOIN_RIGHT
            
    def __repr__(self) -> str:
        symbol = self.toSymbol()
        return '\n'.join(symbol)
                
            