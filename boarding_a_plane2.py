import regex as re


def fun(map, pattern, repl):
    fl = 0
    letters = 'ABC_DEF'
    for i, row in enumerate(map):
        if re.search(pattern, row):
            fl = 1
            map[i] = re.sub(pattern, repl, row)

            print('Passengers can take seats:', end=' ')
            for j in re.finditer('X', map[i]):
                print('{}{}'.format(i + 1, letters[j.start()]), end=' ')
            print()
            for s in map:
                print(s)

            map[i] = re.sub('X', '#', map[i])
            break

    if not fl:
        print('Cannot fulfill passengers requirements')

    return map


def main():

    n = int(input())
    map = [input() for _ in range(n)]
    m = int(input())
    for i in range(m):
        num, side, position = input().split()
        num = int(num)

        if side == 'left':
            if position == 'window':
                pattern = r'(\.{%s})(.{%s}_.{3})' % (num, (3 - num))
                repl = 'X'*num + r'\2'

            elif position == 'aisle':
                pattern = r'(.{%s})(\.{%s})(_.{3})' % ((3 - num), num)
                repl = r'\1' + 'X' * num + r'\3'

        elif side == 'right':
            if position == 'window':
                pattern = r'(.{3}_.{%s})(\.{%s})' % ((3 - num), num)
                repl = r'\1' + 'X'*num

            elif position == 'aisle':
                pattern = r'(.{3}_)(\.{%s})(.{%s})' % (num, (3 - num))
                repl = r'\1' + 'X' * num + r'\3'

        map = fun(map, pattern, repl)


if __name__ == '__main__':
    main()
    # test()
