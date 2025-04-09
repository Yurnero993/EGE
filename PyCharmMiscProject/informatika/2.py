with open("26_7626.txt") as file:
    k = int(file.readline())
    N = int(file.readline())
    times = []
    for i in file:
        times.append(list(map(int, i.split())))
times = sorted(times)
cells = [0] * k
cnt = 0
last = 0
for client in times:
    for i in range(k):
       if client[0] >= cells[i]:
           cells[i] = client[1] + 1
           cnt += 1
           last = i + 1
           break
print(cnt, last)

