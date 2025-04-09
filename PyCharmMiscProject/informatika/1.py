with open("26_21424.txt") as file:
    N = int(file.readline())
    lengths = []
    for i in file:
        lengths.append(int(i))
lengths.sort(reverse=True)
last = [lengths[0]]
for next in lengths[1:]:
    if last[-1] - next >= 9:
        last.append(next)
print(len(last) , last[-1])