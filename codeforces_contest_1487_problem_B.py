for _ in range(int(input())):
    n, k = map(int, input().split())
    if k == 1:
        print(1)
    elif n%2 == 0:        
        if k%n == 0:
            print(n)
        else:
            print(k%n)
    else:
        x = n//2
        if k%x == 0:
            x = k//x -1
        else:
            t = k%x
            t = k-t
            x = k//x 
        r = (x+k)%n
        if r == 0:
            print(n)
        else:
            print(r)