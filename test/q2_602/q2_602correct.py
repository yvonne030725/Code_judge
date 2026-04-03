sum = 0 
n = input()

for i in range(5):
    if i == "A":
        sum += 1
    
    elif i == "J":
        sum += 11

    elif i == "Q":
        sum += 12

    elif i == "K":
        sum += 13

    else:
        sum += int(n)

print(sum)