text = input()
# служит для подсчета количества элементов последовательности
print(len(text))

cnt = 0
for i in text:
    cnt +=1
print(cnt)

cnt = 0
while text:
    cnt += 1
    text = text[:-1]
