with open("26_954.txt") as file:
    N, K, M =  map(int, file.readline().split())
    prices = []
    for i in file:
        prices.append(int(i))
prices.sort(reverse=True)
ans= sum(prices[0:K]) * 0.2
ans2 = sum(prices[K:K+M]) * 0.1
ans3 = prices[K+M]
print(ans3, ans+ans2)





