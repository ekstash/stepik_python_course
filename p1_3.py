n, k = map(int, input().split())


def c(n, k):
    if n == k or k == 0:
        return 1
    else:
        return c(n - 1, k) + c(n - 1, k - 1)


if k > n:
    print(0)
else:
    print(c(n, k))
