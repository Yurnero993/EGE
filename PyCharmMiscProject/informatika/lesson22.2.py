#взаимодействие с файлов с автоматическим закрытием потока
with open("test.txt") as file:
    data = file.readline()

print(data)
