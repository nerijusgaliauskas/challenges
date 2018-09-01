#110103

M = 1000
PRICE = 10000.00

f = open('input.txt', 'r')
data_in = [int(float(l.split()[0]) * 100) for l in f]
f.close()

data_out = ''

m = data_in.pop(0) // 100
while m > 0:
    if m < M + 1:
        average = 0
        for i in range(m):
            if data_in[i] < int(PRICE * 100) + 1:
                average += data_in[i]
            else:
                raise Exception('no student spent more than ${:,.2f} ' \
                                '(entered ${:,.2f})' \
                                .format(PRICE, data_in[i] / 100))
        average //= m
        exchange = 0
        for i in range(m):
            diff = data_in[0] - average
            if diff < 0:
                exchange += diff
            data_in.pop(0)
        data_out += '${:.2f}\n'.format(-exchange / 100)
        m = data_in.pop(0) // 100
    else:
        raise Exception('the number of students cannot be greater than {} ' \
                        '(entered {})'.format(M, m))

f = open('output.txt', 'w')
f.write(data_out.strip('\n'))
f.close()

print(data_out.strip('\n'))
