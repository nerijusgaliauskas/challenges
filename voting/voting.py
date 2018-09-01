#110108

import math
import sys

# max number of candidates
N = 20
# max number of ballots
M = 1000

def read_data(input):
    output = []
    cases, case = -1, -1
    with open(input, 'r') as file:
        for line in file:
            line_content = line.split()
            if len(line_content) > 0:
                if cases == -1:
                    cases = int(line_content[0])
                    output = [[] for i in range(cases)]
                else:
                    output[case].append(line_content)
                    if len(output[case]) > M:
                        raise Exception('invalid number of ballots '
                            '(expected less than {})'
                            .format(M + 1))
            else:
                case += 1
    return output

def find_winners(data):
    names_len = int(data[0][0])
    if names_len > N:
        raise Exception('invalid number of candidates '
            '(entered: {}, expected less than {})'
            .format(names_len, N + 1))
    names = [' '.join(data[i]) for i in range(1, names_len + 1)]

    votes_total = len(data) - names_len - 1
    votes_need = math.ceil(votes_total * .5)

    votes = [[] for i in range(names_len)]
    for i in range(names_len + 1, len(data)):
        vote = [int(data[i][j]) for j in range(names_len)]
        votes[vote[0] - 1].append(vote)

    count, next = 0, True
    while next:
        votes_lens = [len(votes[i]) for i in range(len(votes))]
        votes_max = max(votes_lens)
        if votes_max >= votes_need:
            next = False
            for i, j in enumerate(votes_lens):
                if votes_max != j:
                    names[i] = ''
        else:
            count += 1
            votes_min, votes_min_pos = min(votes_lens), []
            for i, j in enumerate(votes_lens):
                if votes_min == j:
                    votes_min_pos.append(i)
            # we exclude the first candidate with the lowest number of votes
            exclude = votes_min_pos[0]
            exclude_len = len(votes[exclude])
            for i in range(exclude_len):
                vote = votes[exclude].pop()
                votes[vote[count] - 1].append(vote)
    return names

def write_data(data, output):
    data_out = ''
    for i in data:
        if len(i) > 0:
            data_out += '{}\n'.format(i)
    data_out += '\n'
    with open(output, 'a') as file:
        file.write(data_out)

try:
    data_in = read_data('input.txt')
    for i in data_in:
        winners = find_winners(i)
        write_data(winners, 'output.txt')
except Exception as e:
    print('Error: {}'.format(e))
    sys.exit()
