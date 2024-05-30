from test import copy_cube, simulate


def find_algorithm2(ccube):
    turn_notation = ["R", "L", "U", "D", "F", "B",
                     "R'", "L'", "U'", "D'", "F'", "B'",
                     "R2", "L2", "U2", "D2", "F2", "B2"]
    max_turns = 0
    seeking_alg = []

    for lay1 in range(18):
        for lay2 in range(18):
            cccube = copy_cube(ccube)
            alg = [turn_notation[lay1], turn_notation[lay2]]
            _, cycles = simulate(cccube, alg)
            print(cycles, alg)
            if cycles > max_turns:
                max_turns = cycles
                seeking_alg = alg

    return max_turns, seeking_alg


def find_algorithm3(ccube):
    turn_notation = ["R", "L", "U", "D", "F", "B",
                     "R'", "L'", "U'", "D'", "F'", "B'",
                     "R2", "L2", "U2", "D2", "F2", "B2"]
    max_turns = 0
    seeking_alg = []

    for lay1 in range(18):
        for lay2 in range(18):
            for lay3 in range(18):
                cccube = copy_cube(ccube)
                alg = [turn_notation[lay1], turn_notation[lay2], turn_notation[lay3]]
                _, cycles = simulate(cccube, alg)
                if cycles > max_turns:
                    max_turns = cycles
                    seeking_alg = alg

    return max_turns, seeking_alg


def find_algorithm4(ccube):
    turn_notation = ["R", "L", "U", "D", "F", "B",
                     "R'", "L'", "U'", "D'", "F'", "B'",
                     "R2", "L2", "U2", "D2", "F2", "B2"]
    max_turns = 0
    seeking_alg = []

    for lay1 in range(18):
        print(lay1)
        for lay2 in range(18):
            for lay3 in range(18):
                for lay4 in range(18):
                    cccube = copy_cube(ccube)
                    alg = [turn_notation[lay1], turn_notation[lay2], turn_notation[lay3], turn_notation[lay4]]
                    _, cycles = simulate(cccube, alg)
                    if cycles > max_turns:
                        max_turns = cycles
                        seeking_alg = alg

    return max_turns, seeking_alg


def find_algorithm5(ccube):
    turn_notation = ["R", "L", "U", "D", "F", "B",
                     "R'", "L'", "U'", "D'", "F'", "B'",
                     "R2", "L2", "U2", "D2", "F2", "B2"]
    max_turns = 0
    seeking_alg = []

    for lay1 in range(4, 18):
        print(lay1)
        # 4
        for lay2 in range(18):
            for lay3 in range(18):
                for lay4 in range(18):
                    for lay5 in range(18):
                        cccube = copy_cube(ccube)
                        alg = [turn_notation[lay1], turn_notation[lay2], turn_notation[lay3],
                               turn_notation[lay4], turn_notation[lay5]]
                        _, cycles = simulate(cccube, alg)
                        if cycles > max_turns:
                            max_turns = cycles
                            seeking_alg = alg
                            print(max_turns, seeking_alg)

    return max_turns, seeking_alg


def find_algorithm6(ccube):
    turn_notation = ["R", "L", "U", "D", "F", "B",
                     "R'", "L'", "U'", "D'", "F'", "B'",
                     "R2", "L2", "U2", "D2", "F2", "B2"]
    max_turns = 0
    seeking_alg = []

    for lay2 in range(1, 18):
        print(lay2)
        for lay3 in range(18):
            for lay4 in range(18):
                for lay5 in range(18):
                    for lay6 in range(18):
                        cccube = copy_cube(ccube)
                        alg = ["R", turn_notation[lay2], turn_notation[lay3],
                               turn_notation[lay4], turn_notation[lay5], turn_notation[lay6]]
                        _, cycles = simulate(cccube, alg)
                        if cycles > max_turns:
                            max_turns = cycles
                            seeking_alg = alg
                            print(max_turns, seeking_alg)

    return max_turns, seeking_alg


def find_algorithm7(ccube):
    turn_notation = ["R", "L", "U", "D", "F", "B",
                     "R'", "L'", "U'", "D'", "F'", "B'",
                     "R2", "L2", "U2", "D2", "F2", "B2"]
    max_turns = 0
    seeking_alg = []

    for lay2 in range(8, 18):
        for lay3 in range(18):
            for lay4 in range(18):
                print(lay2, lay3, lay4)
                for lay5 in range(18):
                    for lay6 in range(18):
                        for lay7 in range(18):
                            cccube = copy_cube(ccube)
                            alg = ["R", turn_notation[lay2], turn_notation[lay3],
                                   turn_notation[lay4], turn_notation[lay5],
                                   turn_notation[lay6], turn_notation[lay7]]
                            _, cycles = simulate(cccube, alg)
                            if cycles > max_turns:
                                max_turns = cycles
                                seeking_alg = alg
                                print(max_turns, seeking_alg)

    return max_turns, seeking_alg
