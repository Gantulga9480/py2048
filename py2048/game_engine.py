import numpy as np
import random

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
UNDO = 4  # Experimantal
ACTION_SPACE = 5  # 5 for +UNDO
INPLACE = 5  # For animation


class Board:

    ODDS = 0.1     # odds to generate 4 instead of 2
    START_BOX = 3  # Boxes to generate at start

    def __init__(self, size) -> None:
        self.size = size
        self.board = None
        self.last_board = None
        self.score = 0
        self.reset()

    def __repr__(self) -> str:
        rep_str = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(str(self.board[i][j]))
            rep_str.append(' '.join(row))
        return '\n'.join(rep_str)

    def __getitem__(self, indices):
        return self.board[indices]

    def __setitem__(self, indices, new_value):
        self.board[indices] = new_value

    def reset(self):
        self.last_board = None
        self.score = 0
        board_list = []
        for _ in range(self.size):
            board_list.append([0 for _ in range(self.size)])
        self.board = np.array(board_list)
        for _ in range(self.START_BOX):
            self.generate()

    def set(self, board: np.ndarray):
        if not isinstance(board, np.ndarray):
            raise TypeError(f"Expected 'numpy.ndarray', got {type(board)}")
        if board.shape != self.board.shape:
            raise AttributeError(f"Input shape of {board.shape} does not match shape {self.board.shape}")
        self.board = board.copy()

    def set_all(self, board: 'Board'):
        if not isinstance(board, Board):
            raise TypeError(f"Expected 'Board', got {type(board)}")
        self.set(board.get())
        self.score = board.score
        if board.last_board is not None:
            self.last_board = Board(board.size)
            self.last_board.set(board.last_board.get())
            self.last_board.score = board.last_board.score
        else:
            self.last_board = None

    def get(self) -> np.ndarray:
        board = np.zeros((self.size, self.size), dtype=np.int32)
        for i in range(self.size):
            for j in range(self.size):
                board[i, j] = self.board[i, j]
        return board

    def generate(self) -> int:
        empty_boxes = self.get_empty()
        if empty_boxes.__len__() > 0:
            pos = random.choice(empty_boxes)
            prob = random.random()
            if prob <= self.ODDS:
                self.board[pos] = 4
            else:
                self.board[pos] = 2
            return self.board[pos]
        return 0

    def get_empty(self) -> list:
        empty_box = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i, j] == 0:
                    empty_box.append((i, j))
        return empty_box

    def is_full(self) -> bool:
        empty_boxes = self.get_empty()
        if empty_boxes.__len__() > 0:
            return False
        else:
            return True

    def available(self):
        if self.board[self.size - 1][self.size - 1] == 0:
            return True
        for i in range(self.size - 1):
            for j in range(self.size):
                if self.board[i][j] == self.board[i + 1][j] or self.board[i][j] == 0:
                    return True
                if self.board[j][i] == self.board[j][i + 1] or self.board[j][i] == 0:
                    return True
        return False

    def move(self, move_dir: int) -> bool:
        result = False
        if move_dir == UP:
            result = self.up()
        elif move_dir == DOWN:
            result = self.down()
        elif move_dir == LEFT:
            result = self.left()
        elif move_dir == RIGHT:
            result = self.right()
        else:
            raise ValueError("Undefined move direction given")
        return result

    def up(self) -> bool:
        self.board = np.rot90(self.board, 2)
        local_score = self.__compute()
        self.board = np.rot90(self.board, 2)
        return self.__end_move(local_score)

    def down(self) -> bool:
        local_score = self.__compute()
        return self.__end_move(local_score)

    def left(self) -> bool:
        self.board = np.rot90(self.board, 1)
        local_score = self.__compute()
        self.board = np.rot90(self.board, 3)
        return self.__end_move(local_score)

    def right(self) -> bool:
        self.board = np.rot90(self.board, 3)
        local_score = self.__compute()
        self.board = np.rot90(self.board, 1)
        return self.__end_move(local_score)

    def __compute(self) -> int:
        score = -1
        for col_idx in range(self.size):
            last_summed = False
            for row_idx in range(self.size - 2, -1, -1):
                diff = self.size - 1 - row_idx
                new_j = row_idx
                for _ in range(diff):
                    current_tile_value = self.board[new_j][col_idx]
                    new_j += 1
                    next_tile_value = self.board[new_j][col_idx]
                    if current_tile_value > 0:
                        if (next_tile_value == 0) or ((next_tile_value == current_tile_value) and not last_summed):
                            self.board[new_j][col_idx] += current_tile_value  # set new tile value
                            self.board[new_j - 1][col_idx] = 0                # clear current tile value
                            if next_tile_value > 0:
                                if score < 0:
                                    score = 0
                                score += next_tile_value * 2
                                last_summed = True                            # block next tile sum check
                                break
                            if score < 0:
                                score = 0
                        else:
                            last_summed = False  # if stuck unblock next tile and break
                            break
        return score

    def __end_move(self, local_score) -> bool:
        if local_score < 0:
            return False
        gen_score = self.generate()
        self.score += gen_score
        self.score += local_score
        return True
