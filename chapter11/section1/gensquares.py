def gensquares(N):
    res = []
    for i in range(N):
        res.append(i*i)
    return res

for item in gensquares(5):
    print(item)
