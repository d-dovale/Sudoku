# board class
from cell import Cell
import pygame, sys
from sudoku_generator import *
from constants import *


class Board:
    def __init__(self, width, height, screen, difficulty):  # Constructor for the Board class
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(9, difficulty)
        self.rows = 9
        self.cols = 9
        self.cells = [[Cell(self.board[i][j], i, j, self.screen)
                       for j in range(self.cols)] for i in range(self.rows)]

        self.empty_cells = []

    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()

    def draw(self):  # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.
        # draw lines
        for i in range(0, 4):  # draw thick horizontal lines
            pygame.draw.line(self.screen, LINE_COLOR, (0, GROUP_SIZE * i), (WIDTH, GROUP_SIZE * i), LINE_WIDTH)

        for i in range(0, 4):  # draw thick vertical lines
            pygame.draw.line(self.screen, LINE_COLOR, (GROUP_SIZE * i, 0), (GROUP_SIZE * i, HEIGHT), LINE_WIDTH)

        for i in range(1, 9):  # draw thin horizontal lines
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), CELL_LINE_WIDTH)

        for i in range(1, 9):  # draw thick vertical lines
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), CELL_LINE_WIDTH)

        for i in range(9):  # draw the cells values
            for j in range(9):
                self.cells[i][j].draw()

    def select(self, row, col):  # Marks current selected cell, the user can edit its value or sketched value.
        for i in range(9):  # sets all cells selected values to false so the other cells aren't outlined
            for j in range(9):
                self.cells[i][j].clicked = False
        self.cells[row][col].clicked = True  # sets the selected cells value to true
        self.click(row,col)

    def click(self, x, y):  # if (x, y) within the  board, returns tuple of clicked cell. Otherwise, returns None.
        clicked_row = x // SQUARE_SIZE
        clicked_col = y // SQUARE_SIZE
        if clicked_row in range(9) and clicked_col in range(9):
            coordinates = (clicked_row, clicked_col)
            return coordinates
        else:
            return None

    def coordinates(self,x,y):
        coords = []
        coords.append(x)
        coords.append(y)
        return coords

    def clear(self):  # Clears the value cell. Note that the user can only remove values/sketch filled by themselves.
        pass

    def sketch(self, value):  # Sets sketched value of selected cell to user value. displayed top left corner of cell
        for row in self.cells:
            for cell in row:
                if cell.clicked == True:
                    cell.set_sketched_value(value)

    def place_number(self):  # Sets value of current cell equal to user value. Called when user presses Enter
        self.find_empty()  # populate empty cells list
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].clicked == True:
                    if (i, j) in self.empty_cells:  # to check if value existed before
                        value = self.cells[i][j].sketched_value
                        if value == None:
                            self.cells[i][j].set_cell_value(0)
                        else:
                            self.cells[i][j].set_cell_value(value)

    def find_empty(self):  # Finds an empty cell and returns its row and col as a tuple(x, y).
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    cell_tuple = (i, j)
                    self.empty_cells.append(cell_tuple)

        return self.empty_cells

    def reset_to_original(self):  # Reset all cells in the board to their original values
        for i in range(9):
            for j in range(9):
                if (i, j) in self.empty_cells:  # to check if value existed before
                    self.cells[i][j].set_cell_value(0)  # set values to zero
                    self.cells[i][j].set_sketched_value(None)  # get rid of sketches
                    self.cells[i][j].clicked = False  # remove red highlight

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.cells[i][j].value
        pass

    def is_full(self):  # Returns a Boolean value indicating whether the board is full or not.
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:  # check if there are any empty cells
                    return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        onetonine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        compare = []
        for i in range(0, 3):  # the 3 rows
            for j in range(0, 3):  # the 3 cols
                val = self.board[row_start + i][col_start + j]
                compare.append(val)
        sorted_compare = sorted(compare)
        if sorted_compare == onetonine:
            return True
        return False

    def check_board(self):  # checks if sudoku solved correctly
        onetonine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        compare = []
        for i in range(9):  # checks if valid in row
            for j in range(9):
                num = self.board[i][j]
                compare.append(num)
            sorted_compare = sorted(compare)
            if sorted_compare == onetonine:
                compare = []
                continue
            else:
                return False

        for i in range(9):  # checks if valid in col
            for j in range(9):
                num = self.board[j][i]
                compare.append(num)
            sorted_compare = sorted(compare)
            if sorted_compare == onetonine:
                compare = []
                continue
            else:
                return False

        for i in range(9):
            for j in range(9):
                row_start = i // 3 * 3
                col_start = j // 3 * 3
                num = self.board[i][j]
                if self.valid_in_box(row_start, col_start, num):
                    continue
                else:
                    return False

        return True










