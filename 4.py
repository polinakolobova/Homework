p = [0]*6
max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        n = i*j
        temp = n
        if len(str(n)) == 5:
            p[5] = n % 10
            n = n // 10
            p[4] = n % 10
            n = n // 10
            p[3] = n % 10
            n = n // 10
            p[2] = n % 10
            n = n // 10
            p[1] = n % 10
            if (p[1] == p[5]) and (p[2]== p[4]):
                if temp > max:
                    max = temp
        if len(str(n)) == 6:
            p[5] = n % 10
            n = n // 10
            p[4] = n % 10
            n = n // 10
            p[3] = n % 10
            n = n // 10
            p[2] = n % 10
            n = n // 10
            p[1] = n % 10
            n = n // 10
            p[0] = n % 10
            if (p[0] == p[5]) and (p[1] == p[4]) and (p[2] == p[3]):
                if temp > max:
                    max = temp
print(max)

