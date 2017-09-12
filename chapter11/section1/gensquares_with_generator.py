def gensquares(N):
    for i in range(N):
        yield i ** 2

for item in gensquares(5):
    print(item)
