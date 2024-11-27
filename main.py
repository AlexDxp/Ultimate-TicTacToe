# Alex Day, Jun Jia Liu
# 18/10/2024
# Term 1 Mini Project - Ultimate Tic Tac Toe / Super TTT

# \\ IMPORTS //#
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # Disables that really annoying welcome message pygame outputs

import sys
import playsound3
import pygame
from pygame import MOUSEBUTTONDOWN

# \\ CONSTANTS //#

# Sizes
SCREEN_WIDTH = 646  # px
SCREEN_HEIGHT = 646  # px

GRID_SIZE = 9
CELL_SIZE = (SCREEN_WIDTH + 2) // GRID_SIZE

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)


# \\ FUNCTIONS //#

# \\ CLASSES //#

class TTTGame:
    def __init__(self):
        self.grid = [["#" for i in range(9)] for i in range(9)]
        self.ultimate_grid = [["#" for i in range(3)] for i in range(3)]
        self.previous = [["#" for i in range(3)] for i in range(3)]
        self.winner = None
        self.turn = "X"
        self.restriction_x = -1
        self.restriction_y = -1
        self.running = True

        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Super T-T-T [" + self.turn + " Turn | Unrestricted]")

        self.game()

    def draw_grid(self):
        colour = WHITE

        self.screen.fill(colour)

        for row in range(9):
            for col in range(9):
                row_grid = row // 3
                col_grid = col // 3

                if row_grid % 2 == 0:
                    if col_grid % 2 == 1:
                        colour = GREY
                    else:
                        colour = WHITE
                else:
                    if col_grid % 2 == 0:
                        colour = GREY
                    else:
                        colour = WHITE

                x_pos = (row * 70) + (2 * row)
                y_pos = (col * 70) + (2 * col)

                # Draws the cells
                grid = pygame.draw.rect(self.screen, colour, (x_pos, y_pos, CELL_SIZE - 2, CELL_SIZE - 2))

                # Draws the marked cells
                if self.grid[col][row] == "X":
                    imp = pygame.image.load("./assets/70x70/x70.png")
                    self.screen.blit(imp, (x_pos, y_pos))
                elif self.grid[col][row] == "O":
                    imp = pygame.image.load("./assets/70x70/o70.png")
                    self.screen.blit(imp, (x_pos, y_pos))

                # Draws the gridlines
                x_gridline = pygame.draw.rect(self.screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE - 2, CELL_SIZE, 2))
                y_gridline = pygame.draw.rect(self.screen, BLACK,(col * CELL_SIZE - 2, row * CELL_SIZE, 2, CELL_SIZE - 2))

        for i in range(3):
            for j in range(3):
                self.previous[j][i] = self.ultimate_grid[i][j]

        if self.grid[0][0] == self.grid[0][1] == self.grid[0][2] == "X" or self.grid[1][0] == self.grid[1][1] == self.grid[1][2] == "X" or self.grid[2][0] == self.grid[2][1] == self.grid[2][2] == "X" or self.grid[0][0] == self.grid[1][0] == self.grid[2][0] == "X" or self.grid[0][1] == self.grid[1][1] == self.grid[2][1] == "X" or self.grid[0][2] == self.grid[1][2] == self.grid[2][2] == "X" or self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == "X" or self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == "X":
            self.ultimate_grid[0][0] = "X"
        if self.grid[0][0] == self.grid[0][1] == self.grid[0][2] == "O" or self.grid[1][0] == self.grid[1][1] == self.grid[1][2] == "O" or self.grid[2][0] == self.grid[2][1] == self.grid[2][2] == "O" or self.grid[0][0] == self.grid[1][0] == self.grid[2][0] == "O" or self.grid[0][1] == self.grid[1][1] == self.grid[2][1] == "O" or self.grid[0][2] == self.grid[1][2] == self.grid[2][2] == "O" or self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == "O" or self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == "O":
            self.ultimate_grid[0][0] = "O"
        if self.grid[3][0] == self.grid[3][1] == self.grid[3][2] == "X" or self.grid[4][0] == self.grid[4][1] == self.grid[4][2] == "X" or self.grid[5][0] == self.grid[5][1] == self.grid[5][2] == "X" or self.grid[3][0] == self.grid[4][0] == self.grid[5][0] == "X" or self.grid[3][1] == self.grid[4][1] == self.grid[5][1] == "X" or self.grid[3][2] == self.grid[4][2] == self.grid[5][2] == "X" or self.grid[3][0] == self.grid[4][1] == self.grid[5][2] == "X" or self.grid[3][2] == self.grid[4][1] == self.grid[5][0] == "X":
            self.ultimate_grid[1][0] = "X"
        if self.grid[3][0] == self.grid[3][1] == self.grid[3][2] == "O" or self.grid[4][0] == self.grid[4][1] == self.grid[4][2] == "O" or self.grid[5][0] == self.grid[5][1] == self.grid[5][2] == "O" or self.grid[3][0] == self.grid[4][0] == self.grid[5][0] == "O" or self.grid[3][1] == self.grid[4][1] == self.grid[5][1] == "O" or self.grid[3][2] == self.grid[4][2] == self.grid[5][2] == "O" or self.grid[3][0] == self.grid[4][1] == self.grid[5][2] == "O" or self.grid[3][2] == self.grid[4][1] == self.grid[5][0] == "O":
            self.ultimate_grid[1][0] = "O"
        if self.grid[6][0] == self.grid[6][1] == self.grid[6][2] == "X" or self.grid[7][0] == self.grid[7][1] == self.grid[7][2] == "X" or self.grid[8][0] == self.grid[8][1] == self.grid[8][2] == "X" or self.grid[6][0] == self.grid[7][0] == self.grid[8][0] == "X" or self.grid[6][1] == self.grid[7][1] == self.grid[8][1] == "X" or self.grid[6][2] == self.grid[7][2] == self.grid[8][2] == "X" or self.grid[6][0] == self.grid[7][1] == self.grid[8][2] == "X" or self.grid[6][2] == self.grid[7][1] == self.grid[8][0] == "X":
            self.ultimate_grid[2][0] = "X"
        if self.grid[6][0] == self.grid[6][1] == self.grid[6][2] == "O" or self.grid[7][0] == self.grid[7][1] == self.grid[7][2] == "O" or self.grid[8][0] == self.grid[8][1] == self.grid[8][2] == "O" or self.grid[6][0] == self.grid[7][0] == self.grid[8][0] == "O" or self.grid[6][1] == self.grid[7][1] == self.grid[8][1] == "O" or self.grid[6][2] == self.grid[7][2] == self.grid[8][2] == "O" or self.grid[6][0] == self.grid[7][1] == self.grid[8][2] == "O" or self.grid[6][2] == self.grid[7][1] == self.grid[8][0] == "O":
            self.ultimate_grid[2][0] = "O"
        if self.grid[0][3] == self.grid[0][4] == self.grid[0][5] == "X" or self.grid[1][3] == self.grid[1][4] == self.grid[1][5] == "X" or self.grid[2][3] == self.grid[2][4] == self.grid[2][5] == "X" or self.grid[0][3] == self.grid[1][3] == self.grid[2][3] == "X" or self.grid[0][4] == self.grid[1][4] == self.grid[2][4] == "X" or self.grid[0][5] == self.grid[1][5] == self.grid[2][5] == "X" or self.grid[0][3] == self.grid[1][4] == self.grid[2][5] == "X" or self.grid[0][5] == self.grid[1][4] == self.grid[2][3] == "X":
            self.ultimate_grid[0][1] = "X"
        if self.grid[0][3] == self.grid[0][4] == self.grid[0][5] == "O" or self.grid[1][3] == self.grid[1][4] == self.grid[1][5] == "O" or self.grid[2][3] == self.grid[2][4] == self.grid[2][5] == "O" or self.grid[0][3] == self.grid[1][3] == self.grid[2][3] == "O" or self.grid[0][4] == self.grid[1][4] == self.grid[2][4] == "O" or self.grid[0][5] == self.grid[1][5] == self.grid[2][5] == "O" or self.grid[0][3] == self.grid[1][4] == self.grid[2][5] == "O" or self.grid[0][5] == self.grid[1][4] == self.grid[2][3] == "O":
            self.ultimate_grid[0][1] = "O"
        if self.grid[3][3] == self.grid[3][4] == self.grid[3][5] == "X" or self.grid[4][3] == self.grid[4][4] == self.grid[4][5] == "X" or self.grid[5][3] == self.grid[5][4] == self.grid[5][5] == "X" or self.grid[3][3] == self.grid[4][3] == self.grid[5][3] == "X" or self.grid[3][4] == self.grid[4][4] == self.grid[5][4] == "X" or self.grid[3][5] == self.grid[4][5] == self.grid[5][5] == "X" or self.grid[3][3] == self.grid[4][4] == self.grid[5][5] == "X" or self.grid[3][5] == self.grid[4][4] == self.grid[5][3] == "X":
            self.ultimate_grid[1][1] = "X"
        if self.grid[3][3] == self.grid[3][4] == self.grid[3][5] == "O" or self.grid[4][3] == self.grid[4][4] == self.grid[4][5] == "O" or self.grid[5][3] == self.grid[5][4] == self.grid[5][5] == "O" or self.grid[3][3] == self.grid[4][3] == self.grid[5][3] == "O" or self.grid[3][4] == self.grid[4][4] == self.grid[5][4] == "O" or self.grid[3][5] == self.grid[4][5] == self.grid[5][5] == "O" or self.grid[3][3] == self.grid[4][4] == self.grid[5][5] == "O" or self.grid[3][5] == self.grid[4][4] == self.grid[5][3] == "O":
            self.ultimate_grid[1][1] = "O"
        if self.grid[6][3] == self.grid[6][4] == self.grid[6][5] == "X" or self.grid[7][3] == self.grid[7][4] == self.grid[7][5] == "X" or self.grid[8][3] == self.grid[8][4] == self.grid[8][5] == "X" or self.grid[6][3] == self.grid[7][3] == self.grid[8][3] == "X" or self.grid[6][4] == self.grid[7][4] == self.grid[8][4] == "X" or self.grid[6][5] == self.grid[7][5] == self.grid[8][5] == "X" or self.grid[6][3] == self.grid[7][4] == self.grid[8][5] == "X" or self.grid[6][5] == self.grid[7][4] == self.grid[8][3] == "X":
            self.ultimate_grid[2][1] = "X"
        if self.grid[6][3] == self.grid[6][4] == self.grid[6][5] == "O" or self.grid[7][3] == self.grid[7][4] == self.grid[7][5] == "O" or self.grid[8][3] == self.grid[8][4] == self.grid[8][5] == "O" or self.grid[6][3] == self.grid[7][3] == self.grid[8][3] == "O" or self.grid[6][4] == self.grid[7][4] == self.grid[8][4] == "O" or self.grid[6][5] == self.grid[7][5] == self.grid[8][5] == "O" or self.grid[6][3] == self.grid[7][4] == self.grid[8][5] == "O" or self.grid[6][5] == self.grid[7][4] == self.grid[8][3] == "O":
            self.ultimate_grid[2][1] = "O"
        if self.grid[0][6] == self.grid[0][7] == self.grid[0][8] == "X" or self.grid[1][6] == self.grid[1][7] == self.grid[1][8] == "X" or self.grid[2][6] == self.grid[2][7] == self.grid[2][8] == "X" or self.grid[0][6] == self.grid[1][6] == self.grid[2][6] == "X" or self.grid[0][7] == self.grid[1][7] == self.grid[2][7] == "X" or self.grid[0][8] == self.grid[1][8] == self.grid[2][8] == "X" or self.grid[0][6] == self.grid[1][7] == self.grid[2][8] == "X" or self.grid[0][8] == self.grid[1][7] == self.grid[2][6] == "X":
            self.ultimate_grid[0][2] = "X"
        if self.grid[0][6] == self.grid[0][7] == self.grid[0][8] == "O" or self.grid[1][6] == self.grid[1][7] == self.grid[1][8] == "O" or self.grid[2][6] == self.grid[2][7] == self.grid[2][8] == "O" or self.grid[0][6] == self.grid[1][6] == self.grid[2][6] == "O" or self.grid[0][7] == self.grid[1][7] == self.grid[2][7] == "O" or self.grid[0][8] == self.grid[1][8] == self.grid[2][8] == "O" or self.grid[0][6] == self.grid[1][7] == self.grid[2][8] == "O" or self.grid[0][8] == self.grid[1][7] == self.grid[2][6] == "O":
            self.ultimate_grid[0][2] = "O"
        if self.grid[3][6] == self.grid[3][7] == self.grid[3][8] == "X" or self.grid[4][6] == self.grid[4][7] == self.grid[4][8] == "X" or self.grid[5][6] == self.grid[5][7] == self.grid[5][8] == "X" or self.grid[3][6] == self.grid[4][6] == self.grid[5][6] == "X" or self.grid[3][7] == self.grid[4][7] == self.grid[5][7] == "X" or self.grid[3][8] == self.grid[4][8] == self.grid[5][8] == "X" or self.grid[3][6] == self.grid[4][7] == self.grid[5][8] == "X" or self.grid[3][8] == self.grid[4][7] == self.grid[5][6] == "X":
            self.ultimate_grid[1][2] = "X"
        if self.grid[3][6] == self.grid[3][7] == self.grid[3][8] == "O" or self.grid[4][6] == self.grid[4][7] == self.grid[4][8] == "O" or self.grid[5][6] == self.grid[5][7] == self.grid[5][8] == "O" or self.grid[3][6] == self.grid[4][6] == self.grid[5][6] == "O" or self.grid[3][7] == self.grid[4][7] == self.grid[5][7] == "O" or self.grid[3][8] == self.grid[4][8] == self.grid[5][8] == "O" or self.grid[3][6] == self.grid[4][7] == self.grid[5][8] == "O" or self.grid[3][8] == self.grid[4][7] == self.grid[5][6] == "O":
            self.ultimate_grid[1][2] = "O"
        if self.grid[6][6] == self.grid[6][7] == self.grid[6][8] == "X" or self.grid[7][6] == self.grid[7][7] == self.grid[7][8] == "X" or self.grid[8][6] == self.grid[8][7] == self.grid[8][8] == "X" or self.grid[6][6] == self.grid[7][6] == self.grid[8][6] == "X" or self.grid[6][7] == self.grid[7][7] == self.grid[8][7] == "X" or self.grid[6][8] == self.grid[7][8] == self.grid[8][8] == "X" or self.grid[6][6] == self.grid[7][7] == self.grid[8][8] == "X" or self.grid[6][8] == self.grid[7][7] == self.grid[8][6] == "X":
            self.ultimate_grid[2][2] = "X"
        if self.grid[6][6] == self.grid[6][7] == self.grid[6][8] == "O" or self.grid[7][6] == self.grid[7][7] == self.grid[7][8] == "O" or self.grid[8][6] == self.grid[8][7] == self.grid[8][8] == "O" or self.grid[6][6] == self.grid[7][6] == self.grid[8][6] == "O" or self.grid[6][7] == self.grid[7][7] == self.grid[8][7] == "O" or self.grid[6][8] == self.grid[7][8] == self.grid[8][8] == "O" or self.grid[6][6] == self.grid[7][7] == self.grid[8][8] == "O" or self.grid[6][8] == self.grid[7][7] == self.grid[8][6] == "O":
            self.ultimate_grid[2][2] = "O"

        if self.ultimate_grid[0][0] == "X":
            imp = pygame.image.load("./assets/214x214/x214.png")
            self.screen.blit(imp, (0, 0))
        if self.ultimate_grid[0][0] == "O":
            imp = pygame.image.load("./assets/214x214/o214.png")
            self.screen.blit(imp, (0, 0))
        if self.ultimate_grid[0][1] == "X":
            imp = pygame.image.load("./assets/214x214/x214.png")
            self.screen.blit(imp, (216, 0))
        if self.ultimate_grid[0][1] == "O":
            imp = pygame.image.load("./assets/214x214/o214.png")
            self.screen.blit(imp, (216, 0))
        if self.ultimate_grid[0][2] == "X":
            imp = pygame.image.load("./assets/214x214/x214.png")
            self.screen.blit(imp, (432, 0))
        if self.ultimate_grid[0][2] == "O":
            imp = pygame.image.load("./assets/214x214/o214.png")
            self.screen.blit(imp, (432, 0))
        if self.ultimate_grid[1][0] == "X":
            imp = pygame.image.load("./assets/214x214/x214.png")
            self.screen.blit(imp, (0, 216))
        if self.ultimate_grid[1][0] == "O":
            imp = pygame.image.load("./assets/214x214/o214.png")
            self.screen.blit(imp, (0, 216))
        if self.ultimate_grid[1][1] == "X":
            imp = pygame.image.load("./assets/214x214/x214.png")
            self.screen.blit(imp, (216, 216))
        if self.ultimate_grid[1][1] == "O":
            imp = pygame.image.load("./assets/214x214/o214.png")
            self.screen.blit(imp, (216, 216))
        if self.ultimate_grid[1][2] == "X":
            imp = pygame.image.load("./assets/214x214/x214.png")
            self.screen.blit(imp, (432, 216))
        if self.ultimate_grid[1][2] == "O":
            imp = pygame.image.load("./assets/214x214/o214.png")
            self.screen.blit(imp, (432, 216))
        if self.ultimate_grid[2][0] == "X":
            imp = pygame.image.load("./assets/214x214/x214.png")
            self.screen.blit(imp, (0, 432))
        if self.ultimate_grid[2][0] == "O":
            imp = pygame.image.load("./assets/214x214/o214.png")
            self.screen.blit(imp, (0, 432))
        if self.ultimate_grid[2][1] == "X":
            imp = pygame.image.load("./assets/214x214/x214.png")
            self.screen.blit(imp, (216, 432))
        if self.ultimate_grid[2][1] == "O":
            imp = pygame.image.load("./assets/214x214/o214.png")
            self.screen.blit(imp, (216, 432))
        if self.ultimate_grid[2][2] == "X":
            imp = pygame.image.load("./assets/214x214/x214.png")
            self.screen.blit(imp, (432, 432))
        if self.ultimate_grid[2][2] == "O":
            imp = pygame.image.load("./assets/214x214/o214.png")
            self.screen.blit(imp, (432, 432))

        # Restriction highlights
        if self.restriction_x != -1 and self.restriction_y != -1:
            if self.ultimate_grid[self.restriction_y][self.restriction_x] == "#":
                rx_pos = (self.restriction_x * 210) + (6 * self.restriction_x)
                ry_pos = (self.restriction_y * 210) + (6 * self.restriction_y)

                highlight = pygame.Surface((214, 214), pygame.SRCALPHA)  # per-pixel alpha
                highlight.fill((0, 200, 0, 64))  # notice the alpha value in the color

                self.screen.blit(highlight, (rx_pos, ry_pos))

        if self.check_ultimate_rows():

            self.screen.fill(WHITE)

            font = pygame.font.SysFont("Comic Sans MS", 30)

            win_string = ""

            if self.winner == "X":
                win_string = "Player 1 (X) wins!"
            elif self.winner == "O":
                win_string = "Player 2 (O) wins!"

            text = font.render(win_string, True, BLACK)
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            self.screen.blit(text, text_rect)

            playsound3.playsound("./assets/sounds/tada.mp3")

        pygame.display.flip()

    def check_ultimate_rows(self):
        three_row = False
        if self.ultimate_grid[0][0] == self.ultimate_grid[0][1] == self.ultimate_grid[0][2] != "#":
            three_row = True
        elif self.ultimate_grid[1][0] == self.ultimate_grid[1][1] == self.ultimate_grid[1][2] != "#":
            three_row = True
        elif self.ultimate_grid[2][0] == self.ultimate_grid[2][1] == self.ultimate_grid[2][2] != "#":
            three_row = True
        elif self.ultimate_grid[0][0] == self.ultimate_grid[1][0] == self.ultimate_grid[2][0] != "#":
            three_row = True
        elif self.ultimate_grid[0][1] == self.ultimate_grid[1][1] == self.ultimate_grid[2][1] != "#":
            three_row = True
        elif self.ultimate_grid[0][2] == self.ultimate_grid[1][2] == self.ultimate_grid[2][2] != "#":
            three_row = True
        elif self.ultimate_grid[0][0] == self.ultimate_grid[1][1] == self.ultimate_grid[2][2] != "#":
            three_row = True
        elif self.ultimate_grid[2][0] == self.ultimate_grid[1][1] == self.ultimate_grid[0][2] != "#":
            three_row = True
        else:
            three_row = False

        if self.turn == "X":
            self.winner = "O"
        elif self.turn == "O":
            self.winner = "X"

        return three_row

    def validate_move(self, x, y):
        if (x // 3 == self.restriction_x and y // 3 == self.restriction_y) or (
                self.restriction_x == -1 and self.restriction_y == -1):
            if self.grid[y][x] == "#":
                return True
            else:
                return False
        else:
            ux = x // 3
            uy = y // 3
            if self.ultimate_grid[self.restriction_y][self.restriction_x] != "#":
                self.restriction_x = ux
                self.restriction_y = uy
                if self.grid[y][x] == "#":
                    return True
                else:
                    return False
            else:
                playsound3.playsound("./assets/sounds/denied.mp3")
                return False

    def game(self):
        self.draw_grid()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()

                        x_cell = x // 72
                        y_cell = y // 72

                        x_pos = (x_cell * 70) + (2 * x_cell)
                        y_pos = (y_cell * 70) + (2 * y_cell)

                        ux_cell = x_cell % 3
                        uy_cell = y_cell % 3

                        if self.validate_move(x_cell, y_cell):
                            playsound3.playsound("./assets/sounds/click.mp3")
                            if self.turn == "X":
                                self.grid[y_cell][x_cell] = "X"
                                self.turn = "O"
                            elif self.turn == "O":
                                self.grid[y_cell][x_cell] = "O"
                                self.turn = "X"

                            if self.ultimate_grid[uy_cell][ux_cell] == "#":
                                self.restriction_x = ux_cell
                                self.restriction_y = uy_cell
                            else:
                                self.restriction_x = -1
                                self.restriction_y = -1

                            self.draw_grid()
                        if self.restriction_x and self.restriction_y != -1:
                            pygame.display.set_caption("Super T-T-T [" + self.turn + " Turn | Restricted Move]")
                        else:
                            pygame.display.set_caption("Super T-T-T [" + self.turn + " Turn | Unrestricted]")

        pygame.quit()


if __name__ == "__main__":
    game = TTTGame()
