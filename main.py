import pygame
import sys
import map_generator
from time import sleep

pygame.font.init()


def winner_menu():
    restart_button = pygame.image.load("restart.png")
    exit_button = pygame.image.load("exit.png")
    record_text = font.render("WIN!", True, WHITE)
    menu_run = True
    while menu_run:
        for event in pygame.event.get():  # перебираем очередь событий для каждого события
            if event.type == pygame.QUIT:  # если нажали на красный крестик
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if size[0] // 2 - 77 < x < size[0] // 2 - 77 + 134 and size[1] // 2 - 100 < y < size[1] // 2 - 100 + 47:
                    sys.exit()
                if size[0] // 2 - 77 < x < size[0] // 2 - 77 + 134 and size[1] // 2 + 100 < y < size[1] // 2 + 100 + 47:
                    menu_run = False
        window.fill(BLACK)
        window.blit(record_text, [size[0] // 2 - 65, size[1] // 2])
        window.blit(exit_button, [size[0] // 2 - 77, size[1] // 2 - 100])
        window.blit(restart_button, [size[0] // 2 - 77, size[1] // 2 + 100])
        pygame.display.update()


def open_neighboring(r, c):
    if r != 0:  # если есть сосед сверху
        if level_flags[r - 1][c] == 'h':
            level_flags[r - 1][c] = 'o'
            if level[r - 1][c] == 0:  # если это мина
                open_neighboring(r - 1, c)
    if r != counter_cells_height - 1:  # есть ли сосед снизу
        if level_flags[r + 1][c] == 'h':
            level_flags[r + 1][c] = 'o'
            if level[r + 1][c] == 0:  # если это мина
                open_neighboring(r + 1, c)
    if c != 0:  # есть ли сосед слева
        if level_flags[r][c - 1] == 'h':
            level_flags[r][c - 1] = 'o'
            if level[r][c - 1] == 0:
                open_neighboring(r, c - 1)
    if c != counter_cells_width - 1:
        if level_flags[r][c + 1] == 'h':
            level_flags[r][c + 1] = 'o'
            if level[r][c + 1] == 0:
                open_neighboring(r, c + 1)
    if r != 0 and c != 0:  # если у ячейки есть сосед слева-сверху
        if level_flags[r - 1][c - 1] == 'h':
            level_flags[r - 1][c - 1] = 'o'
            if level[r - 1][c - 1] == 0:
                open_neighboring(r - 1, c - 1)
    if r != 0 and c != counter_cells_width - 1:  # если у ячейки есть сосед справа-сверху
        if level_flags[r - 1][c + 1] == 'h':
            level_flags[r - 1][c + 1] = 'o'
            if level[r - 1][c + 1] == 0:
                open_neighboring(r - 1, c + 1)
    if c != 0 and r != counter_cells_height - 1:
        if level_flags[r + 1][c - 1] == 'h':
            level_flags[r + 1][c - 1] = 'o'
            if level[r + 1][c - 1] == 0:
                open_neighboring(r + 1, c - 1)
    if c != counter_cells_width - 1 and r != counter_cells_height - 1:
        if level_flags[r + 1][c + 1] == 'h':
            level_flags[r + 1][c + 1] = 'o'
            if level[r + 1][c + 1] == 0:
                open_neighboring(r + 1, c + 1)


size = 600, 600
cell_size = 40
window = pygame.display.set_mode(size)
counter_cells_width = size[0] // cell_size  # кол-во клеток в ширину
counter_cells_height = size[1] // cell_size  # кол-во клеток в высоту

font = pygame.font.Font("emulogic.ttf", 30)

hide_cell = pygame.image.load("hide.png")
hide_cell = pygame.transform.scale(hide_cell, [cell_size, cell_size])
mine = pygame.image.load("mine.png")
mine = pygame.transform.scale(mine, [cell_size, cell_size])
flag_image = pygame.image.load('flag.png')
flag_image = pygame.transform.scale(flag_image, [cell_size, cell_size])

nums_images = []
for n in range(9):
    img = pygame.image.load(f'{n}.png')
    img = pygame.transform.scale(img, [cell_size, cell_size])
    nums_images.append(img)

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (3, 0, 199)
RED = (255, 0, 0)
GREEN = (94, 255, 0)
WHITE = (255, 255, 255)

level, counter_of_mines = map_generator.generate_sweeper_map(size[0] // cell_size, size[1] // cell_size, 0.13)
flags_counter = 0

# check level
for r in range(15):
    for c in range(15):
        mines_counter = 0
        if c > 0:  # left
            if level[r][c - 1] == 'm':
                mines_counter += 1
        if c < 14:  # right
            if level[r][c + 1] == 'm':
                mines_counter += 1
        if r > 0:  # up
            if level[r - 1][c] == 'm':
                mines_counter += 1
        if r < 14:  # down
            if level[r + 1][c] == 'm':
                mines_counter += 1
        if r > 0 and c > 0:  # up-left
            if level[r - 1][c - 1] == 'm':
                mines_counter += 1
        if r > 0 and c < 14:  # up-right
            if level[r - 1][c + 1] == 'm':
                mines_counter += 1
        if r < 14 and c > 0:  # down-left
            if level[r + 1][c - 1] == 'm':
                mines_counter += 1
        if r < 14 and c < 14:  # down-right
            if level[r + 1][c + 1] == 'm':
                mines_counter += 1
        if level[r][c] != 'm':
            level[r][c] = mines_counter

level_flags = [['h' for i in range(15)] for j in range(15)]  # [["h"] * 15] * 15
# level_flags[0][0] = 'o'
# for r in level_flags:
#     print(*r)

for row in level:
    print(' '.join(map(str, row)))

wins_counter = 0

run = True
while run:
    window.fill([0, 0, 0])
    pygame.display.set_caption(f'mines = {counter_of_mines}, flags = {flags_counter}')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            row_ind, col_ind = mouse_y // cell_size, mouse_x // cell_size
            if event.button == 1:
                if level[row_ind][col_ind] == 0:
                    open_neighboring(row_ind, col_ind)
                level_flags[row_ind][col_ind] = 'o'
                if level[row_ind][col_ind] == "m":
                    for i in range(len(level)):
                        for j in range(len(level[i])):
                            if level[i][j] == 'm':
                                window.blit(mine, [j * cell_size, i * cell_size])
                            if level[i][j] != 'm' and level_flags[i][j] == 'o':
                                window.blit(nums_images[level[i][j]], [j * cell_size, i * cell_size])
                    pygame.display.update()
                    sleep(3)
                    sys.exit()
                level_flags[row_ind][col_ind] = 'o'
            if event.button == 3:
                if level_flags[row_ind][col_ind] == 'h':
                    if level[row_ind][col_ind] == "m":
                        wins_counter += 1
                    level_flags[row_ind][col_ind] = 'f'
                    flags_counter += 1
                elif level_flags[row_ind][col_ind] == 'f':
                    if level[row_ind][col_ind] == "m":
                        wins_counter -= 1
                    level_flags[row_ind][col_ind] = 'h'
                    flags_counter -= 1
    #    pygame.draw.rect(window, WHITE, [0, 0, cell_size, cell_size])
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] != 'm' and level_flags[i][j] == 'o':
                window.blit(nums_images[level[i][j]], [j * cell_size, i * cell_size])
            if level[i][j] == "m" and level_flags[i][j] == 'o':
                window.blit(mine, [j * cell_size, i * cell_size])
            if level_flags[i][j] == 'f':
                window.blit(flag_image, [j * cell_size, i * cell_size])
            if level_flags[i][j] == 'h':
                window.blit(hide_cell, [j * cell_size, i * cell_size])
    if wins_counter == counter_of_mines and flags_counter == counter_of_mines:
        winner_menu()
        level, counter_of_mines = map_generator.generate_sweeper_map(size[0] // cell_size, size[1] // cell_size, 0.12)
        flags_counter = 0
        wins_counter = 0
        level_flags = [['h' for i in range(15)] for j in range(15)]
        print("--------")
        for row in level:
            print(' '.join(map(str, row)))
        for r in range(15):
            for c in range(15):
                mines_counter = 0
                if c > 0:  # left
                    if level[r][c - 1] == 'm':
                        mines_counter += 1
                if c < 14:  # right
                    if level[r][c + 1] == 'm':
                        mines_counter += 1
                if r > 0:  # up
                    if level[r - 1][c] == 'm':
                        mines_counter += 1
                if r < 14:  # down
                    if level[r + 1][c] == 'm':
                        mines_counter += 1
                if r > 0 and c > 0:  # up-left
                    if level[r - 1][c - 1] == 'm':
                        mines_counter += 1
                if r > 0 and c < 14:  # up-right
                    if level[r - 1][c + 1] == 'm':
                        mines_counter += 1
                if r < 14 and c > 0:  # down-left
                    if level[r + 1][c - 1] == 'm':
                        mines_counter += 1
                if r < 14 and c < 14:  # down-right
                    if level[r + 1][c + 1] == 'm':
                        mines_counter += 1
                if level[r][c] != 'm':
                    level[r][c] = mines_counter

    pygame.display.update()
