def get_even_num(l):
    for item in l:
        if item % 2 == 0:
            yield item

def main():
    l = range(5)
    for item in get_even_num(l):
        print(item)

if __name__ == '__main__':
    main()
