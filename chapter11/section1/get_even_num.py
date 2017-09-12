def get_even_num(l):
    res = []
    for item in l:
        if item % 2 == 0:
            res.append(item)
    return res

def main():
    l = range(5)
    for item in get_even_num(l):
        print(item)

if __name__ == '__main__':
    main()
