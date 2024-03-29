from .Game.Game import Game
from .game_engine import Board
from .game_engine import UP, DOWN, LEFT, RIGHT, UNDO, INPLACE
from .utils import Colors
import pygame as pg


class Py2048(Game):

    WIDTH = 900
    HEIGTH = WIDTH

    def __init__(self, board_size=4) -> None:
        super().__init__()
        self.board_size = board_size
        self.title = r'2048'
        self.size = (self.WIDTH, self.HEIGTH)
        self.fps = 60
        self.over = False
        self.color = Colors()
        self.board = Board(self.board_size)
        self.BOX_PAD = self.WIDTH / self.board_size / 10
        self.BOX = (self.WIDTH - self.BOX_PAD) / self.board_size
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
        result = self.board.move(move_dir)
        self.over = not self.board.available()
        return result

    def reset(self):
        self.over = False
        self.board.reset()

    def onRender(self) -> None:
        self.window.fill(self.color.BG)
        self.draw_board()
        if self.over:
            self.draw_end_screen()

    def draw_board(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                tile_value = self.board[i, j]
                position = [self.BOX_PAD + self.BOX * j, self.BOX_PAD + self.BOX * i]
                pg.draw.rect(self.window, self.color[tile_value],
                             pg.Rect(*position, self.BOX - self.BOX_PAD, self.BOX - self.BOX_PAD),
                             0, 7)
                if tile_value != 0:
                    if tile_value < 4096:
                        txt = self.font.render(str(tile_value), 1, (0, 0, 0))
                    else:
                        txt = self.font.render(str(tile_value), 1, (255, 255, 255))
                    self.window.blit(txt, [position[0] + (self.BOX - self.BOX_PAD) // 2 - txt.get_width() // 2, position[1] + (self.BOX - self.BOX_PAD) // 2 - txt.get_height() // 2])

    def draw_end_screen(self):
        surf = pg.Surface((self.WIDTH, self.HEIGTH))
        surf.set_alpha(200)
        surf.fill(pg.Color(0, 0, 0))
        self.window.blit(surf, (0, 0))
        txt = self.font2.render('GAME OVER', 1, (0, 0, 0), (255, 0, 0))
        self.window.blit(txt, [self.WIDTH // 2 - txt.get_width() // 2,
                               self.HEIGTH // 2 - txt.get_height() // 2])
