from random import randint
data = []
for i in range(20):
    data.append(randint(1,100))
print(data)
pos_min_el = data.index(min(data))
pos_max_el = data.index(max(data))
if pos_max_el > pos_min_el:
    for i in range(pos_min_el + 1, pos_max_el):
        print(data[i], end=" ")
else:
    for i in range(pos_max_el + 1, pos_min_el):
        print(data[i], end=" ")


