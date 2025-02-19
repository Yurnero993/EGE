data = ['hello', 'my', 'friend']

for i in range(len(data)):
    print(data[i])
    data = 'hello'

    print(data[0], data[4])
    print(data[len(data) - 1])
    print(data[-1], data[-5])
