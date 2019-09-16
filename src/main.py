import sys
import pygame
import math
pygame.init()

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

DIGIT_1 = [[1,1,1,1,0,0,0],
           [0,0,0,1,0,0,0],
           [0,0,0,1,0,0,0],
           [0,0,0,1,0,0,0],
           [0,0,0,1,0,0,0],
           [0,0,0,1,0,0,0],
           [1,1,1,1,1,1,1]]
DIGIT_2 = [[1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0],
           [1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1]]
DIGIT_3 = [[1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1]]
DIGIT_4 = [[1,0,0,0,0,0,1],
           [1,0,0,0,0,0,1],
           [1,0,0,0,0,0,1],
           [1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1]]
DIGIT_5 = [[1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0],
           [1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1]]
DIGIT_6 = [[1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0],
           [1,0,0,0,0,0,0],
           [1,1,1,1,1,1,1],
           [1,0,0,0,0,0,1],
           [1,0,0,0,0,0,1],
           [1,1,1,1,1,1,1]]
DIGIT_7 = [[1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1]]
DIGIT_8 = [[1,1,1,1,1,1,1],
           [1,0,0,0,0,0,1],
           [1,0,0,0,0,0,1],
           [1,1,1,1,1,1,1],
           [1,0,0,0,0,0,1],
           [1,0,0,0,0,0,1],
           [1,1,1,1,1,1,1]]
DIGIT_9 = [[1,1,1,1,1,1,1],
           [1,0,0,0,0,0,1],
           [1,0,0,0,0,0,1],
           [1,1,1,1,1,1,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1],
           [0,0,0,0,0,0,1]]

LETTER_D = [[1,1,1,1,1,1,0],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,0]]
LETTER_K = [[1,0,0,0,0,0,1],
            [1,0,0,0,0,1,0],
            [1,0,0,1,1,0,0],
            [1,1,1,0,0,0,0],
            [1,0,0,1,1,0,0],
            [1,0,0,0,0,1,0],
            [1,0,0,0,0,0,1]]
LETTER_O = [[1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1]]
LETTER_S = [[1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,1,1,1,1,1,1],
            [0,0,0,0,0,0,1],
            [0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1]]
LETTER_U = [[1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1]]

DIGITS = {1: DIGIT_1,
          2: DIGIT_2,
          3: DIGIT_3,
          4: DIGIT_4,
          5: DIGIT_5,
          6: DIGIT_6,
          7: DIGIT_7,
          8: DIGIT_8,
          9: DIGIT_9}

WORD_SUDOKU = [LETTER_S,
               LETTER_U,
               LETTER_D,
               LETTER_O,
               LETTER_K,
               LETTER_U]

SUDOKU_PUZZLE = [[0,0,4,1,0,0,0,0,0],
                 [0,6,0,8,0,9,4,0,0],
                 [0,0,0,0,0,0,9,2,0],
                 [1,0,0,0,6,2,0,3,0],
                 [8,0,0,0,0,0,0,0,6],
                 [0,5,0,3,9,0,0,0,4],
                 [0,2,7,0,0,0,0,0,0],
                 [0,0,3,9,0,7,0,8,0],
                 [0,0,0,0,0,1,6,0,0]]

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------


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
        __init__: Initializes the rectangle.
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
                         pygame.Rect(self.x-self.thickness,
                                     self.y-self.thickness,
                                     self.length+2*self.thickness,
                                     self.thickness))
        pygame.draw.rect(surf,
                         color,
                         pygame.Rect(self.x-self.thickness,
                                     self.y+self.width,
                                     self.length+2*self.thickness,
                                     self.thickness))
        pygame.draw.rect(surf,
                         color,
                         pygame.Rect(self.x-self.thickness,
                                     self.y-self.thickness,
                                     self.thickness,
                                     self.width+2*self.thickness))
        pygame.draw.rect(surf,
                         color,
                         pygame.Rect(self.x+self.length,
                                     self.y-self.thickness,
                                     self.thickness,
                                     self.width+2*self.thickness))

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

class Cell:
    """
    Represents a cell on the Sudoku board.

    Instance Variables:
        SIZE(int): The width and height of the cell.
        surf(Surface): The surface that represents the cell visually.
        val(int): The value to be shown on the cell, i.e. what digit the cell is currently.
        background_color(Color): The background color.
        number_color: The color of the digit.

    Methods:
        __init__: Initializes the cell.
        set_color: Sets the color attributes of the cell.
        display:

    """

    def __init__(self, size):
        self.SIZE = size
        self.surf = pygame.Surface((9*self.SIZE, 9*self.SIZE))
        self.val = 0

    def set_color(self, background_color, number_color):
        self.background_color = background_color
        self.number_color = number_color

    def display(self):
        self.surf.fill(self.background_color)

        if (self.val != 0):
            symbol = Symbol(self.SIZE, DIGITS[self.val])
            symbol.set_color(self.background_color, self.number_color)
            self.surf.blit(symbol.display(), (0, 0))
        
        return self.surf

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

class Board:
    
    def __init__(self,size):

        self.SIZE = size
        self.BOARD_WIDTH = 95*self.SIZE
        self.surf = pygame.Surface((self.BOARD_WIDTH,self.BOARD_WIDTH))
        self.current_selection = [0,0]

        self.board = []
        for i in range(9):
            board_row = []
            for j in range(9):
                board_row.append(Cell(size))
            self.board.append(board_row)

    def set_color(self,background_color,thin_color,thick_color,highlight_color,game_digit_color,user_digit_color):
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
                               i*31*self.SIZE,
                               self.BOARD_WIDTH,
                               2*self.SIZE)
            self.surf.fill(color,rect)
            rect = pygame.Rect(i*31*self.SIZE,
                               0,
                               2*self.SIZE,
                               self.BOARD_WIDTH)
            self.surf.fill(color,rect)

        color = self.thin_color
        for i in range(3):
            for j in range(3):
                for k in range(2):
                    rect = pygame.Rect(j*29*self.SIZE+(j+1)*2*self.SIZE,
                                       i*29*self.SIZE+(i+1)*2*self.SIZE+k*self.SIZE+(k+1)*9*self.SIZE,
                                       29*self.SIZE,
                                       self.SIZE)
                    self.surf.fill(color,rect)
                    rect = pygame.Rect(i*29*self.SIZE+(i+1)*2*self.SIZE+k*self.SIZE+(k+1)*9*self.SIZE,
                                       j*29*self.SIZE+(j+1)*2*self.SIZE,
                                       self.SIZE,
                                       29*self.SIZE)
                    self.surf.fill(color,rect)
                
        return self.surf

    def display(self):
        self.set_up()
        self.clear_board()
        self.__display_game()
        self.display_highlight_selection()
        
        return self.surf

    def import_game(self,game):
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
                        rect = pygame.Rect(j*29*self.SIZE+(j+1)*2*self.SIZE+l*10*self.SIZE,
                                           i*29*self.SIZE+(i+1)*2*self.SIZE+k*10*self.SIZE,
                                           9*self.SIZE,
                                           9*self.SIZE)
                        self.surf.fill(color,rect)

    def __display_game(self):
        background_color = self.background_color
        number_color_1 = self.game_digit_color
        number_color_2 = self.user_digit_color
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        (x,y) = (3*i+k,3*j+l)
                        if (self.game[x][y] != 0):
                            self.board[x][y].set_color(background_color,number_color_1)
                            self.board[x][y].val = self.game[x][y]
                            surf = self.board[x][y].display()
                            self.surf.blit(surf,(j*29*self.SIZE+(j+1)*2*self.SIZE+l*10*self.SIZE,
                                                 i*29*self.SIZE+(i+1)*2*self.SIZE+k*10*self.SIZE))
                        elif (self.board[x][y].val != 0):
                            self.board[x][y].set_color(background_color,number_color_2)
                            surf = self.board[x][y].display()
                            self.surf.blit(surf,(j*29*self.SIZE+(j+1)*2*self.SIZE+l*10*self.SIZE,
                                                 i*29*self.SIZE+(i+1)*2*self.SIZE+k*10*self.SIZE))

    def user_move(self,num):
        background_color = self.background_color
        number_color = self.user_digit_color
        
        if (self.game[self.current_selection[0]][self.current_selection[1]] == 0):
            (x,y) = (self.current_selection[0],self.current_selection[1])
            (i,k,j,l) = (int(self.current_selection[0]//3),self.current_selection[0]%3,int(self.current_selection[1]//3),self.current_selection[1]%3)
            self.board[x][y].set_color(background_color,number_color)
            self.board[x][y].val = num
            surf = self.board[x][y].display()
            self.surf.blit(surf,(j*29*self.SIZE+(j+1)*2*self.SIZE+l*10*self.SIZE,
                                 i*29*self.SIZE+(i+1)*2*self.SIZE+k*10*self.SIZE))

        return self.surf

    def display_highlight_selection(self):

        color = self.highlight_color
        (i,k,j,l) = (int(self.current_selection[0]//3),self.current_selection[0]%3,int(self.current_selection[1]//3),self.current_selection[1]%3)
        
        rect = Rect(int(math.ceil(self.SIZE/2)),
                    j*29*self.SIZE+(j+1)*2*self.SIZE+l*10*self.SIZE,
                    2*self.SIZE,
                    9*self.SIZE,
                    self.BOARD_WIDTH-4*self.SIZE)
        rect.set_color(color)
        rect.draw(self.surf)

        rect = Rect(int(math.ceil(self.SIZE/2)),
                    2*self.SIZE,
                    i*29*self.SIZE+(i+1)*2*self.SIZE+k*10*self.SIZE,
                    self.BOARD_WIDTH-4*self.SIZE,
                    9*self.SIZE)
        rect.set_color(color)
        rect.draw(self.surf)

        return self.surf

    def remove_highlight_selection(self):
        color = self.thick_color
        for i in range(4):
            rect = pygame.Rect(0,
                               i*31*self.SIZE,
                               self.BOARD_WIDTH,
                               2*self.SIZE)
            self.surf.fill(color,rect)
            rect = pygame.Rect(i*31*self.SIZE,
                               0,
                               2*self.SIZE,
                               self.BOARD_WIDTH)
            self.surf.fill(color,rect)
        
        color = self.thin_color
        for i in range(3):
            for j in range(3):
                for k in range(2):
                    rect = pygame.Rect(j*29*self.SIZE+(j+1)*2*self.SIZE,
                                       i*29*self.SIZE+(i+1)*2*self.SIZE+k*self.SIZE+(k+1)*9*self.SIZE,
                                       29*self.SIZE,
                                       self.SIZE)
                    self.surf.fill(color,rect)
                    rect = pygame.Rect(i*29*self.SIZE+(i+1)*2*self.SIZE+k*self.SIZE+(k+1)*9*self.SIZE,
                                       j*29*self.SIZE+(j+1)*2*self.SIZE,
                                       self.SIZE,
                                       29*self.SIZE)
                    self.surf.fill(color,rect)
                
        return self.surf

    def non_valid_vals(self):
        non_valid_vals = set()
        (x,y) = (self.current_selection[0],self.current_selection[1])
        if (self.game[x][y] == 0):
            for i in range(9):
                non_valid_vals.add(self.board[x][i].val)
                non_valid_vals.add(self.board[i][y].val)
            
            (a,b) = (int(x//3),int(y//3))
            for i in range(3):
                for j in range(3):
                    non_valid_vals.add(self.board[3*a+i][3*b+j].val)
        else:
            for i in range(1,10):
                non_valid_vals.add(i)

        return non_valid_vals

    def delete_cell(self):
        (x,y) = (self.current_selection[0],self.current_selection[1])
        self.board[x][y].val = 0

        return self.non_valid_vals()

    def reset(self):
        for i in range(9):
            for j in range(9):
                if (self.game[i][j] == 0):
                    self.board[i][j].val = 0
                

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

class HelpBar:
        
    def __init__(self,size,digits):
        self.SIZE = size
        self.digits = []
        self.disable = False
        
        for i in digits:
           self.digits.append(Symbol(size,i))
        self.HELPBAR_LENGTH = 93*size
        self.HELPBAR_WIDTH = 13*size
        self.surf = pygame.Surface((self.HELPBAR_LENGTH,self.HELPBAR_WIDTH))

    def set_color(self,background_color,thin_color,thick_color,digit_color):
        self.background_color = background_color
        self.thin_color = thin_color
        self.thick_color = thick_color
        self.digit_color = digit_color

    def set_up(self):
        self.surf.fill(self.background_color)

        rect = Rect(2*self.SIZE,
                    2*self.SIZE,
                    2*self.SIZE,
                    self.HELPBAR_LENGTH-4*self.SIZE,
                    self.HELPBAR_WIDTH-4*self.SIZE)
        rect.set_color(self.thick_color)
        rect.draw(self.surf)

        color = self.thin_color
        for i in range(8):
            rect = pygame.Rect(2*self.SIZE+i*self.SIZE+(i+1)*9*self.SIZE,
                               2*self.SIZE,
                               self.SIZE,
                               self.HELPBAR_WIDTH-4*self.SIZE)
            self.surf.fill(color,rect)
        
        return self.surf

    def user_move(self,digits_dont_display):
        background_color = self.background_color
        digit_color = self.digit_color
        for i in range(1,10):
            if (i not in digits_dont_display and not self.disable):  
                symbol = Symbol(self.SIZE,DIGITS[i])
                symbol.set_color(background_color,digit_color)
                surf = symbol.display()
                self.surf.blit(surf,(2*self.SIZE+(i-1)*10*self.SIZE,
                                     2*self.SIZE))
            else:
                rect = pygame.Rect(2*self.SIZE+(i-1)*10*self.SIZE,
                                   2*self.SIZE,
                                   9*self.SIZE,
                                   9*self.SIZE)
                self.surf.fill(background_color,rect)

        return self.surf            

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

class Symbol:

    def __init__(self,size,symbol):
        self.size = size
        self.symbol = symbol #7x7 array
        self.surf = pygame.Surface((9*size,9*size))

    def __str__(self):
        string = ""
        for i in range(len(self.symbol)):
            string += str(self.symbol[i])
            string += "\n"
        string += "\n"
        return string

    def set_color(self,background_color,symbol_color):
        self.background_color = background_color
        self.symbol_color = symbol_color
        
    def display(self):
        self.surf.fill(self.background_color)

        color = self.symbol_color
        for i in range(7):
            for j in range(7):
                if (self.symbol[i][j] == 1):
                    rect = pygame.Rect(self.size+j*self.size,
                                       self.size+i*self.size,
                                       self.size,
                                       self.size)
                    self.surf.fill(color,rect)
        
        return self.surf

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

class Word:
    
    def __init__(self,size,symbols):
        self.size = size
        self.symbols = []
        
        for i in symbols:
           self.symbols.append(Symbol(size,i))
        self.surf = pygame.Surface((size+8*size*len(symbols),9*size))

    def __str__(self):
        string = ""
        for i in range(len(self.symbols)):
            string += str(self.symbols[i])
        string += "\n\n"
        return string

    def set_color(self,background_color,word_color):
        self.background_color = background_color
        self.word_color = word_color

    def display(self):
        self.surf.fill(self.background_color)
        
        for i in range(len(self.symbols)):
            self.symbols[i].set_color(self.background_color,self.word_color)
            self.surf.blit(self.symbols[i].display(),(8*i*self.size,0))

        return self.surf

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

COLOR_1 = ((255,255,255))
COLOR_2 = ((0,0,0))
COLOR_3 = ((255,255,0))
COLOR_4 = ((0,0,255))

SIZE = 3
SCREEN_SIZE = ((800,450))

# --------------------------------------------------------------------------------------------------------------------------------------------

pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode(SCREEN_SIZE,pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)

screen.fill(COLOR_1)
full_screen = screen.copy()

clock = pygame.time.Clock()
clock.tick(30)

# --------------------------------------------------------------------------------------------------------------------------------------------

title = Word(2*SIZE,WORD_SUDOKU)
title.set_color(COLOR_1,
                COLOR_2)
surf = title.display()
title_size = surf.get_size()
title_offset = ((SCREEN_SIZE[0]-title_size[0])/2,
                4*SIZE)
full_screen.blit(surf,title_offset)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

board = Board(SIZE)
board.set_color(COLOR_1,
                COLOR_2,
                COLOR_2,
                COLOR_3,
                COLOR_2,
                COLOR_4)
board.set_up()
surf = board.import_game(SUDOKU_PUZZLE)
board_size = surf.get_size()
board_offset = ((SCREEN_SIZE[0]-board_size[0])/2,
                4*SIZE+6*SIZE+title_size[1])
full_screen.blit(surf,board_offset)

board.current_selection = [0,0]
full_screen.blit(board.display_highlight_selection(),
                 board_offset)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

helpbar = HelpBar(SIZE,DIGITS)
helpbar.set_color(COLOR_1,
                  COLOR_2,
                  COLOR_2,
                  COLOR_2)
surf = helpbar.set_up()
helpbar_offset = (SIZE+board_offset[0],
                  3*SIZE+((6*SIZE+title_size[1]+board_size[1])*3+SCREEN_SIZE[1])/4)
full_screen.blit(surf,helpbar_offset)

non_valid_vals = board.non_valid_vals()
full_screen.blit(helpbar.user_move(non_valid_vals),
                 helpbar_offset)
                 

# --------------------------------------------------------------------------------------------------------------------------------------------

def main():
    highlight_shown = True
    
    while True:
        for event in pygame.event.get():
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            elif (event.type == pygame.VIDEORESIZE):
                new_res = event.dict['size']
                screen = pygame.display.set_mode(new_res, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            elif (event.type == pygame.KEYDOWN):
                keys = pygame.key.get_pressed()

                if (event.key == pygame.K_q):
                    pygame.quit()
                    sys.exit()

                elif (event.key == pygame.K_r):
                    board.reset()
                    full_screen.blit(board.display(),
                                     board_offset)
                    non_valid_vals = board.non_valid_vals()
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)
                    if (not highlight_shown):
                        surf = board.remove_highlight_selection()
                        full_screen.blit(surf,board_offset)

                elif (event.key == pygame.K_h):
                    helpbar.disable = not helpbar.disable
                    non_valid_vals = board.non_valid_vals()
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)

                elif (event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE):
                    non_valid_vals = board.delete_cell()
                    full_screen.blit(board.display(),
                                     board_offset)
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)
                
                elif (event.key == pygame.K_0 and keys[pygame.K_LCTRL]):
                    COLOR_1 = ((255,255,255))
                    COLOR_2 = ((0,0,0))
                    COLOR_3 = ((255,255,0))
                    COLOR_4 = ((0,0,255))

                    full_screen.fill(COLOR_1)                               # Background
                    title.set_color(COLOR_1,                                # Background
                                    COLOR_2)                                # Text
                    full_screen.blit(title.display(),
                                     title_offset)
                    board.set_color(COLOR_1,                                # Background
                                    COLOR_2,                                # Thin
                                    COLOR_2,                                # Thick
                                    COLOR_3,                                # Highlight
                                    COLOR_2,                                # Game Digits
                                    COLOR_4)                                # User Digits
                    full_screen.blit(board.display(),
                                     board_offset)
                    helpbar.set_color(COLOR_1,                              # Background
                                      COLOR_2,                              # Thin
                                      COLOR_2,                              # Thick,
                                      COLOR_2)                              # Text
                    full_screen.blit(helpbar.set_up(),
                                     helpbar_offset)
                    non_valid_vals = board.non_valid_vals()
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)

                elif (event.key == pygame.K_1 and keys[pygame.K_LCTRL]):
                    COLOR_1 = pygame.Color("#5d001e")
                    COLOR_2 = pygame.Color("#e3e2df")
                    COLOR_3 = pygame.Color("#e3afbc")
                    COLOR_4 = pygame.Color("#9a1750")
                    COLOR_5 = pygame.Color("#ee4c7c")
                
                    full_screen.fill(COLOR_2)                               # Background
                    title.set_color(COLOR_2,                                # Background
                                    COLOR_5)                                # Text
                    full_screen.blit(title.display(),
                                     title_offset)
                    board.set_color(COLOR_2,                                # Background
                                    COLOR_4,                                # Thin
                                    COLOR_1,                                # Thick
                                    COLOR_3,                                # Highlight
                                    COLOR_1,                                # Game Digits
                                    COLOR_4)                                # User Digits
                    full_screen.blit(board.display(),
                                     board_offset)
                    helpbar.set_color(COLOR_2,                              # Background
                                      COLOR_4,                              # Thin
                                      COLOR_1,                              # Thick,
                                      COLOR_5)                              # Text
                    full_screen.blit(helpbar.set_up(),
                                     helpbar_offset)
                    non_valid_vals = board.non_valid_vals()
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)

                elif (event.key == pygame.K_2 and keys[pygame.K_LCTRL]):
                    COLOR_1 = pygame.Color("#f8e9a1")
                    COLOR_2 = pygame.Color("#f76c6c")
                    COLOR_3 = pygame.Color("#a8d0e6")
                    COLOR_4 = pygame.Color("#374785")
                    COLOR_5 = pygame.Color("#24305e")
                
                    full_screen.fill(COLOR_1)                               # Background
                    title.set_color(COLOR_1,                                # Background
                                    COLOR_2)                                # Text
                    full_screen.blit(title.display(),
                                     title_offset)
                    board.set_color(COLOR_1,                                # Background
                                    COLOR_3,                                # Thin
                                    COLOR_5,                                # Thick
                                    COLOR_2,                                # Highlight
                                    COLOR_4,                                # Game Digits
                                    COLOR_3)                                # User Digits
                    full_screen.blit(board.display(),
                                     board_offset)
                    helpbar.set_color(COLOR_1,                              # Background
                                      COLOR_3,                              # Thin
                                      COLOR_5,                              # Thick,
                                      COLOR_2)                              # Text
                    full_screen.blit(helpbar.set_up(),
                                     helpbar_offset)
                    non_valid_vals = board.non_valid_vals()
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)

                elif (event.key == pygame.K_3 and keys[pygame.K_LCTRL]):
                    COLOR_1 = pygame.Color("#fcfc62")
                    COLOR_2 = pygame.Color("#feffea")
                    COLOR_3 = pygame.Color("#c9c9c9")
                    COLOR_4 = pygame.Color("#a3a3a3")
                    COLOR_5 = pygame.Color("#424242")

                    full_screen.fill(COLOR_2)                               # Background
                    title.set_color(COLOR_2,                                # Background
                                    COLOR_5)                                # Text
                    full_screen.blit(title.display(),
                                     title_offset)
                    board.set_color(COLOR_2,                                # Background
                                    COLOR_3,                                # Thin
                                    COLOR_5,                                # Thick
                                    COLOR_1,                                # Highlight
                                    COLOR_5,                                # Game Digits
                                    COLOR_4)                                # User Digits
                    full_screen.blit(board.display(),
                                     board_offset)
                    helpbar.set_color(COLOR_2,                              # Background
                                      COLOR_3,                              # Thin
                                      COLOR_5,                              # Thick,
                                      COLOR_5)                              # Text
                    full_screen.blit(helpbar.set_up(),
                                     helpbar_offset)
                    non_valid_vals = board.non_valid_vals()
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)
                    
                elif (event.key == pygame.K_4 and keys[pygame.K_LCTRL]):
                    pass

                elif (event.key == pygame.K_5 and keys[pygame.K_LCTRL]):
                    pass

                elif (event.key == pygame.K_6 and keys[pygame.K_LCTRL]):
                    pass

                elif (event.key == pygame.K_7 and keys[pygame.K_LCTRL]):
                    pass

                elif (event.key == pygame.K_8 and keys[pygame.K_LCTRL]):
                    pass

                elif (event.key == pygame.K_9 and keys[pygame.K_LCTRL]):
                    pass

                elif (event.key in [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]):
                    full_screen.blit(board.user_move(event.key-48),
                                     board_offset)
                    non_valid_vals = board.non_valid_vals()
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)

                elif (event.key == pygame.K_ESCAPE):
                    surf = board.remove_highlight_selection()
                    full_screen.blit(surf,board_offset)
                    highlight_shown = False
                
                elif (event.key in [pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP]):
                    if (highlight_shown):
                        if (event.key == pygame.K_RIGHT):
                            board.current_selection[1] += 1
                            board.current_selection[1] %= 9
                        if (event.key == pygame.K_LEFT):
                            board.current_selection[1] -= 1
                            board.current_selection[1] %= 9
                        if (event.key == pygame.K_DOWN):
                            board.current_selection[0] += 1
                            board.current_selection[0] %= 9
                        if (event.key == pygame.K_UP):
                            board.current_selection[0] -= 1
                            board.current_selection[0] %= 9

                        full_screen.blit(board.remove_highlight_selection(),
                                         board_offset)
                    highlight_shown = True
                    full_screen.blit(board.display_highlight_selection(),
                                     board_offset)
                    non_valid_vals = board.non_valid_vals()
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)
        
        screen.blit(pygame.transform.scale(full_screen,new_res),(0,0))        
        pygame.display.flip()

main()
