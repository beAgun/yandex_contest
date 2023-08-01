def find_seats(map, num, side, position):
    letters = {'left': 'ABC', 'right': 'DEF'}
    fl = 0
    s = 1 if side == 'left' else 0
    pos = 1 if position == 'window' else 0

    for row in range(len(map)):

        seats = map[row][side] if (s and pos) or (not s and not pos) else map[row][side][::-1]

        if seats[:num] == '.' * num:
            seats = 'X' * num + seats[num:]
            map[row][side] = seats if (s and pos) or (not s and not pos) else seats[::-1]

            print('Passengers can take seats:', end='')
            range_ = range(num) if (s and pos) or (not s and not pos) else range(3)[3 - num:]
            #print(range_)
            for i in range_:
                print(' ' + '{}{}'.format(row + 1, letters[side][i]), end='')
            print()
            for j in map:
                print(map[j]['left'] + '_' + map[j]['right'])
            seats = '#' * num + seats[num:]
            map[row][side] = seats if (s and pos) or (not s and not pos) else seats[::-1]
            fl = 1
            break

    if not fl:
        print('Cannot fulfill passengers requirements')

    return map


def main():
    n = int(input())
    map = {}
    for i in range(n):
        left, right = input().split('_')
        #a, b, c = left
        #d, e, f = right
        #map[i + 1] = {'left': {'A': a, 'B': b, 'C': c},
        #                       'right':{'D': d, 'E': e, 'F': f}}
        map[i] = {'left': left, 'right': right}

    m = int(input())
    for i in range(m):
        num, side, position = input().split()
        map = find_seats(map, int(num), side, position)


if __name__ == '__main__':
    main()
    # test()
