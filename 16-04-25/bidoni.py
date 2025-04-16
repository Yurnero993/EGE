with open("26.2_19727.txt") as file:
    M, N = map(int, file.readline().split())
    litrs = []
    for i in file:
        litrs.append(int(i))

litrs.sort()
min_litr = 0
cnt = 0
for i in litrs:
    if M >= min_litr + i:
        min_litr += i
        cnt +=1
cnt2 = 0
for i in litrs:
   if sum(litrs[:cnt-1]) + i > M:
       cnt2 += 1
print(cnt, cnt2)