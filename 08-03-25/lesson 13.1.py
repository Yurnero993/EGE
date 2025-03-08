# проверка что все символы строки являются числами
data = "123"
print(data.isdigit())



# проверка что все символы строки являются буквами
data = "Hello"
print(data.isalpha())



# проверка что все символы строки являются цифрами либо буквами
data = "Hello"
print(data.isalnum())



# проверка что все символы строки являются пробелами
data = "                  "
print(data.isspace())


# проверка регистра строки
data = "Hello"
print(data.islower())
print(data.isupper())