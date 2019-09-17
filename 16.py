n = 2
sum = 0
for i in range(1, 1000):
    n = n * 2
while n > 0:
    sum = sum + n % 10
    n = n // 10
print(sum)