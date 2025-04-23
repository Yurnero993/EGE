with open("26_20815.txt") as file:
    N, K = map(int, file.readline().split())
    astronauts = []
    for i in file:
        a1, a2, a3, a4, a5 = map(int, i.split())
        astronauts.append([a2 + a3 + a4 + a5,a5 , a1])
astronauts.sort(key=lambda x: (-x[0],-x[1], x[2] ))
if astronauts[K - 1][0] == astronauts[K][0]:
    cnt = 0
    half_point = astronauts[K][0]
    id = 0
    for i in astronauts:
        if i[0] == half_point:
            cnt += 1
        if i[0] > half_point:
            id = i[2]
    print(id, cnt)
else:
    print(astronauts[K - 1][2], 0 )



