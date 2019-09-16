import pygame


class Rect:
    """
    Represents a non filled in rectangle with a non zero border.

    Instance Variables:
        thickness(int): Thickness of the border.
        x(int): X coordinate of the top left corner (not including the border).
        y(int): Y coordinate of the top left corner (not including the border).
        length(int): Length (in the x direction) of the rectangle.
        width(int): Width (in the y direction) of the rectangle.

    Methods:
        set_color: Sets the color of the rectangle.
        draw: Draws the rectangle on a Surface.
    """

    def __init__(self, thickness, x, y, length, width):
        self.thickness = thickness
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def set_color(self, color):
        self.color = color

    def draw(self, surf):
        color = self.color

        pygame.draw.rect(surf,
                         color,
                         pygame.Rect(self.x - self.thickness,
                                     self.y - self.thickness,
                                     self.length + 2 * self.thickness,
                                     self.thickness))
        pygame.draw.rect(surf,
                         color,
                         pygame.Rect(self.x - self.thickness,
                                     self.y + self.width,
                                     self.length + 2 * self.thickness,
                                     self.thickness))
        pygame.draw.rect(surf,
                         color,
                         pygame.Rect(self.x - self.thickness,
                                     self.y - self.thickness,
                                     self.thickness,
                                     self.width + 2 * self.thickness))
        pygame.draw.rect(surf,
                         color,
                         pygame.Rect(self.x + self.length,
                                     self.y - self.thickness,
                                     self.thickness,
                                     self.width + 2 * self.thickness))
