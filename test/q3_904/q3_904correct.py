l_h = []
l_w = []
l_people = []

with open("test/q3_904/q3_904_read.txt", "r", encoding="utf-8") as file:
    for line in file:
        l = line.split(' ') #「以空格為剪刀，把一行字串切成一塊一塊的清單 (List)」
        l_h.append(float(l[1]))
        l_w.append(float(l[2]))
        l_people.append({
            'name': l[0],
            'h': float(l[1]),
            'w': float(l[2])
        })
        
        print(f'{l[0]} {l[1]} {l[2]}')

print(f'Average height: {sum(l_h)/len(l_h):.2f}')
print(f'Average weight: {sum(l_w)/len(l_w):.2f}')

l_tall = sorted(l_people, key=lambda x:x['h'], reverse=True)
l_heavy = sorted(l_people, key=lambda x:x['w'], reverse=True)


print(f'The tallest is {l_tall[0]["name"]} with {l_tall[0]["h"]:.2f}cm')
print(f'The heaviest is {l_heavy[0]["name"]} with {l_heavy[0]["w"]:.2f}kg')
