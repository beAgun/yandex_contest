def equal(sets, i, j):
    if i != j:
        sets.setdefault(i, set())
        sets.setdefault(j, set())
        sets[j] |= {i}
        sets[i] |= {j}
    return sets


def includes(sets, i, j):
    sets[i] |= {j}
    return sets


def not_included(sets, i, j):
    if i in sets[j]:
        return 0
    return sets


def fun(n, facts):
    sets = {i: {i} for i in range(1, n + 1)}

    relations = {'=': equal, '>': includes, '!': not_included}

    sets2 = {}
    if '=' in facts:
        for i, j in facts['=']:
            sets2 = relations['='](sets2, i, j)
        del facts['=']

    for set_ in sorted(sets2):
        equal_sets = sorted(sets2[set_])
        for equal_set in equal_sets:
            sets[set_] |= sets[equal_set]
            sets[equal_set] = sets[set_]
            sets2[equal_set] = set()
            set_ = equal_set
    sets2.clear()

    if '>' in facts:
        for i, j in facts['>']:
            sets = relations['>'](sets, i, j)
        del facts['>']

    if '<' in facts:
        for i, j in facts['<']:
            sets = relations['>'](sets, j, i)
        del facts['<']

    cache = set()

    def f(set_, elements):
        nonlocal cache
        elements_copy = elements.copy()
        for el in elements_copy:
            if el == set_ or sets[el] == elements:
                continue
            elements |= sets[el]
            if el not in cache:
                cache |= {el}
                elements |= f(el, sets[el])
        return elements

    for set_ in sets:
        cache |= {set_}
        sets[set_] |= f(set_, sets[set_])

    if '!' in facts:
        for i, j in facts['!']:
            sets = relations['!'](sets, i, j)
            if sets == 0:
                return 0
        del facts['!']

    if '^' in facts:
        for i, j in facts['^']:
            sets = relations['!'](sets, j, i)
            if sets == 0:
                return 0
        del facts['^']

    return sets


def test():

    with open('test.txt', 'r') as inf:
        for line in inf:
            testname = line.rstrip()
            n = int(inf.readline().rstrip())
            facts = {}
            for i in range(n):
                for j, ch in enumerate(inf.readline().rstrip()):
                    if ch != '?':
                        facts.setdefault(ch, ())
                        facts[ch] += ((i + 1, j + 1),)

            m = int(inf.readline().rstrip())
            sets = {}
            for i in range(m):
                line = inf.readline().rstrip()
                setnum, size, elements = line.split(maxsplit=2)
                sets[int(setnum)] = set(map(int, elements.split()))
            try:
                if '31' in testname:
                    pass
                res = fun(n, facts)
                if res == 0:
                    res = {}
                assert sets == res
                print(testname, ': OK')
            except AssertionError:
                print(testname, ': AssertionError')
                print(n, facts, sep='\n')
                print('sets:', sets)
                print('res:', fun(n, facts))
                for key in sets:
                    if sets[key] != res[key]:
                        print('mistake:')
                        print(key, sets[key], res[key], sep='\n')
                        print()


def main():
    n, facts = int(input()), {}
    for i in range(n):
        for j, ch in enumerate(input()):
            if ch != '?':
                facts.setdefault(ch, ())
                facts[ch] += ((i + 1, j + 1),)

    sets = fun(n, facts)
    if not sets:
        print('No')
    else:
        print('Yes')
        for set_ in sorted(sets):
            print(set_, len(sets[set_]), *sorted(sets[set_]))


if __name__ == '__main__':
    main()
    # test()
