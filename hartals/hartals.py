#110203

def read(file_name):
    output = []
    with open(file_name, 'r') as f:
        for line in f:
            content = line.split()
            if len(content) > 0:
                output.append(int(content[0]))
    return output

def prepare(data):
    DAYS_MIN, DAYS_MAX = 7, 3650
    PARTIES_MIN, PARTIES_MAX = 1, 100
    output = []
    if len(data) > 0:
        tests = data.pop(0)
        for i in range(tests):
            if len(data) > 1:
                days = data.pop(0)
                if not (DAYS_MIN <= days and days <= DAYS_MAX):
                    raise Exception(
                        'invalid number of days: ' \
                        'expected between {} and {}, ' \
                        'received {}'
                        .format(DAYS_MIN, DAYS_MAX, days)
                    )
                parties = data.pop(0)
                if not (PARTIES_MIN <= parties and parties <= PARTIES_MAX):
                    raise Exception(
                        'invalid number of parties: ' \
                        'expected between {} and {}, ' \
                        'received {}'
                        .format(PARTIES_MIN, PARTIES_MAX, parties)
                    )
                if len(data) >= parties:
                    hartals = []
                    for j in range(parties):
                        h = data.pop(0)
                        if h < 0 or h % 7 == 0:
                            raise Exception(
                                'invalid `hartal parameter` {}: ' \
                                'it must be positive and ' \
                                'never be a multiple of 7'
                                .format(h)
                            )
                        hartals.append(h)
            output.append({
                'days': days,
                'hartals': hartals,
            })
    return output

def process(data):
    output = []
    week_days = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    for i in data:
        days = i['days']
        hartals = i['hartals']
        hartals_days = 0
        for day in range(days):
            # no hartals on either Fridays or Saturdays
            week_day = week_days[day % 7]
            if week_day != 'Fr' and week_day != 'Sa':
                index = 0
                hartal = False
                while not hartal and index < len(hartals):
                    hartal = (day + 1) % hartals[index] == 0
                    if hartal:
                        hartals_days += 1
                    index += 1
        output.append(hartals_days)
    return output

def write(data, file_name):
    output = ''
    for i in data:
        output += '{}\n'.format(i)
    with open(file_name, 'w') as f:
        f.write(output.strip('\n'))

if __name__ == '__main__':
    try:
        write(process(prepare(read('input.txt'))), 'output')
    except Exception as e:
        print('Error: {}'.format(e))
