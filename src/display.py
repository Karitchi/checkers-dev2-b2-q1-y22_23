import pygame
from src.constants import BEIGE, BROWN, GREY, TILE_SIZE, WHITE, BLACK, RED


def draw_checkerboard(window, checkerboard):
    for y in range(8):
        for x in range(8):
            if y % 2:
                if x % 2:
                    pygame.draw.rect(
                        window, BROWN, (x*TILE_SIZE, (7 - y)*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                else:
                    pygame.draw.rect(
                        window, BEIGE, (x*TILE_SIZE, (7 - y)*TILE_SIZE, TILE_SIZE, TILE_SIZE))

            else:
                if x % 2:
                    pygame.draw.rect(
                        window, BEIGE, (x*TILE_SIZE, (7 - y)*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                else:
                    pygame.draw.rect(
                        window, BROWN, (x*TILE_SIZE, (7 - y)*TILE_SIZE, TILE_SIZE, TILE_SIZE))


def draw_pawns(window, checkerboard):
    for y in range(len(checkerboard)):
        for x in range(len(checkerboard[y])):
            if checkerboard[y][x].pawn != None:
                if checkerboard[y][x].pawn.color == WHITE:
                    pygame.draw.circle(
                        window, WHITE, (x*TILE_SIZE + TILE_SIZE/2, (7 - y)*TILE_SIZE + TILE_SIZE/2), TILE_SIZE/2.5)
                else:
                    pygame.draw.circle(
                        window, BLACK, (x*TILE_SIZE + TILE_SIZE/2, (7 - y)*TILE_SIZE + TILE_SIZE/2), TILE_SIZE/2.5)
                    pass


def draw_buttons(window):
    pygame.draw.rect(
        window, RED, (700, 800, 100, 50))


def draw_hints(window, valid_moves):
    for move in valid_moves:
        pygame.draw.circle(
            window, GREY, (move[1] * TILE_SIZE + TILE_SIZE/2, (7 - move[0]) * TILE_SIZE + TILE_SIZE/2), TILE_SIZE/8)
