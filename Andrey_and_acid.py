def fun1(n, arr):
    count = 0
    for i in reversed(range(n - 1)):
        if arr[i] > arr[i + 1]:
            count = -1
            break
        elif arr[i] < arr[i + 1]:
            count += (arr[i + 1] - arr[i])

    return count


def test(f):
    assert f(2, [1, 2]) == 1
    assert f(5, [1, 1, 5, 5, 5]) == 4
    assert f(3, [3, 2, 1]) == -1


def main():
    n = int(input())
    arr = [int(i) for i in input().split()]

    print(fun1(n, arr))


if __name__ == '__main__':
    main()
    # test()
