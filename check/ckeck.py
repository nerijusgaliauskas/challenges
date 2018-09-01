#110107

def king_position(king, board):
    for i, row in enumerate(board):
        j = row.find(king)
        if j > -1:
            return (i, j)
    return (-1, -1)

def move(position, direction, *commands):
    for c in commands:
        if c == 'go':
            x, y = 0, 0
            if direction == 'north':
                x = -1
            elif direction == 'east':
                y = 1
            elif direction == 'south':
                x = 1
            elif direction == 'west':
                y = -1
            position = (position[0] + x, position[1] + y)

        elif c == 'right':
            if direction == 'north':
                direction = 'east'
            elif direction == 'east':
                direction = 'south'
            elif direction == 'south':
                direction = 'west'
            elif direction == 'west':
                direction = 'north'

        elif c == 'left':
            if direction == 'north':
                direction = 'west'
            elif direction == 'west':
                direction = 'south'
            elif direction == 'south':
                direction = 'east'
            elif direction == 'east':
                direction = 'north'
    return position

def feasible(position):
    la = (0, 0)
    rb = (7, 7)
    feasible_row = la[0] <= position[0] and position[0] <= rb[0]
    feasible_col = la[1] <= position[1] and position[1] <= rb[1]
    return feasible_row and feasible_col

def capture(piece, position, board):
    output = []
    i, j = position
    if piece.lower() == 'p':
        if piece == 'p':
            for c in ['right', 'left']:
                pos = move(position, 'south', 'go', c, 'go')
                if feasible(pos):
                    output.append(pos)
        else:
            for c in ['right', 'left']:
                pos = move(position, 'north', 'go', c, 'go')
                if feasible(pos):
                    output.append(pos)

    elif piece.lower() == 'n':
        for direction in ['north', 'east', 'south', 'west']:
            for c in ['right', 'left']:
                pos = move(position, direction, 'go', 'go', c, 'go')
                if feasible(pos):
                    output.append(pos)

    elif piece.lower() == 'b':
        for direction in ['north', 'south']:
            for c in ['right', 'left']:
                pos = move(position, direction, 'go', c, 'go')
                while feasible(pos):
                    output.append(pos)
                    pos = move(pos, direction, 'go', c, 'go')

    elif piece.lower() == 'r':
        for direction in ['north', 'east', 'south', 'west']:
            pos = move(position, direction, 'go')
            while feasible(pos):
                output.append(pos)
                pos = move(pos, direction, 'go')

    elif piece.lower() == 'q':
        output = capture('b', position, board) + capture('r', position, board)

    return output

def king_check(king, board):
    pos = king_position(king, board)
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if king == 'k':
                white = piece != piece.lower()
                if white and pos in capture(piece, (i, j), board):
                    return True
            elif king == 'K':
                black = piece == piece.lower()
                if black and pos in capture(piece, (i, j), board):
                    return True
    return False

def read_data(input):
    output = [[]]
    board = 0
    with open(input, 'r') as file:
        for line in file:
            line_content = line.split()
            if len(line_content) > 0:
                output[board].append(line_content[0])
            else:
                output.append([])
                board += 1
    output.pop()
    return output

def write_data(data, output):
    with open(output, 'w') as file:
        file.write(data.strip())

data_in = read_data('input.txt')

data_out = ''
for i, board in enumerate(data_in):
    data_out += 'Game #{}: '.format(i + 1)
    black_in_check = king_check('k', board)
    white_in_check = king_check('K', board)
    if black_in_check:
        data_out += 'black king is in check.\n'
    elif white_in_check:
        data_out += 'white king is in check.\n'
    else:
        data_out += 'no king is in check.\n'

write_data(data_out, 'output.txt')
