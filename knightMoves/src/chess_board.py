from string import ascii_uppercase
from random import randrange


class Coordinates():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y

    def is_in_range(self):
        return bool(self.x in range(5) and self.y in range(5))

    def __add__(self, add_coords):
        return Coordinates(self.x + add_coords.x, self.y + add_coords.y)

    def __repr__(self):
        return f"({self._x}, {self._y})"


KNIGHT_MOVES = [
    Coordinates(2, 1),
    Coordinates(2, -1),
    Coordinates(-2, 1),
    Coordinates(-2, -1),
    Coordinates(1, 2),
    Coordinates(1, -2),
    Coordinates(-1, 2),
    Coordinates(-1, -2)
]


class Node():
    def __init__(self, symbol, coords, board):
        self.parent = None
        self.coords = coords
        self.symbol = symbol
        self.board = board

    def is_empty(self):
        return self.symbol == ' '

    def adopt_node(self, node):
        node.parent = self

    def generation_count(self):
        return len(self.get_lineage())

    def get_lineage(self):  # This includes itself
        parent_node = self.parent
        lineage = [self.coords]

        while parent_node:
            lineage.append(parent_node)
            parent_node = parent_node.parent

        return lineage

    def __repr__(self):
        return self.symbol


class ChessBoard():
    def __init__(self):
        self.board = []
        self.create_board()
        self.find_potential_moves()

    def create_board(self):
        count = 0
        for row in range(5):
            self.board.append([])
            for col in range(5):
                if(ascii_uppercase[count] in ['D', 'F', 'X', 'Y']):
                    cell_char = ' '
                else:
                    cell_char = ascii_uppercase[count]
                self.board[row].append(Node(cell_char, Coordinates(row, col), self))
                count += 1

    def find_potential_moves(self):
        for row in self.board:
            for node in row:
                possible_moves = []
                for move in KNIGHT_MOVES:
                    coords = node.coords + move
                    if coords.is_in_range() and not self.get_node(coords).is_empty():
                        possible_moves.append(coords)

                node.potential_moves = possible_moves
                print(f"POSSIBLE MOVES FOR {node}: {node.potential_moves}")

    def get_node(self, coords):
        return self.board[coords.x][coords.y]

    def solve_matrix(self, node):
        print(f"\nENTERING SOLVE MATRIX {node.coords}\n----------------------")
        print(f"POTENTIAL MOVES: {node.potential_moves}")

        starting_node = node

    def print_board(self):
        for row in self.board:
            for col in row:
                print('[ ' + str(col) + ' ]', sep='\t', end='')
            print()


if __name__ == '__main__':
    start_coords = None
    my_board = ChessBoard()
    my_board.print_board()
    start_pos = ' '

    while start_pos == ' ':
        start_coords = Coordinates(randrange(0, 5), randrange(0, 5))
        start_pos = str(my_board.board[start_coords.x][start_coords.y])

    starting_node = my_board.get_node(start_coords)
    print(f"STARTING POINT: {starting_node.symbol} {start_coords}")

    my_board.solve_matrix(starting_node)
