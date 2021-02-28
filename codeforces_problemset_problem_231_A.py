c = 0
for _ in range(int(input())):
    a = list(map(int,input().split()))
    if a.count(1) >= 2 :
        c += 1
print(c)