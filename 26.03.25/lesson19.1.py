with open("24_1874.txt") as file:
    data = file.readline()
data = data.replace("QW", "Q W")
data = data.split()
ans = 0
for i in data:
    if ans < len(i):
        ans = len(i)
print(ans)
