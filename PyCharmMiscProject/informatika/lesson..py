#перенаправление потока в файл
file= open("test.txt")
#считывание еще не считанной строки
print(file.readline())
print(file.readline())
print(file.readline())
#считывание еще не считанных сток
print(file.readlines())
#закрытие потока
file.close()