# Разделение строки на подстроки при помощи разделителя (по умолчанию пробел)
#Возвращает список подстрок




data1 = "Ivanov Ivan Ivanovitsch"
data2 = r"Ivanov\u4236Ivan\u4236874368Ivanovitsch"
data3 = "Ivanov.Ivan.Ivanovitsch"
print(data1.split())
print(data2.split(r"\u4236"))
print(data3.split("."))