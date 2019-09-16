import pygame
from .symbol import Symbol


class Word:
    """
    Represents a string of symbols.

    Instance Variables:
        size(int): Unit size.
        symbols(list): String of symbols.
        surf(Surface): Surface to display the word visually.
        background_color(Color): Background color.
        word_color(Color): Word color.

    Methods:
        set_color: Sets the colors
        display: Displays the word on the surface.
    """

    def __init__(self, size, symbols):
        self.size = size
        self.symbols = []

        for i in symbols:
            self.symbols.append(Symbol(size, i))
        self.surf = pygame.Surface((size + 8 * size * len(symbols), 9 * size))

    def __str__(self):
        string = ""
        for i in range(len(self.symbols)):
            string += str(self.symbols[i])
        string += "\n\n"
        return string

    def set_color(self, background_color, word_color):
        self.background_color = background_color
        self.word_color = word_color

    def display(self):
        self.surf.fill(self.background_color)

        for i in range(len(self.symbols)):
            self.symbols[i].set_color(self.background_color, self.word_color)
            self.surf.blit(self.symbols[i].display(), (8 * i * self.size, 0))

        return self.surf
