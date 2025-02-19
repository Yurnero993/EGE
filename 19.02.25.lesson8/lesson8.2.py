#Считать с клавиатуры число.
#Вывести на экран его разряды.
num = int(input())
summ = 0
for i in str(num):
    summ += int(i)
print(summ)
