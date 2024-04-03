from typing import Callable, Type
from src.board import Board

class PipePuzzle:
    """Game-playing modeling
    - State to be used is required to have a `to_move` attribute (may also have `utility` for algo)
    """
    
    def __init__(self, initial: Board) -> None:
        self.initial = initial
        self.width = initial.width
        self.height = initial.height
    
    def actions(self, state: Board):
        """The set of legal moves in `state`"""
        moves = set()
        for row in range(self.height):
            for col in range(self.width):
                if state.rotate_count_at(row, col) < 3:
                    moves.add((row, col))
                    
        return list(moves)
    
    def result(self, state: Board, move):
        """The transition model, which defines the state resulting from taking action `move` in `state`"""
        return state.rotate(*move)
    
    def is_terminal(self, state: Board):
        """A terminal test, which is true when the game is over and false Terminal test otherwise."""
        return len(state.connected_cells) == state.width * state.height
    
    def utility(self, state, player):
        """A utility function (also called an objective function or payoff function), which defines the final numeric value to `player` when the game ends in terminal `state`."""
        raise NotImplementedError
    
    def __repr__(self) -> str:
        return '<{}>'.format(self.__class__.__name__)
    
    def play(self, strategy: Callable[['PipePuzzle', Board], tuple], verbose = False):
        
        state = self.initial
        while not self.is_terminal(state):
            move = strategy(self, state)
            if verbose:
                print("Move: " + str(move))
                print(state)
        return state