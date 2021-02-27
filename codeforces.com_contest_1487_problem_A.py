for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c = a.count(a[0])
    print(n-c)
