import pygame
from main import cube, turn
from find_algorithms import *
import time
import random as r
from Variables import *


def draw(surface, points, colors):
    for i in range(3):
        for p_index, point in enumerate(points[i]):
            if point and all(point):
                pygame.draw.polygon(surface, colors[i][p_index], point)
            else:
                break


def draw_lines(surface):
    pygame.draw.line(surface, 0, (100, 200), (300, 100), 4)
    pygame.draw.line(surface, 0, (167, 233), (367, 133), 4)
    pygame.draw.line(surface, 0, (234, 266), (434, 166), 4)
    pygame.draw.line(surface, 0, (300, 300), (500, 200), 4)

    pygame.draw.line(surface, 0, (100, 200), (300, 300), 4)
    pygame.draw.line(surface, 0, (167, 167), (367, 267), 4)
    pygame.draw.line(surface, 0, (233, 133), (433, 233), 4)
    pygame.draw.line(surface, 0, (300, 100), (500, 200), 4)

    pygame.draw.line(surface, 0, (100, 274), (300, 374), 4)
    pygame.draw.line(surface, 0, (100, 348), (300, 448), 4)
    pygame.draw.line(surface, 0, (100, 421), (300, 521), 4)

    pygame.draw.line(surface, 0, (100, 200), (100, 423), 4)
    pygame.draw.line(surface, 0, (167, 233), (167, 456), 4)
    pygame.draw.line(surface, 0, (234, 266), (234, 489), 4)
    pygame.draw.line(surface, 0, (300, 300), (300, 521), 4)

    pygame.draw.line(surface, 0, (366, 266), (366, 489), 4)
    pygame.draw.line(surface, 0, (432, 233), (432, 456), 4)
    pygame.draw.line(surface, 0, (500, 200), (500, 423), 4)

    pygame.draw.line(surface, 0, (300, 374), (500, 274), 4)
    pygame.draw.line(surface, 0, (300, 448), (500, 348), 4)
    pygame.draw.line(surface, 0, (300, 521), (500, 421), 4)


def draw_back(surface, window_x, window_y):
    for i in range(0, window_x, int(window_x / 15)):
        pygame.draw.line(surface, (100, 60, 40), (i, 0), (i, window_y), 3)

    for i in range(0, window_y, int(window_y / 10)):
        pygame.draw.line(surface, (100, 60, 40), (0, i), (window_x, i), 3)


def draw_buttons(surface, active_button=None):
    for arrow in arrow_points:
        pygame.draw.polygon(surface, "gray", arrow)
    for button in button_points:
        pygame.draw.rect(surface, "gray", button)
    if active_button[0] == "Arrow":
        pygame.draw.polygon(surface, dark_grey, arrow_points[active_button[1]])
    elif active_button[0] == "Move":
        pygame.draw.rect(surface, dark_grey, button_points[active_button[1]])


def draw_text(surface):
    turns = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'"]
    f1 = pygame.font.SysFont('arial', 26)
    R_text = f1.render("R", True, "black")
    Rp_text = f1.render("R'", True, "black")
    L_text = f1.render("L", True, "black")
    Lp_text = f1.render("L'", True, "black")
    U_text = f1.render("U", True, "black")
    Up_text = f1.render("U'", True, "black")
    D_text = f1.render("D", True, "black")
    Dp_text = f1.render("D'", True, "black")
    F_text = f1.render("F", True, "black")
    Fp_text = f1.render("F'", True, "black")
    B_text = f1.render("B", True, "black")
    Bp_text = f1.render("B'", True, "black")
    surface.blit(R_text, (953, 45))
    surface.blit(Rp_text, (1032, 45))
    surface.blit(L_text, (955, 105))
    surface.blit(Lp_text, (1034, 105))
    surface.blit(U_text, (953, 165))
    surface.blit(Up_text, (1032, 165))
    surface.blit(D_text, (953, 225))
    surface.blit(Dp_text, (1032, 225))
    surface.blit(F_text, (953, 285))
    surface.blit(Fp_text, (1032, 285))
    surface.blit(B_text, (953, 345))
    surface.blit(Bp_text, (1032, 345))
    pygame.display.update()


def render(surface, colors, button=[None, None]):
    draw_back(surface, window_x, window_y)
    draw_buttons(surface, button)
    draw(surface, left_points, colors)
    draw_lines(surface)
    pygame.display.flip()


def copy_cube(ccube):
    new_cube = []
    for l in ccube:
        new_cube.append(l.copy())

    return new_cube


def scramble(ccube, tturns):
    for i in tturns:
        turn(ccube, i)


def equal(ccube1, ccube2):
    for side in ccube1:
        if side not in ccube2:
            return False

    return True


def difference(ccube1, ccube2):
    dif = 0
    for side in range(6):
        for sq in range(9):
            if ccube1[side][sq] != ccube2[side][sq]:
                dif += 1
    return dif


def simulate(s_cube, turn_names, scrambled_cube=None):
    solved_cube = copy_cube(s_cube)
    count_turns = 0
    if not scrambled_cube:
        while True:
            for turn_name in turn_names:
                turn(s_cube, turn_name)
                count_turns += 1

                if equal(s_cube, solved_cube):
                    return count_turns, count_turns/len(turn_names)
    else:
        closest_state = [copy_cube(scrambled_cube)]
        fewer_moves = difference(scrambled_cube, solved_cube)
        fewer_moves_turn = 0
        was_closest = False
        unsolved_cube = copy_cube(scrambled_cube)
        while True:
            for turn_name in turn_names:
                turn(scrambled_cube, turn_name)
                count_turns += 1
                dif = difference(scrambled_cube, solved_cube)
                print(dif)
                if dif == 0:
                    print("Solved!")
                    return count_turns, count_turns/len(turn_names)
                elif equal(scrambled_cube, unsolved_cube):
                    if was_closest:
                        print(f"Closest state{closest_state}\nit was {fewer_moves} moves apart \nand it was {fewer_moves_turn} turn")
                    return f"Impossible:( \n{count_turns}, {count_turns/len(turn_names)} was done btw"
                if dif < fewer_moves:
                    print(dif, fewer_moves)
                    fewer_moves = dif
                    closest_state = scrambled_cube
                    fewer_moves_turn = count_turns
                    was_closest = True


def animate(ccube, turns):
    window_x = 1200
    window_y = 600
    pygame.init()
    window = pygame.display.set_mode((window_x, window_y))
    colors = ccube[0], ccube[1], ccube[2]
    run = True
    change = -1

    while run:
        window.fill((150, 90, 60))
        draw_back(window, window_x, window_y)
        render(window, colors)
        time.sleep(2)
        change += 1
        for i in turns:
            turn(ccube, i)
            render(window, colors)
            time.sleep(3)

        time.sleep(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


def click(mouse):
    if 610 <= mouse[0] <= 650:
        if 275 <= mouse[1] <= 350:
            turn(cube, "L'")
            turn(cube, "M'")
            turn(cube, "R")
        elif 400 <= mouse[1] <= 475:
            turn(cube, "L")
            turn(cube, "M")
            turn(cube, "R'")
    elif 350 <= mouse[1] <= 400:
        if 650 <= mouse[0] <= 725:
            turn(cube, "U'")
            turn(cube, "E")
            turn(cube, "D")
        elif 525 <= mouse[0] <= 600:
            turn(cube, "U")
            turn(cube, "E'")
            turn(cube, "D'")
    if 935 <= mouse[0] <= 985:
        if 35 <= mouse[1] <= 85:
            turn(cube, "R")
        elif 95 <= mouse[1] <= 145:
            turn(cube, "L")
        elif 155 <= mouse[1] <= 205:
            turn(cube, "U")
        elif 215 <= mouse[1] <= 265:
            turn(cube, "D")
        elif 275 <= mouse[1] <= 325:
            turn(cube, "F")
        elif 335 <= mouse[1] <= 385:
            turn(cube, "B")
    elif 1015 <= mouse[0] <= 1065:
        if 35 <= mouse[1] <= 85:
            turn(cube, "R'")
        elif 95 <= mouse[1] <= 145:
            turn(cube, "L'")
        elif 155 <= mouse[1] <= 205:
            turn(cube, "U'")
        elif 215 <= mouse[1] <= 265:
            turn(cube, "D'")
        elif 275 <= mouse[1] <= 325:
            turn(cube, "F'")
        elif 335 <= mouse[1] <= 385:
            turn(cube, "B'")


def check_active_button(mouse):
    active_button = [None, None]
    if 610 <= mouse[0] <= 650:
        if 275 <= mouse[1] <= 350:
            active_button = ("Arrow", 0)
        elif 400 <= mouse[1] <= 475:
            active_button = ("Arrow", 2)
    elif 350 <= mouse[1] <= 400:
        if 650 <= mouse[0] <= 725:
            active_button = ("Arrow", 1)
        elif 525 <= mouse[0] <= 600:
            active_button = ("Arrow", 3)
    if 935 <= mouse[0] <= 985:
        if 35 <= mouse[1] <= 85:
            active_button = ("Move", 0)
        elif 95 <= mouse[1] <= 145:
            active_button = ("Move", 2)
        elif 155 <= mouse[1] <= 205:
            active_button = ("Move", 4)
        elif 215 <= mouse[1] <= 265:
            active_button = ("Move", 6)
        elif 275 <= mouse[1] <= 325:
            active_button = ("Move", 8)
        elif 335 <= mouse[1] <= 385:
            active_button = ("Move", 10)
    elif 1015 <= mouse[0] <= 1065:
        if 35 <= mouse[1] <= 85:
            active_button = ("Move", 1)
        elif 95 <= mouse[1] <= 145:
            active_button = ("Move", 3)
        elif 155 <= mouse[1] <= 205:
            active_button = ("Move", 5)
        elif 215 <= mouse[1] <= 265:
            active_button = ("Move", 7)
        elif 275 <= mouse[1] <= 325:
            active_button = ("Move", 9)
        elif 335 <= mouse[1] <= 385:
            active_button = ("Move", 11)

    return active_button


def play(sscramble=None):
    pygame.init()
    window = pygame.display.set_mode((window_x, window_y))
    colors = cube[0], cube[1], cube[2]
    run = True
    if sscramble:
        scramble_turns = sscramble
    else:
        scramble_turns = random_turns()
    scramble(cube, scramble_turns)
    active_button = [None, None]
    window.fill((150, 90, 60))
    render(window, colors, active_button)
    draw_text(window)
    change_state = 0
    print(scramble_turns)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(mouse)
                render(window, colors, active_button)
                draw_text(window)

        mouse = pygame.mouse.get_pos()
        active_button = check_active_button(mouse)

        if active_button != [None, None] and change_state != 2:
            change_state = 1
        if change_state == 1:
            render(window, colors, active_button)
            draw_text(window)
            change_state = 2
        if active_button == [None, None] and change_state == 2:
            render(window, colors, active_button)
            draw_text(window)
            change_state = 0

    pygame.quit()


def random_turns():
    turn_notation = [["R", "R'", "R2"], ["L", "L'", "L2"],
                     ["U", "U'", "U2"], ["D", "D'", "D2"],
                     ["F", "F'", "F2"], ["B", "B'", "B2"]]

    turn_notation_extended = ["R",  "L",  "U",  "D",  "F",  "B",  "M",  "E",  "S",
                              "R'", "L'", "U'", "D'", "F'", "B'", "M'", "E'", "S'",
                              "R2", "L2", "U2", "D2", "F2", "B2", "M2", "E2", "S2"]

    previously_used = r.choice(r.choice(turn_notation))
    alg = [previously_used]
    
    for _ in range(20):
        using = r.choice(r.choice(turn_notation))
        while using[0] == previously_used[0]:
            using = r.choice(r.choice(turn_notation))
        alg.append(using)
        previously_used = using

    return alg


def main():
    scramble_turns = ["R", "R'"]
    # scramble_turns = ["E"]
    # scrambled_cube = copy_cube(cube)
    # scramble(cube, scramble_turns)
    # turns = ['R', "U'", 'B', "U'", 'D2']
    # max_moves = 0
    # max_cycles = 0
    # max_moves_alg = []
    # max_cycles_alg = []
    # for _ in range(10000):
    #     turns = random_turns()
    #     moves, cycles = simulate(cube, turns)
    #     if moves > max_moves:
    #         max_moves = moves
    #         max_moves_alg = turns
    #     if cycles > max_cycles:
    #         max_cycles = cycles
    #         max_cycles_alg = turns
    # print(max_cycles)
    # print(max_cycles_alg)
    # print(max_moves)
    # print(max_moves_alg)

    # alt_cube = [cube[2], cube[4], cube[0], cube[5], cube[1], cube[3]]
    # animate(cube, ["M"])
    # print(find_algorithm7(cube))
    # print(cube)
    # turn(cube, "R")
    # turn(cube, "E")
    # print(cube)
    # turn(cube, "E")
    # print(cube)
    play()


if __name__ == '__main__':
    main()
