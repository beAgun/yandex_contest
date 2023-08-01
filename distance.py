def fun(n: int, k: int, arr: list) -> dict:
    arr = sorted(arr)

    s = 0
    for i in range(1, k + 1):
        s += (arr[i] - arr[0])
    dist = {arr[0]: s}

    l, r = 0, k
    for i in range(1, n):
        if arr[i] not in dist:
            if i > r:
                # s = k * arr[i] + (s - k * arr[r]) + (arr[i] - arr[r]) - (arr[i] - arr[l])
                s = k * arr[i] + (s - k * arr[r]) + (arr[l] - arr[r])
                l += 1;
                r += 1
            else:
                s += (arr[i] - arr[i - 1]) * ((i - l - 1) - (r - i))
            while l != i and r + 1 < n:
                delta = (arr[r + 1] - arr[i]) - (arr[i] - arr[l])
                if delta >= 0:
                    break
                s += delta
                l += 1;
                r += 1

            dist[arr[i]] = s

        elif i > r:
            l += 1;
            r += 1

    return dist


def test(f):
    import random as r
    import time

    assert f(2, 1, [1, 5]) == {1: 4, 5: 4}
    assert f(5, 2, [1, 1, 1, 1, 1]) == {1: 0}

    assert f(4, 2, [1, 2, 3, 4]) == {1: 3, 2: 2, 3: 2, 4: 3}
    assert f(5, 3, [3, 2, 5, 1, 2]) == {3: 4, 2: 2, 5: 8, 1: 4}
    assert f(6, 2, [3, 2, 1, 101, 102, 103]) == {3: 3, 2: 2, 1: 3, 101: 3, 102: 2, 103: 3}

    assert f(5, 2, [3, 2, 3, 7, 10]) == {2: 2, 3: 1, 7: 7, 10: 10}
    assert f(5, 1, [8, 4, 4, 4, 4]) == {4: 0, 8: 4}

    # worst case
    n = 3 * 10 ** 5
    k = n - 1
    arr = [r.randint(1, 10 ** 9) for i in range(n)]
    t0 = time.perf_counter()
    f(n, k, arr)
    t1 = time.perf_counter()
    # print('n: {}, k: {}'.format(n, k))
    # print('time:', t1 - t0)

    if t1 - t0 < 4:
        print('Everything is OK')


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    res = fun(n, k, arr)
    for i in arr:
        print(res[i], end=' ')


if __name__ == '__main__':
    main()
    # test(fun)
