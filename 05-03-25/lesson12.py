# Возвращает True если строка string оканчивается на suffix
#
# Если указаны параметры start/end, то suffix ищется в срезе от start до end

data = 'Hello'
print(data.endswith('Hello'))


data=(input("введите строку:"))
end_line = (input("введите на что должна оканчиваться строка:"))
start_pos = int(input("введите левую границу поиска:"))
end_pos = int(input("введите правую позицию поиска:"))
if start_pos > end_pos:
    print("Левая граница не может превышать правую границу")
elif start_pos < 0 or end_pos < 0:
    print("Левая граница и правая граница могут принимать только положительные число")
elif start_pos > len(data):
    print("Левая граница не должна превышать ко-во символов строки")
else:
    if data [start_pos:end_pos] [-len(end_line):] == end_line:
        print(True)
    else:
        print(False)
