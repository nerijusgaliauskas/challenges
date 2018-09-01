#110202

STRAIGHT_FLUSH = 8
FOUR_OF_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_KIND = 3
TWO_PAIRS = 2
PAIR = 1
HIGH_CARD = 0

def read(file):
    output = []
    with open(file, 'r') as f:
        for line in f:
            content = line.split()
            if len(content) == 2 * 5:
                output.append(content)
            elif len(content) > 0:
                raise Exception('the number of cards has to be equal to {}'
                    .format(2 * 5))
    return output

def get_value(char):
    values = '0123456789TJQKA'
    if char in values:
        return values.index(char)
    else:
        raise Exception('the symbol {} does not belong to the set "{}"'
            .format(char, values))

def get_values_suites(cards):
    values, suites = [], []
    for card in cards:
        if len(card) == 2:
            values.append(get_value(card[0]))
            suites.append(card[1])
        else:
            raise Exception('invalid card {}'.format(card))
    return (sorted(values), sorted(suites))

def get_high_card(values, suites):
    return (HIGH_CARD, values)

def get_pair(values, suites):
    list = sorted([i for i in set(values)])
    condition = len(list) == 4
    if condition:
        pair = [values[i] for i in range(5) if values.count(values[i]) == 2]
        list.append(pair[0] + 14)
        return (PAIR, list)
    return (-1, -1)

def get_two_pairs(values, suites):
    list = [values[i] for i in [0, 1, 1, 3, 3]]
    condition = values == list and len(set(list)) == 3
    if condition:
        return (TWO_PAIRS, [values[i] for i in [0, 1, 3]])
    else:
        list = [values[i] for i in [0, 0, 2, 3, 3]]
        condition = values == list and len(set(list)) == 3
        if condition:
            return (TWO_PAIRS, [values[i] for i in [0, 2, 3]])
        else:
            list = [values[i] for i in [0, 0, 2, 2, 4]]
            condition = values == list and len(set(list)) == 3
            if condition:
                return (TWO_PAIRS, [values[i] for i in [0, 2, 4]])
    return (-1, -1)

def get_three_of_kind(values, suites):
    list = [values[i] for i in [0, 0, 0, 3, 4]]
    condition = values == list and len(set(list)) == 3
    if condition:
        return (THREE_OF_KIND, values[0])
    else:
        list = [values[i] for i in [0, 1, 1, 1, 4]]
        condition = values == list and len(set(list)) == 3
        if condition:
            return (THREE_OF_KIND, values[1])
        else:
            list = [values[i] for i in [0, 1, 2, 2, 2]]
            condition = values == list and len(set(list)) == 3
            if condition:
                return (THREE_OF_KIND, values[2])
    return (-1, -1)

def get_straight(values, suites):
    condition = values == list(range(values[0], values[0] + 5))
    if condition:
        return (STRAIGHT, max(values))
    return (-1, -1)

def get_flush(values, suites):
    condition = suites.count(suites[0]) == 5
    if condition:
        return (FLUSH, values)
    return (-1, -1)

def get_full_house(values, suites):
    list = [values[i] for i in [0, 0, 0, 3, 3]]
    condition = values == list
    if condition:
        return (FULL_HOUSE, values[0])
    else:
        list = [values[i] for i in [0, 0, 2, 2, 2]]
        condition = values == list
        if condition:
            return (FULL_HOUSE, values[2])
    return (-1, -1)

def get_four_of_kind(values, suites):
    condition = values.count(values[0]) == 4
    if condition:
        return (FOUR_OF_KIND, values[0])
    else:
        condition = values.count(values[1]) == 4
        if condition:
            return (FOUR_OF_KIND, values[1])
    return (-1, -1)

def get_straight_flush(values, suites):
    condition1 = suites.count(suites[0]) == 5
    condition2 = values == list(range(values[0], values[0] + 5))
    if condition1 and condition2:
        return (STRAIGHT_FLUSH, max(values))
    return (-1, -1)

def evaluate(cards):
    values, suites = get_values_suites(cards)
    rank, value = get_straight_flush(values, suites)
    if rank == -1:
        rank, value = get_four_of_kind(values, suites)
        if rank == -1:
            rank, value = get_full_house(values, suites)
            if rank == -1:
                rank, value = get_flush(values, suites)
                if rank == -1:
                    rank, value = get_straight(values, suites)
                    if rank == -1:
                        rank, value = get_three_of_kind(values, suites)
                        if rank == -1:
                            rank, value = get_two_pairs(values, suites)
                            if rank == -1:
                                rank, value = get_pair(values, suites)
                                if rank == -1:
                                    rank, value = get_high_card(values, suites)
    return {'rank': rank, 'value': value}

def get_rank_name(rank):
    if rank == 0:
        output = 'HIGH_CARD'
    elif rank == 1:
        output = 'PAIR'
    elif rank == 2:
        output = 'TWO_PAIRS'
    elif rank == 3:
        output = 'THREE_OF_KIND'
    elif rank == 4:
        output = 'STRAIGHT'
    elif rank == 5:
        output = 'FLUSH'
    elif rank == 6:
        output = 'FULL_HOUSE'
    elif rank == 7:
        output = 'FOUR_OF_KIND'
    else:
        output = 'STRAIGHT_FLUSH'
    return output

def process(data):
    output = ''
    for cards in data:
        black = evaluate(cards[:5])
        white = evaluate(cards[5:])
        output += get_rank_name(black['rank']) + ' '
        output += get_rank_name(white['rank']) + ' '
        if black['rank'] > white['rank']:
            output += 'Black wins.\n'
        elif black['rank'] == white['rank']:
            if type(black['value']) is list:
                next = True
                while next:
                    next = False
                    black_value = max(black['value'])
                    black['value'] = [i for i in black['value'] 
                        if i != black_value]
                    white_value = max(white['value'])
                    white['value'] = [i for i in white['value']
                        if i != white_value]
                    if black_value > white_value:
                        output += 'Black wins.\n'
                    elif black_value == white_value:
                        if len(black['value']) > 0 and len(white['value']) > 0:
                            next = True
                        else:
                            output += 'Tie.\n'
                    else:
                        output += 'White wins.\n'
            else:
                if black['value'] > white['value']:
                    output += 'Black wins.\n'
                elif black['value'] == white['value']:
                    output += 'Tie.\n'
                else:
                    output += 'White wins.\n'
        else:
            output += 'White wins.\n'
    return output

def write(file, data):
    with open(file, 'w') as f:
        f.write(data.strip())

if __name__ == '__main__':
    write('output.txt', process(read('input.txt')))
