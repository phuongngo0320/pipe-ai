from src.board import Board
from src.cell import Cell
from src.direction import Direction
from src.shape import Shape
import src.symbol as sym

board = Board(2, 2)
board.map[0][0] = Cell(Shape.CORNER, Direction.RIGHT)
board.map[0][1] = Cell(Shape.CORNER, Direction.DOWN)
board.map[1][0] = Cell(Shape.CORNER, Direction.UP)
board.map[1][1] = Cell(Shape.CORNER, Direction.LEFT)
print(board)