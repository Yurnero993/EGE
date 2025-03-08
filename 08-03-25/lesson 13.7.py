#текстовый файл состоит из символов,обозначающих прописные буквы латинского алфавита.
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых гласные и согласные буквы чередуются.
with open("24_11813.txt") as file:
    data = file.readline()
for i in "EYUIO":
    data = data.replace(i, "A")
for i in "QWRTPSDFGHJKLZXCVBNM":
    data = data.replace(i, "B")
while "AA" in data or "BB" in data:
    data = data.replace("AA", "A A")
    data = data.replace("BB", "B B")
data =data.split()
print(data)
ans = 0
for i in data:
    if len(i) > ans:
        ans = len(i)
print(ans)
