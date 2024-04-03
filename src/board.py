from copy import deepcopy
from src.cell import Cell
from src.direction import Direction
import src.symbol as sym

class Board:
    
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

        self.map: list[list[Cell]] = [
            [ 
                None
                for j in range(width)
            ]
            for i in range(height)
        ]
        
        self.rotate_count = [
            [
                0
                for j in range(width)
            ]
            for i in range(height)
        ]
        
        self.connected_cells = set()
        self.populate()
        
    def populate(self):
        # TODO: generate input
        pass
        
    def out_of_board(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            return False
        return True
    
    def at(self, row, col) -> Cell:
        return self.map[row][col]
    
    def rotate_count_at(self, row, col):
        return self.rotate_count[row][col]
    
    def connected(self, pos1: tuple, pos2: tuple):
        
        r1, c1 = pos1
        r2, c2 = pos2
        ep1 = self.at(r1, c1).endpoints()
        ep2 = self.at(r2, c2).endpoints()
        
        if r1 == r2 and c1 + 1 == c2: 
            # [1] [2]
            return (Direction.RIGHT in ep1) and (Direction.LEFT in ep2)
        
        if r1 == r2 and c1 == c2 + 1:
            # [2] [1]
            return (Direction.LEFT in ep1) and (Direction.RIGHT in ep2)
        
        if c1 == c2 and r1 + 1 == r2:
            # [1]
            # [2]
            return (Direction.DOWN in ep1) and (Direction.UP in ep2)
        
        if c1 == c2 and r1 == r2 + 1:
            # [2]
            # [1]
            return (Direction.UP in ep1) and (Direction.DOWN in ep2)
        
        raise Exception("Unexpected Error: not adjacent")
        
    def rotate(self, r, c):
        
        board = deepcopy(self)
        board.map[r][c].rotate()
        board.rotate_count[r][c] += 1
        
        # check if it is fully connected
        conn = True
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            
            if self.out_of_board(r + dr, c + dc):
                continue
            
            # check for connection between two adjacent cells
            if not self.connected((r, c), (r + dr, c + dc)):
                conn = False
                
        if conn:
            self.connected_cells.add((r, c))
        else:
            if (r, c) in self.connected_cells:
                self.connected_cells.remove((r, c))
        
        return board        
        
    def __repr__(self) -> str:
        
        return '\n'.join([
            sym.symbol_row([
                cell.toSymbol()
                for cell in self.map[row]   
            ])
            for row in range(self.height)
        ])
            
            