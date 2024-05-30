cube = [
    [
        'red', 'red', 'red',
        'red', 'red', 'red',
        'red', 'red', 'red'
    ],
    [
        'blue', 'blue', 'blue',
        'blue', 'blue', 'blue',
        'blue', 'blue', 'blue'
    ],
    [
        'white', 'white', 'white',
        'white', 'white', 'white',
        'white', 'white', 'white'
    ],
    [
        'orange', 'orange', 'orange',
        'orange', 'orange', 'orange',
        'orange', 'orange', 'orange'
    ],
    [
        'green3', 'green3', 'green3',
        'green3', 'green3', 'green3',
        'green3', 'green3', 'green3'
    ],
    [
        'yellow', 'yellow', 'yellow',
        'yellow', 'yellow', 'yellow',
        'yellow', 'yellow', 'yellow'
    ]
]


def turn(cube, name):
    match name:
        case 'R':
            cube[2][0], cube[2][2], cube[2][6], cube[2][8] = cube[2][2], cube[2][8], cube[2][0], cube[2][6]
            cube[2][1], cube[2][3], cube[2][5], cube[2][7] = cube[2][5], cube[2][1], cube[2][7], cube[2][3]

            cube[0][6], cube[1][6], cube[3][0], cube[4][6] = cube[1][6], cube[3][0], cube[4][6], cube[0][6]
            cube[0][7], cube[1][7], cube[3][3], cube[4][7] = cube[1][7], cube[3][3], cube[4][7], cube[0][7]
            cube[0][8], cube[1][8], cube[3][6], cube[4][8] = cube[1][8], cube[3][6], cube[4][8], cube[0][8]
        case "R'":
            turn(cube, 'R')
            turn(cube, 'R')
            turn(cube, 'R')
        case "R2":
            turn(cube, "R")
            turn(cube, "R")
        case 'L':
            new_cube = [cube[3], cube[5], cube[4], cube[0], cube[2], cube[1]]
            turn(new_cube, 'F')
        case "L'":
            turn(cube, 'L')
            turn(cube, 'L')
            turn(cube, 'L')
        case "L2":
            turn(cube, "L")
            turn(cube, "L")
        case "U":
            cube[0][6], cube[0][8], cube[0][2], cube[0][0] = cube[0][0], cube[0][6], cube[0][8], cube[0][2]
            cube[0][3], cube[0][7], cube[0][5], cube[0][1] = cube[0][1], cube[0][3], cube[0][7], cube[0][5]

            cube[1][0], cube[2][0], cube[4][8], cube[5][8] = cube[2][0], cube[4][8], cube[5][8], cube[1][0]
            cube[1][3], cube[2][3], cube[4][5], cube[5][5] = cube[2][3], cube[4][5], cube[5][5], cube[1][3]
            cube[1][6], cube[2][6], cube[4][2], cube[5][2] = cube[2][6], cube[4][2], cube[5][2], cube[1][6]
        case "U'":
            turn(cube, 'U')
            turn(cube, 'U')
            turn(cube, 'U')
        case "U2":
            turn(cube, "U")
            turn(cube, "U")
        case 'D':
            new_cube = [cube[3], cube[5], cube[4], cube[0], cube[2], cube[1]]
            turn(new_cube, 'U')
        case "D'":
            turn(cube, 'D')
            turn(cube, 'D')
            turn(cube, 'D')
        case "D2":
            turn(cube, "D")
            turn(cube, "D")
        case 'F':
            cube[1][0], cube[1][2], cube[1][6], cube[1][8] = cube[1][2], cube[1][8], cube[1][0], cube[1][6]
            cube[1][1], cube[1][3], cube[1][5], cube[1][7] = cube[1][5], cube[1][1], cube[1][7], cube[1][3]

            cube[0][2], cube[2][0], cube[3][0], cube[5][0] = cube[5][0], cube[0][2], cube[2][0], cube[3][0]
            cube[0][5], cube[2][1], cube[3][1], cube[5][1] = cube[5][1], cube[0][5], cube[2][1], cube[3][1]
            cube[0][8], cube[2][2], cube[3][2], cube[5][2] = cube[5][2], cube[0][8], cube[2][2], cube[3][2]
        case "F'":
            turn(cube, 'F')
            turn(cube, 'F')
            turn(cube, 'F')
        case "F2":
            turn(cube, "F")
            turn(cube, "F")
        case 'B':
            new_cube = [cube[3], cube[5], cube[4], cube[0], cube[2], cube[1]]
            turn(new_cube, 'R')
        case "B'":
            turn(cube, 'B')
            turn(cube, 'B')
            turn(cube, 'B')
        case "B2":
            turn(cube, "B")
            turn(cube, "B")
        case "M'":
            cube[0][3], cube[1][3], cube[3][1], cube[4][3] = cube[1][3], cube[3][1], cube[4][3], cube[0][3]
            cube[0][4], cube[1][4], cube[3][4], cube[4][4] = cube[1][4], cube[3][4], cube[4][4], cube[0][4]
            cube[0][5], cube[1][5], cube[3][7], cube[4][5] = cube[1][5], cube[3][7], cube[4][5], cube[0][5]
        case "M":
            turn(cube, "M'")
            turn(cube, "M'")
            turn(cube, "M'")
        case "M2":
            turn(cube, "M'")
            turn(cube, "M'")
        case "E":
            # cube[1][1], cube[2][1], cube[4][1], cube[5][1] = cube[5][7], cube[1][1], cube[2][7], cube[4][1]
            # cube[1][4], cube[2][4], cube[4][4], cube[5][4] = cube[5][4], cube[1][4], cube[2][4], cube[4][4]
            # cube[1][7], cube[2][7], cube[4][7], cube[5][7] = cube[5][1], cube[1][7], cube[2][1], cube[4][7]

            cube[1][1], cube[2][1], cube[4][1], cube[5][1], cube[1][4], cube[2][4], cube[4][4], cube[5][4], cube[1][7], cube[2][7], cube[4][7], cube[5][7] = cube[5][7], cube[1][1], cube[2][7], cube[4][1], cube[5][4], cube[1][4], cube[2][4], cube[4][4], cube[5][1], cube[1][7], cube[2][1], cube[4][7]
        case "E'":
            turn(cube, "E")
            turn(cube, "E")
            turn(cube, "E")
        case "E2":
            turn(cube, "E")
            turn(cube, "E")
        case "S":
            cube[0][1], cube[2][3], cube[3][3], cube[5][3] = cube[5][3], cube[0][1], cube[2][3], cube[3][3]
            cube[0][4], cube[2][4], cube[3][4], cube[5][4] = cube[5][4], cube[0][4], cube[2][4], cube[3][4]
            cube[0][7], cube[2][5], cube[3][5], cube[5][5] = cube[5][5], cube[0][7], cube[2][5], cube[3][5]
        case "S'":
            turn(cube, "S")
            turn(cube, "S")
            turn(cube, "S")
        case "S2":
            turn(cube, "S")
            turn(cube, "S")
