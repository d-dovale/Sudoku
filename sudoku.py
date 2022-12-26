from sudoku_generator import *
from constants import *
import os
from board import *
import pygame, sys
from pygame.locals import QUIT


def draw_game_start(screen):
    # Initialize title font - syed
    start_title_font = pygame.font.Font(None, 80)
    start_subheading_font = pygame.font.Font(None, 60)
    button_font = pygame.font.Font(None, 50)

    # Color background - syed
    screen.fill(BG_COLOR)

    # Initialize and draw title - syed
    title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Initialize and draw subheading - syed
    subheading_surface = start_subheading_font.render("Select Game Mode:", 0, LINE_COLOR)
    subheading_rect = subheading_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 220))
    screen.blit(subheading_surface, subheading_rect)

    # Initialize buttons - syed
    # Initialize text first - syed
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    med_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))
    quit_text = button_font.render("Quit", 0, (255, 255, 255))

    # Initialize Easy button background color and text - syed
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    # Initialize Medium button background color and text - syed
    med_surface = pygame.Surface((med_text.get_size()[0] + 20, med_text.get_size()[1] + 20))
    med_surface.fill(LINE_COLOR)
    med_surface.blit(med_text, (10, 10))

    # Initialize Hard button background color and text - syed
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))


    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    # Initialize button rectangle - syed
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 300))
    med_rectangle = med_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 300))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH - (WIDTH // 4), HEIGHT // 2 + 300))
    quit_rectangle = quit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 300))

    # Draw buttons - dany
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(med_surface, med_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    # screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    difficulty = 30
                    return difficulty # If the mouse is on the medium button, we can return to main and set difficulty
                elif med_rectangle.collidepoint(event.pos):
                    difficulty = 40
                    return difficulty # If the mouse is on the medium button, we can return to main and set difficulty
                elif hard_rectangle.collidepoint(event.pos):
                    difficulty = 50
                    return difficulty # If the mouse is on the medium button, we can return to main and set difficulty
                elif quit_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
                    sys.exit()
        pygame.display.update()


def draw_game_over(screen, win):
    game_over_font = pygame.font.Font(None, 80)
    screen.fill(BG_COLOR)
    if win == True:
        text = 'Game Won!'
        game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
        game_over_rect = game_over_surf.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(game_over_surf, game_over_rect)
        # Initialize text first
        exit_text = button_font.render("Exit", 0, (255, 255, 255))
        # Initialize Exit button background color and text
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(LINE_COLOR)
        exit_surface.blit(exit_text, (10, 10))
        exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 165))
        screen.blit(exit_surface, exit_rectangle)
    else:
        text = "Game Over :("
        game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
        game_over_rect = game_over_surf.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(game_over_surf, game_over_rect)
        # Initialize restart button
        button_font = pygame.font.Font(None, 50)
        # Initialize text first
        exit_restart_text = button_font.render("Restart", 0, (255, 255, 255))
        # Initialize Restart button background color and text
        exit_restart_surface = pygame.Surface((exit_restart_text.get_size()[0] + 20, exit_restart_text.get_size()[1] + 20))
        exit_restart_surface.fill(LINE_COLOR)
        exit_restart_surface.blit(exit_restart_text, (10, 10))
        exit_restart_rectangle = exit_restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 165))
        screen.blit(exit_restart_surface, exit_restart_rectangle)









if __name__ == '__main__':
    outer_loop = True
    inner_loop = True
    game_over = False
    win = False
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT+100))
    pygame.display.set_caption("Sudoku")
    while outer_loop:
        inner_loop = True
        difficulty = draw_game_start(screen)  # Calls function to draw start screen

        screen.fill(BG_COLOR)
        # draw_lines()
        # middle_cell = Cell('o', 1, 1, 200, 200)
        # middle_cell.draw(screen)
        board = Board(WIDTH, HEIGHT, screen, difficulty)
        # board.print_board()
        board.draw()
        board.print_board()  # print board to console
        print()

        # Initialize game buttons - syed
        button_font = pygame.font.Font(None, 50)
        # Initialize text first - jehan
        reset_text = button_font.render("Reset", 0, (255, 255, 255))
        restart_text = button_font.render("Restart", 0, (255, 255, 255))
        exit_text = button_font.render("Exit", 0, (255, 255, 255))

        # Initialize Reset button background color and text - syed
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surface.fill(LINE_COLOR)
        reset_surface.blit(reset_text, (10, 10))

        # Initialize Restart button background color and text - syed
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill(LINE_COLOR)
        restart_surface.blit(restart_text, (10, 10))

        # Initialize Exit button background color and text - syed
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(LINE_COLOR)
        exit_surface.blit(exit_text, (10, 10))

        # Initialize game button rectangle - syed
        reset_rectangle = reset_surface.get_rect(center=(SQUARE_SIZE * 1.5, HEIGHT // 2 + 365))
        restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 365))
        exit_rectangle = exit_surface.get_rect(center=(WIDTH - (SQUARE_SIZE * 1.5), HEIGHT // 2 + 365))

        # Draw game buttons - syed
        screen.blit(reset_surface, reset_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)
        coords = board.coordinates(0,0) #sets the location of the starting current row/column at 0,0
        board.select(0,0) #starts the game with a undrawn select box that doesnt brake the arrow keys with no select box orignially you dont click
        while inner_loop:
            if coords[0] > 7: #if arrow keys go past the boundary of grid they reset to the opposite side
                coords[0] = -1

            if coords[1] > 7: #if arrow keys go past the boundary of grid they reset to the opposite side
                coords[1] = -1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # if user hits 'x' to close - syed
                    sys.exit()
                
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset_rectangle.collidepoint(event.pos):  # if user clicks reset button - syed
                        print('reset')
                        board.reset_to_original()  # reset board and display everything
                        screen.fill(BG_COLOR)
                        board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                    if restart_rectangle.collidepoint(event.pos):  # if user clicks restart button
                        print('restart')
                        inner_loop = False
                        break

                    if exit_rectangle.collidepoint(event.pos):  # if user clicks exit button
                        # If the mouse is on the exit button, exit the program
                        print('exit')
                        sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    coord_tuple = board.click(int(event.pos[1]), (int(event.pos[0])))

                    if coord_tuple != None:  # check if player clicked on board
                        board.select(coord_tuple[0], coord_tuple[1])  # outlines selected cell
                        print(coord_tuple)
                        coords[0] = coord_tuple[0] #aligns arrow key coords to mouse coords
                        coords[1] = coord_tuple[1]
                        board.draw()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        sketched_val = 1
                        board.sketch(1)  # print sketched number than print everything on top again so stuff is hidden
                        screen.fill(BG_COLOR)
                        board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        sketched_val = 2
                        board.sketch(2)  # print sketched number than print everything on top again so stuff is hidden
                        screen.fill(BG_COLOR)
                        board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        sketched_val = 3
                        board.sketch(3)  # print sketched number than print everything on top again so stuff is hidden
                        screen.fill(BG_COLOR)
                        board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_4:
                        sketched_val = 4
                        board.sketch(4)  # print sketched number than print everything on top again so stuff is hidden
                        screen.fill(BG_COLOR)
                        board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_5:
                        sketched_val = 5
                        board.sketch(5)  # print sketched number than print everything on top again so stuff is hidden
                        screen.fill(BG_COLOR)
                        board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_6:
                        sketched_val = 6
                        board.sketch(6)  # print sketched number than print everything on top again so stuff is hidden
                        screen.fill(BG_COLOR)
                        board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_7:
                        sketched_val = 7
                        board.sketch(7)  # print sketched number than print everything on top again so stuff is hidden
                        screen.fill(BG_COLOR)
                        board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_8:
                        sketched_val = 8
                        board.sketch(8)  # print sketched number than print everything on top again so stuff is hidden
                        screen.fill(BG_COLOR)
                        board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_9:
                        sketched_val = 9
                        board.sketch(9)  # print sketched number than print everything on top again so stuff is hidden
                        screen.fill(BG_COLOR)
                        board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # set user value then print everything again so stuff is hidden
                        board.place_number()
                        screen.fill(BG_COLOR)
                        board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:  # allows the selected box to move up
                        board.select(coords[0]-1,coords[1])
                        coords[0] = (coords[0]-1)
                        board.draw()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # allows the selected box to move down
                        board.select(coords[0]+1,coords[1])
                        coords[0] = (coords[0]+1)
                        board.draw()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:  # allows the selected box to move left
                        board.select(coords[0],coords[1]-1)
                        coords[1] = (coords[1]-1)
                        board.draw()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:  # allows the selected box to move right
                        board.select(coords[0],coords[1]+1)
                        coords[1] = (coords[1]+1)
                        board.draw()
                



                        if board.is_full():  # check if board if full
                            game_over_font = pygame.font.Font(None, 80)
                            board.update_board()
                            print(board.check_board())

                            if board.check_board():
                                game_over = True
                                win = True
                                screen.fill(BG_COLOR)
                                text = "Game Won!"  # display text
                                game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
                                game_over_rect = game_over_surf.get_rect(
                                    center=(WIDTH // 2, HEIGHT // 2 - 100))
                                screen.blit(game_over_surf, game_over_rect)

                                over_exit_rectangle = exit_surface.get_rect(
                                    center=(WIDTH // 2, HEIGHT // 2 + 165))
                                screen.blit(exit_surface, over_exit_rectangle)

                            else:
                                win = False
                                screen.fill(BG_COLOR)  # make backgroud

                                text = "Game Over :("  # display text
                                game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
                                game_over_rect = game_over_surf.get_rect(
                                    center=(WIDTH // 2, HEIGHT // 2 - 100))
                                screen.blit(game_over_surf, game_over_rect)

                                screen.blit(restart_surface, restart_rectangle)  # display button



            pygame.display.update()


            # Game is over - jehan
            if game_over:
                # draw_game_over(screen, win)
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if over_exit_rectangle.collidepoint(event.pos):  # if user clicks exit button
                                # If the mouse is on the exit button, exit the program
                                print('exit')
                                sys.exit()
               # inner_loop = False
                    pygame.display.update()


            pygame.display.update()





