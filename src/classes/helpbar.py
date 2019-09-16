import pygame
from .symbol import Symbol
from .rect import Rect
from constant.digit import *


class HelpBar:
    """
    Represents the bar that gives hints.

    Instance Variables:
        SIZE(int): Unit size.
        disable: Should the help bar display anything?

    Methods:
        set_color: Sets the colors of the help bar.
        set_up: Draws the vertical and horizontal lines.
        user_move: Changes the numbers displayed for the new cell the user moved to.
    """

    def __init__(self, size):
        self.SIZE = size
        self.disable = False

        self.HELPBAR_LENGTH = 93 * size
        self.HELPBAR_WIDTH = 13 * size
        self.surf = pygame.Surface((self.HELPBAR_LENGTH, self.HELPBAR_WIDTH))

    def set_color(self, background_color, thin_color, thick_color, digit_color):
        self.background_color = background_color
        self.thin_color = thin_color
        self.thick_color = thick_color
        self.digit_color = digit_color

    def set_up(self):
        self.surf.fill(self.background_color)

        rect = Rect(2 * self.SIZE,
                    2 * self.SIZE,
                    2 * self.SIZE,
                    self.HELPBAR_LENGTH - 4 * self.SIZE,
                    self.HELPBAR_WIDTH - 4 * self.SIZE)
        rect.set_color(self.thick_color)
        rect.draw(self.surf)

        color = self.thin_color
        for i in range(8):
            rect = pygame.Rect(2 * self.SIZE + i * self.SIZE + (i + 1) * 9 * self.SIZE,
                               2 * self.SIZE,
                               self.SIZE,
                               self.HELPBAR_WIDTH - 4 * self.SIZE)
            self.surf.fill(color, rect)

        return self.surf

    def user_move(self, digits_dont_display):
        background_color = self.background_color
        digit_color = self.digit_color
        for i in range(1, 10):
            if i not in digits_dont_display and not self.disable:
                symbol = Symbol(self.SIZE, DIGITS[i])
                symbol.set_color(background_color, digit_color)
                surf = symbol.display()
                self.surf.blit(surf, (2 * self.SIZE + (i - 1) * 10 * self.SIZE,
                                      2 * self.SIZE))
            else:
                rect = pygame.Rect(2 * self.SIZE + (i - 1) * 10 * self.SIZE,
                                   2 * self.SIZE,
                                   9 * self.SIZE,
                                   9 * self.SIZE)
                self.surf.fill(background_color, rect)

        return self.surf
