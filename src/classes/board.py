import pygame
import math
from .cell import Cell
from .rect import Rect


class Board:
    """
    Represents the board.

    Instance Variables:
        SIZE(int): Unit size.
        BOARD_WIDTH(int): Width and height of the board.
        surf(Surface): Surface that represents the board visually.
        current_selection(tuple): Location of the cell is currently selected by the player.
        board(list): 2D array of cells.
        background_color(Color): Background color.
        thin_color(Color): Color of thin separating lines.
        thick_color(Color): Color of thick separating lines.
        highlight_color(Color): Color of selector.
        game_digit_color(Color): Color of default numbers.
        user_digit_color(Color): Color of user input numbers.

    Methods:
        set_color: Sets of the color of the board.
        set_up: Draw grid lines.
        display: Displays everything on the board (grid lines, selector, digits).
        import_game: Import 2D array of predefined digits in each cell.
        clear_board: Clear digits from cells.
        user_move: Updates the board to what digit the user entered.
        display_highligh_selection: Display selector.
        remove_highligh_selection: Remove selector from display.
        non_valid_vals: Non-valid values for selected cell.
        delete_cell: Delete user input from selected cell.
        reset: Rests all user inputs.
    """

    def __init__(self, size):

        self.SIZE = size
        self.BOARD_WIDTH = 95 * self.SIZE
        self.surf = pygame.Surface((self.BOARD_WIDTH, self.BOARD_WIDTH))
        self.current_selection = [0, 0]

        self.board = []
        for i in range(9):
            board_row = []
            for j in range(9):
                board_row.append(Cell(size))
            self.board.append(board_row)

    def set_color(self, background_color, thin_color, thick_color, highlight_color, game_digit_color, user_digit_color):
        self.background_color = background_color
        self.thin_color = thin_color
        self.thick_color = thick_color
        self.highlight_color = highlight_color
        self.game_digit_color = game_digit_color
        self.user_digit_color = user_digit_color

    def set_up(self):
        self.surf.fill(self.background_color)

        color = self.thick_color
        for i in range(4):
            rect = pygame.Rect(0,
                               i * 31 * self.SIZE,
                               self.BOARD_WIDTH,
                               2 * self.SIZE)
            self.surf.fill(color, rect)
            rect = pygame.Rect(i * 31 * self.SIZE,
                               0,
                               2 * self.SIZE,
                               self.BOARD_WIDTH)
            self.surf.fill(color, rect)

        color = self.thin_color
        for i in range(3):
            for j in range(3):
                for k in range(2):
                    rect = pygame.Rect(j * 29 * self.SIZE + (j + 1) * 2 * self.SIZE,
                                       i * 29 * self.SIZE + (i + 1) * 2 * self.SIZE + k * self.SIZE + (
                                                   k + 1) * 9 * self.SIZE,
                                       29 * self.SIZE,
                                       self.SIZE)
                    self.surf.fill(color, rect)
                    rect = pygame.Rect(
                        i * 29 * self.SIZE + (i + 1) * 2 * self.SIZE + k * self.SIZE + (k + 1) * 9 * self.SIZE,
                        j * 29 * self.SIZE + (j + 1) * 2 * self.SIZE,
                        self.SIZE,
                        29 * self.SIZE)
                    self.surf.fill(color, rect)

        return self.surf

    def display(self):
        self.set_up()
        self.clear_board()
        self.__display_game()
        self.display_highlight_selection()

        return self.surf

    def import_game(self, game):
        self.game = game

        self.clear_board()
        self.__display_game()

        for i in range(9):
            for j in range(9):
                self.board[i][j].val = self.game[i][j]

        return self.surf

    def clear_board(self):
        color = self.background_color
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        rect = pygame.Rect(j * 29 * self.SIZE + (j + 1) * 2 * self.SIZE + l * 10 * self.SIZE,
                                           i * 29 * self.SIZE + (i + 1) * 2 * self.SIZE + k * 10 * self.SIZE,
                                           9 * self.SIZE,
                                           9 * self.SIZE)
                        self.surf.fill(color, rect)

    def __display_game(self):
        background_color = self.background_color
        number_color_1 = self.game_digit_color
        number_color_2 = self.user_digit_color
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        (x, y) = (3 * i + k, 3 * j + l)
                        if self.game[x][y] != 0:
                            self.board[x][y].set_color(background_color, number_color_1)
                            self.board[x][y].val = self.game[x][y]
                            surf = self.board[x][y].display()
                            self.surf.blit(surf, (j * 29 * self.SIZE + (j + 1) * 2 * self.SIZE + l * 10 * self.SIZE,
                                                  i * 29 * self.SIZE + (i + 1) * 2 * self.SIZE + k * 10 * self.SIZE))
                        elif self.board[x][y].val != 0:
                            self.board[x][y].set_color(background_color, number_color_2)
                            surf = self.board[x][y].display()
                            self.surf.blit(surf, (j * 29 * self.SIZE + (j + 1) * 2 * self.SIZE + l * 10 * self.SIZE,
                                                  i * 29 * self.SIZE + (i + 1) * 2 * self.SIZE + k * 10 * self.SIZE))

    def user_move(self, num):
        background_color = self.background_color
        number_color = self.user_digit_color

        if self.game[self.current_selection[0]][self.current_selection[1]] == 0:
            (x, y) = (self.current_selection[0], self.current_selection[1])
            (i, k, j, l) = (
            int(self.current_selection[0] // 3), self.current_selection[0] % 3, int(self.current_selection[1] // 3),
            self.current_selection[1] % 3)
            self.board[x][y].set_color(background_color, number_color)
            self.board[x][y].val = num
            surf = self.board[x][y].display()
            self.surf.blit(surf, (j * 29 * self.SIZE + (j + 1) * 2 * self.SIZE + l * 10 * self.SIZE,
                                  i * 29 * self.SIZE + (i + 1) * 2 * self.SIZE + k * 10 * self.SIZE))

        return self.surf

    def display_highlight_selection(self):

        color = self.highlight_color
        (i, k, j, l) = (
        int(self.current_selection[0] // 3), self.current_selection[0] % 3, int(self.current_selection[1] // 3),
        self.current_selection[1] % 3)

        rect = Rect(int(math.ceil(self.SIZE / 2)),
                    j * 29 * self.SIZE + (j + 1) * 2 * self.SIZE + l * 10 * self.SIZE,
                    2 * self.SIZE,
                    9 * self.SIZE,
                    self.BOARD_WIDTH - 4 * self.SIZE)
        rect.set_color(color)
        rect.draw(self.surf)

        rect = Rect(int(math.ceil(self.SIZE / 2)),
                    2 * self.SIZE,
                    i * 29 * self.SIZE + (i + 1) * 2 * self.SIZE + k * 10 * self.SIZE,
                    self.BOARD_WIDTH - 4 * self.SIZE,
                    9 * self.SIZE)
        rect.set_color(color)
        rect.draw(self.surf)

        return self.surf

    def remove_highlight_selection(self):
        color = self.thick_color
        for i in range(4):
            rect = pygame.Rect(0,
                               i * 31 * self.SIZE,
                               self.BOARD_WIDTH,
                               2 * self.SIZE)
            self.surf.fill(color, rect)
            rect = pygame.Rect(i * 31 * self.SIZE,
                               0,
                               2 * self.SIZE,
                               self.BOARD_WIDTH)
            self.surf.fill(color, rect)

        color = self.thin_color
        for i in range(3):
            for j in range(3):
                for k in range(2):
                    rect = pygame.Rect(j * 29 * self.SIZE + (j + 1) * 2 * self.SIZE,
                                       i * 29 * self.SIZE + (i + 1) * 2 * self.SIZE + k * self.SIZE + (
                                                   k + 1) * 9 * self.SIZE,
                                       29 * self.SIZE,
                                       self.SIZE)
                    self.surf.fill(color, rect)
                    rect = pygame.Rect(
                        i * 29 * self.SIZE + (i + 1) * 2 * self.SIZE + k * self.SIZE + (k + 1) * 9 * self.SIZE,
                        j * 29 * self.SIZE + (j + 1) * 2 * self.SIZE,
                        self.SIZE,
                        29 * self.SIZE)
                    self.surf.fill(color, rect)

        return self.surf

    def non_valid_vals(self):
        non_valid_vals = set()
        (x, y) = (self.current_selection[0], self.current_selection[1])
        if self.game[x][y] == 0:
            for i in range(9):
                non_valid_vals.add(self.board[x][i].val)
                non_valid_vals.add(self.board[i][y].val)

            (a, b) = (int(x // 3), int(y // 3))
            for i in range(3):
                for j in range(3):
                    non_valid_vals.add(self.board[3 * a + i][3 * b + j].val)
        else:
            for i in range(1, 10):
                non_valid_vals.add(i)

        return non_valid_vals

    def delete_cell(self):
        (x, y) = (self.current_selection[0], self.current_selection[1])
        self.board[x][y].val = 0

        return self.non_valid_vals()

    def reset(self):
        for i in range(9):
            for j in range(9):
                if self.game[i][j] == 0:
                    self.board[i][j].val = 0
