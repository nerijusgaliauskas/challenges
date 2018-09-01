#110102

def read_data(name):
    data = dict()
    field = 0
    f = open(name, 'r')
    for line in f:
        l = line.split()
        if len(l) == 2:
            n, m = int(l[0]), int(l[1])
            if (n > 0 and m > 0):
                field += 1
                data[field] = []
        else:
            row = []
            for i in l[0]:
                if i == '*':
                    row.append(-1)
                else:
                    row.append(0)
            data[field].append(row)
    f.close()
    return data

def process_data(data):
    for i in data.keys():
        matrix = data[i]
        n, m = len(matrix), len(matrix[0])
        for j in range(n):
            for k in range(m):
                if matrix[j][k] == -1:
                    rows = [r for r in range(j - 1, j + 2) if r > -1 and r < n]
                    cols = [c for c in range(k - 1, k + 2) if c > -1 and c < m]
                    for r, c in [(r, c) for r in rows for c in cols]:
                        if matrix[r][c] > -1:
                            matrix[r][c] += 1
    return data

def write_data(name, data):
    f = open(name, 'w')
    output = ''
    for i in data.keys():
        output += 'Field #{}:\n'.format(i)
        matrix = data[i]
        n, m = len(matrix), len(matrix[0])
        for j in range(n):
            for k in range(m):
                if matrix[j][k] == -1:
                    output += '*'
                else:
                    output += '{}'.format(matrix[j][k])
            output += '\n'
        output += '\n'
    output = output.strip('\n')
    f.write(output)
    f.close()

data_in = read_data('input.txt')
data_out = process_data(data_in)
write_data('output.txt', data_out)
