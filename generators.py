def fibonacci_generator(limit: int):
    n1, n2, count = 0, 1, 0
    while True:
        if count == 0:
            count += 1
            yield n1
        elif count == 1:
            count += 1
            yield n2
        else:
            aux = n1 + n2
            if not limit or aux <= limit:
                n1, n2 = n2, aux
                count += 1
                yield aux
            else:
                break

def writterIterator(iterator):
    for value in iterator:
        print(value)

def run():
    max = input('Enter the number at which the sequence stops: ')
    if not max.isnumeric():
        max = 0
    writterIterator(fibonacci_generator(int(max)))

if __name__ == '__main__':
    run()