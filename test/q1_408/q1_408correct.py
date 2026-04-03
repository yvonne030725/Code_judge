# 408
even = odd = 0
for i in range(10):
    n = eval(input())

    if n % 2 == 0 :
        even += 1
    else:
        odd += 1

print(f"Even: {even}")
print(f"Odd: {odd}")