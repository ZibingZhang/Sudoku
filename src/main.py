import sys

from constant.other import *
from constant.letter import *
from constant.game import *

from classes.board import *
from classes.helpbar import *
from classes.word import *


pygame.init()


pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)

screen.fill(COLOR_1)
full_screen = screen.copy()

clock = pygame.time.Clock()
clock.tick(30)

# --------------------------------------------------------------------------------------------------------------------------------------------

title = Word(2*SIZE, WORD_SUDOKU)
title.set_color(COLOR_1,
                COLOR_2)
surf = title.display()
title_size = surf.get_size()
title_offset = ((SCREEN_SIZE[0]-title_size[0])/2,
                4*SIZE)
full_screen.blit(surf, title_offset)

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
full_screen.blit(surf, board_offset)

board.current_selection = [0,0]
full_screen.blit(board.display_highlight_selection(),
                 board_offset)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

helpbar = HelpBar(SIZE)
helpbar.set_color(COLOR_1,
                  COLOR_2,
                  COLOR_2,
                  COLOR_2)
surf = helpbar.set_up()
helpbar_offset = (SIZE+board_offset[0],
                  3*SIZE+((6*SIZE+title_size[1]+board_size[1])*3+SCREEN_SIZE[1])/4)
full_screen.blit(surf, helpbar_offset)

non_valid_vals = board.non_valid_vals()
full_screen.blit(helpbar.user_move(non_valid_vals),
                 helpbar_offset)
                 

# --------------------------------------------------------------------------------------------------------------------------------------------

def main():
    highlight_shown = True
    
    while True:
        for event in pygame.event.get():
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            elif event.type == pygame.VIDEORESIZE:
                new_res = event.dict['size']
                screen = pygame.display.set_mode(new_res, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_r:
                    board.reset()
                    full_screen.blit(board.display(),
                                     board_offset)
                    non_valid_vals = board.non_valid_vals()
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)
                    if not highlight_shown:
                        surf = board.remove_highlight_selection()
                        full_screen.blit(surf ,board_offset)

                elif event.key == pygame.K_h:
                    helpbar.disable = not helpbar.disable
                    non_valid_vals = board.non_valid_vals()
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)

                elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    non_valid_vals = board.delete_cell()
                    full_screen.blit(board.display(),
                                     board_offset)
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)
                
                elif event.key == pygame.K_0 and keys[pygame.K_LCTRL]:
                    COLOR_1 = (255, 255, 255)
                    COLOR_2 = (0, 0, 0)
                    COLOR_3 = (255, 255, 0)
                    COLOR_4 = (0, 0, 255)

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

                elif event.key == pygame.K_1 and keys[pygame.K_LCTRL]:
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

                elif event.key == pygame.K_2 and keys[pygame.K_LCTRL]:
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

                elif event.key == pygame.K_3 and keys[pygame.K_LCTRL]:
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
                    
                elif event.key == pygame.K_4 and keys[pygame.K_LCTRL]:
                    pass

                elif event.key == pygame.K_5 and keys[pygame.K_LCTRL]:
                    pass

                elif event.key == pygame.K_6 and keys[pygame.K_LCTRL]:
                    pass

                elif event.key == pygame.K_7 and keys[pygame.K_LCTRL]:
                    pass

                elif event.key == pygame.K_8 and keys[pygame.K_LCTRL]:
                    pass

                elif event.key == pygame.K_9 and keys[pygame.K_LCTRL]:
                    pass

                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    full_screen.blit(board.user_move(event.key-48),
                                     board_offset)
                    non_valid_vals = board.non_valid_vals()
                    full_screen.blit(helpbar.user_move(non_valid_vals),
                                     helpbar_offset)

                elif event.key == pygame.K_ESCAPE:
                    surf = board.remove_highlight_selection()
                    full_screen.blit(surf,board_offset)
                    highlight_shown = False
                
                elif event.key in [pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP]:
                    if highlight_shown:
                        if event.key == pygame.K_RIGHT:
                            board.current_selection[1] += 1
                            board.current_selection[1] %= 9
                        if event.key == pygame.K_LEFT:
                            board.current_selection[1] -= 1
                            board.current_selection[1] %= 9
                        if event.key == pygame.K_DOWN:
                            board.current_selection[0] += 1
                            board.current_selection[0] %= 9
                        if event.key == pygame.K_UP:
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
        
        screen.blit(pygame.transform.scale(full_screen, new_res), (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
