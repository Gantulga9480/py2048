from .Game.Game import Game
from .game_engine import Board
from .game_engine import UP, DOWN, LEFT, RIGHT, UNDO, INPLACE
from .utils import Colors
import pygame as pg


class Py2048(Game):

    WIDTH = 900
    HEIGTH = WIDTH
    BOARD_SIZE = 4

    def __init__(self) -> None:
        super().__init__()
        self.title = r'2048'
        self.size = (self.WIDTH, self.HEIGTH)
        self.fps = 60
        self.over = False
        self.color = Colors()
        self.game_board = Board(self.BOARD_SIZE)
        self.BOX_PAD = self.WIDTH / self.BOARD_SIZE / 10
        self.BOX = (self.WIDTH - self.BOX_PAD) / self.BOARD_SIZE
        self.font = pg.font.SysFont("arial", int(self.BOX // 2), True)
        self.font2 = pg.font.SysFont("arial", 150, True)

    def onEvent(self, event) -> None:
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.step(UP)
            elif event.key == pg.K_DOWN:
                self.step(DOWN)
            elif event.key == pg.K_LEFT:
                self.step(LEFT)
            elif event.key == pg.K_RIGHT:
                self.step(RIGHT)
            elif event.key == pg.K_u:
                self.step(UNDO)
            elif event.key == pg.K_r:
                self.reset()

    def step(self, move_dir):
        result = self.game_board.move(move_dir)
        self.over = not self.game_board.available()
        return result

    def reset(self):
        self.over = False
        self.game_board.reset()

    def onRender(self) -> None:
        self.window.fill(self.color.BG)
        self.draw_board()
        if self.over:
            self.draw_end_screen()

    def draw_board(self):
        for i in range(self.game_board.size):
            for j in range(self.game_board.size):
                node_value = self.game_board[i, j]
                position = [self.BOX_PAD + self.BOX * j, self.BOX_PAD + self.BOX * i]
                pg.draw.rect(self.window, self.color[node_value],
                             pg.Rect(*position, self.BOX - self.BOX_PAD, self.BOX - self.BOX_PAD),
                             0, 7)
                if node_value != 0:
                    if node_value < 4096:
                        txt = self.font.render(str(node_value), 1, (0, 0, 0))
                    else:
                        txt = self.font.render(str(node_value), 1, (255, 255, 255))
                    self.window.blit(txt, [position[0] + (self.BOX - self.BOX_PAD) // 2 - txt.get_width() // 2, position[1] + (self.BOX - self.BOX_PAD) // 2 - txt.get_height() // 2])

    def draw_end_screen(self):
        surf = pg.Surface((self.WIDTH, self.HEIGTH))
        surf.set_alpha(200)
        surf.fill(pg.Color(0, 0, 0))
        self.window.blit(surf, (0, 0))
        txt = self.font2.render('GAME OVER', 1, (0, 0, 0), (255, 0, 0))
        self.window.blit(txt, [self.WIDTH // 2 - txt.get_width() // 2,
                               self.HEIGTH // 2 - txt.get_height() // 2])
