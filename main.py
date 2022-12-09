import sys
import pygame
import pygame_widgets

from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from src.game import get_cursor_position, move, search_valid_moves, set_tiles, search_tile, check_move_validity, eat
from src.display import draw_checkerboard, draw_hints, draw_pawns
from src.constants import WHITE, BLACK, RED, DARKER_RED, DARK_RED

turn_color = WHITE


def main():
    pygame.init()
    window = pygame.display.set_mode((800, 850))
    pygame.display.set_caption("checkers")
    clock = pygame.time.Clock()

    checkerboard = set_tiles()
    selected_pawn = ()
    draw_checkerboard(window, checkerboard)
    draw_pawns(window, checkerboard)
    valid_moves = []

    def change_turn():
        global turn_color
        turn_color = BLACK if turn_color == WHITE else WHITE

    def print_textbox1():
        f = open("players_list.txt", "a")
        f = open("players_list.txt", "r")

        for line in f:
            if line == textbox1.getText() + "\n":
                f.close()
                return 0

        f = open("players_list.txt", "a")
        f.write(textbox1.getText() + "\n")
        f.close()

    def print_textbox2():
        f = open("players_list.txt", "a")
        f = open("players_list.txt", "r")

        for line in f:
            if line == textbox2.getText() + "\n":
                f.close()
                return 0

        f = open("players_list.txt", "a")
        f.write(textbox2.getText() + "\n")
        f.close()

    button = Button(
        window,
        400,
        800,
        200,
        50,
        textColour=WHITE,
        inactiveColour=RED,
        hoverColour=DARKER_RED,
        pressedColour=DARK_RED,
        text='Finish turn',
        onClick=change_turn)

    textbox1 = TextBox(
        window,
        0,
        800,
        200,
        50,
        fontSize=32,
        borderThickness=1,
        borderColour=BLACK,
        textColour=BLACK,
        placeholderText='Player 1 name',
        onSubmit=print_textbox1)

    textbox2 = TextBox(
        window,
        200,
        800,
        200,
        50,
        fontSize=32,
        borderThickness=1,
        borderColour=BLACK,
        textColour=BLACK,
        placeholderText='Player 2 name',
        onSubmit=print_textbox2)

    while True:
        clock.tick(60)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor = get_cursor_position()
                clicked_tile = search_tile(cursor)

                # if pawn on clicked tile
                if checkerboard[clicked_tile[0]][clicked_tile[1]].pawn != None:
                    selected_pawn = clicked_tile
                    draw_checkerboard(window, checkerboard)
                    draw_pawns(window, checkerboard)

                    # if color of selected pawn == turn_color
                    if checkerboard[clicked_tile[0]][clicked_tile[1]].pawn.color == turn_color:
                        valid_moves = search_valid_moves(
                            clicked_tile, checkerboard, turn_color)
                        draw_hints(window, valid_moves)

                else:
                    draw_checkerboard(window, checkerboard)
                    draw_pawns(window, checkerboard)
                    is_move_valid = check_move_validity(
                        clicked_tile, valid_moves)
                    if is_move_valid:
                        move(clicked_tile, selected_pawn, checkerboard)
                        eat(clicked_tile, selected_pawn, checkerboard)

                        # turn_color = BLACK if turn_color == WHITE else WHITE
                        draw_checkerboard(window, checkerboard)
                        draw_pawns(window, checkerboard)

            if event.type == pygame.QUIT:
                sys.exit()

        pygame_widgets.update(events)
        pygame.display.update()


main()
