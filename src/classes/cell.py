import pygame
from .symbol import Symbol
from constant.digit import *


class Cell:
    """
    Represents a cell.

    Instance Variables:
        SIZE(int): Unit size.
        surf(Surface): Surface that represents the cell visually.
        val(int): Value to be shown on the cell, i.e. what digit the cell is currently.
        background_color(Color): Background color.
        number_color: Color of the digit.

    Methods:
        set_color: Sets the color attributes of the cell.
        display: Renders the cell (and the digit).

    """

    def __init__(self, size):
        self.SIZE = size
        self.surf = pygame.Surface((9 * self.SIZE, 9 * self.SIZE))
        self.val = 0

    def set_color(self, background_color, number_color):
        self.background_color = background_color
        self.number_color = number_color

    def display(self):
        self.surf.fill(self.background_color)

        if self.val != 0:
            symbol = Symbol(self.SIZE, DIGITS[self.val])
            symbol.set_color(self.background_color, self.number_color)
            self.surf.blit(symbol.display(), (0, 0))

        return self.surf
