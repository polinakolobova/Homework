arr = [0]*6
max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        n = i*j
        temp = n
        if len(str(n)) == 5:
            arr[5] = n % 10
            n = n // 10
            arr[4] = n % 10
            n = n // 10
            arr[3] = n % 10
            n = n // 10
            arr[2] = n % 10
            n = n // 10
            arr[1] = n % 10
            if (arr[1] == arr[5]) and (arr[2] == arr[4]):
                if temp > max:
                    max = temp
        if len(str(n)) == 6:
            arr[5] = n % 10
            n = n // 10
            arr[4] = n % 10
            n = n // 10
            arr[3] = n % 10
            n = n // 10
            arr[2] = n % 10
            n = n // 10
            arr[1] = n % 10
            n = n // 10
            arr[0] = n % 10
            if (arr[0] == arr[5]) and (arr[1] == arr[4]) and (arr[2] == arr[3]):
                if temp > max:
                    max = temp
print(max)

