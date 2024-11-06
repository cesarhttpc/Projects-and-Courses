# %%

while True:
    
    n = int(input())
    if n == 0:
        break

    split = input().split()

    print(int(split[0]))

    for i in range(1, n):
        out = int(split[i])^int(split[i-1])
        print(out, end=' ')

    

