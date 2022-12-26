# cell class
import pygame, sys
from sudoku_generator import *
from constants import *

class Cell:
    def __init__(self, value, row, col, screen):  # Constructor for the Cell class
        self.value = value
        self.sketched_value = None
        self.row = row
        self.col = col
        self.screen = screen
        self.width = WIDTH
        self.height = HEIGHT
        self.clicked = False

    def set_cell_value(self, value):  # Setter for this cell’s value
        self.value = value

    def set_sketched_value(self, value):  # Setter for this cell’s sketched value
        self.sketched_value = value

    def draw(self):
        chip_font = pygame.font.Font(None, 60)
        sketch_font = pygame.font.Font(None, 40)
        sketch_surf = sketch_font.render(str(self.sketched_value), 0, SKETCH_COLOR)
        chip_surf = chip_font.render(str(self.value), 0, NUM_COLOR)
        blank_surf = chip_font.render('', 0, NUM_COLOR)

        if self.value == 0:
            if self.sketched_value == None:
                chip_rect = blank_surf.get_rect(
                    center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row))
                self.screen.blit(blank_surf, chip_rect)
            else:
                sketch_rect = sketch_surf.get_rect(
                    topleft=(5 + SQUARE_SIZE * self.col, 5 + SQUARE_SIZE * self.row))
                self.screen.blit(sketch_surf, sketch_rect)

        else:
            chip_rect = chip_surf.get_rect(
                center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.col, SQUARE_SIZE // 2 + SQUARE_SIZE * self.row))
            self.screen.blit(chip_surf, chip_rect)

        if self.clicked:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.col * SQUARE_SIZE-1, self.row * SQUARE_SIZE-1,
                                                        SQUARE_SIZE + 3, SQUARE_SIZE + 3), CELL_LINE_WIDTH)


