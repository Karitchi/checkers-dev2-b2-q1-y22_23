import pygame

from src.constants import WHITE, BLACK, TILE_SIZE
from src.checkerboard import Checkerboard
from src.pawn import Pawn


def set_tiles():
    checkerboard = []
    color = WHITE

    for y in range(8):
        if y > 2:
            color = BLACK

        checkerboard.append([])
        for x in range(8):
            if y % 2:
                if y in range(3, 5):
                    checkerboard[y].append(Checkerboard(None))
                elif x % 2:
                    checkerboard[y].append(Checkerboard(Pawn(x, y, color)))
                else:
                    checkerboard[y].append(Checkerboard(None))

            else:
                if y in range(3, 5):
                    checkerboard[y].append(Checkerboard(None))
                elif x % 2 == 0:
                    checkerboard[y].append(Checkerboard(Pawn(x, y, color)))
                else:
                    checkerboard[y].append(Checkerboard(None))

    return checkerboard


def get_cursor_position():
    cursor = pygame.mouse.get_pos()
    return cursor


def search_tile(cursor):
    return (7 - (cursor[1] // TILE_SIZE), cursor[0] // TILE_SIZE)


def search_valid_moves(clicked_tile, checkerboard, turn_color):
    valid_moves = []
    vertical = []
    horizontal = [-1, 1]

    if turn_color == WHITE:
        vertical.append(1)
    elif turn_color == BLACK:
        vertical.append(-1)
    else:
        vertical.append(1)
        vertical.append(-1)

    for y in vertical:
        for x in horizontal:

            # check if coords are smaller than 0 or bigger than 7
            if clicked_tile[0] + y < 0 or clicked_tile[1] + x < 0 or clicked_tile[0] + y > 7 or clicked_tile[1] + x > 7:
                continue

            # find playable empty tiles (no jumps)
            if checkerboard[clicked_tile[0] + y][clicked_tile[1] + x].pawn == None:
                valid_moves.append(
                    (clicked_tile[0] + y, clicked_tile[1] + x))

            # find playable jumps
            elif checkerboard[clicked_tile[0] + y][clicked_tile[1] + x].pawn.color != turn_color:
                if clicked_tile[0] + (2 * y) < 0 or clicked_tile[1] + (2 * x) < 0 or clicked_tile[0] + (2 * y) > 7 or clicked_tile[1] + (2 * x) > 7:
                    continue

                if checkerboard[clicked_tile[0] + (2 * y)][clicked_tile[1] + (2 * x)].pawn == None:
                    valid_moves.append(
                        (clicked_tile[0] + (2 * y), clicked_tile[1] + (2 * x)))

    return valid_moves


def check_move_validity(clicked_tile, valid_moves):
    for move in valid_moves:
        if move == clicked_tile:
            return True
    return False


def move(clicked_tile, selected_pawn, checkerboard):
    # swap place of selected pawn and clicked tile in checkerboard
    checkerboard[selected_pawn[0]][selected_pawn[1]], checkerboard[clicked_tile[0]][clicked_tile[1]
                                                                                    ] = checkerboard[clicked_tile[0]][clicked_tile[1]], checkerboard[selected_pawn[0]][selected_pawn[1]]


def eat(clicked_tile, selected_pawn, checkerboard):
    if abs(clicked_tile[0] - selected_pawn[0]) == 2:
        pawn_to_eat = (int((clicked_tile[0] + selected_pawn[0])/2),
                       int((clicked_tile[1] + selected_pawn[1])/2))
        
        checkerboard[pawn_to_eat[0]][pawn_to_eat[1]].pawn = None
