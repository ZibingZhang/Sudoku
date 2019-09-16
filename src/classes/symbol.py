import pygame


class Symbol:
    """
    Represents a symbol that can be rendered by a 7x7 array of pixels.

    Instance Variables:
        size(int): Unit size.
        symbol(list): 7x7 2D array representing the symbol.
        surf(Surface): Surface to represent the symbol visually.
        background_color(Color): Background color.
        symbol_color(Color): Color of symbol.

    Methods:
        set_color: Sets the colors of the symbol.
        display: Display the symbol.
    """

    def __init__(self, size, symbol):
        self.size = size
        self.symbol = symbol  # 7x7 array
        self.surf = pygame.Surface((9 * size, 9 * size))

    def __str__(self):
        string = ""
        for i in range(len(self.symbol)):
            string += str(self.symbol[i])
            string += "\n"
        string += "\n"
        return string

    def set_color(self, background_color, symbol_color):
        self.background_color = background_color
        self.symbol_color = symbol_color

    def display(self):
        self.surf.fill(self.background_color)

        color = self.symbol_color
        for i in range(7):
            for j in range(7):
                if self.symbol[i][j] == 1:
                    rect = pygame.Rect(self.size + j * self.size,
                                       self.size + i * self.size,
                                       self.size,
                                       self.size)
                    self.surf.fill(color, rect)

        return self.surf
