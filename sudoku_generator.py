import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return: None
    '''

    # initialized the class variables - jehan
    # helped jehan initialize the class variable of self.board - syed
    def __init__(self, row_length, removed_cells):
        # an array that is 9 x 9 and holds the entire board's values - jehan
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.row_length = row_length
        self.removed_cells = removed_cells
        # length of one box (3) - jehan
        self.box_length = 3

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    # getter function that just returns the attribute of the self object - taran
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    # printing function in which receives info from the self.board attribute and the get_board function - taran
    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end=" ")
        print()

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):  # checks if number in the row can be placed - syed
        if num in self.board[row]:
            return False  # returns when the number is already in that row - syed
        else:
            return True  # returns when the number is not in that row - syed

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        for item in range(9):
            if self.board[item][col] == num:
                return False
        # no else is needed, as it would throw a logic error and break out of the loop immediately - syed
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        for row in range(0, 3):  # the 3 rows - syed
            for col in range(0, 3):  # the 3 cols - syed
                if self.board[row_start + row][col_start + col] == num:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        box_row = row // 3 * 3  # gets the box row index of what box num is in - syed
        box_col = col // 3 * 3  # gets the box col index of what box num is in - syed
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(box_row, box_col, num):
            return True
        else:
            return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        # list of values that one grid has - jehan
        one_to_nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # the 3 rows in one grid - jehan
        for row in range(3):
            # the 3 cols in one grid - jehan
            for col in range(3):
                # randomly decide what value to input from list through index - syed
                index = random.randint(0, (len(one_to_nine) - 1))
                # get value using index - syed
                value = one_to_nine[index]
                # remove value so it isn't used again - syed
                one_to_nine.pop(index)
                # assign value to specific cell - syed
                self.board[row_start + row][col_start + col] = value

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        # fills the three boxes within the main diagonal of the board - jehan
        self.fill_box(6, 6)
        self.fill_box(3, 3)
        self.fill_box(0, 0)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        i = 0  # index var
        while i < self.removed_cells:  # while current removed is less than num removed needed - syed
            rand_row = random.randint(0, 8)  # random ints for row - syed
            rand_col = random.randint(0, 8)  # random ints for col - syed
            if self.board[rand_row][rand_col] != 0:  # if value isn't already 0, set it to zero - syed
                self.board[rand_row][rand_col] = 0
                i += 1  # increase index to show how many cells removed - syed
                continue
            else:  # when random cell is already 0, loop again to try a diff cell - syed
                continue


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
