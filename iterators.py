import time

class FibonacciIter():

    def __init__(self, max = None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.count = 0
        return self

    def __next__(self):
        if not self.max:
            if self.count == 0:
                self.count += 1
                return self.n1
            elif self.count == 1:
                self.count += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                self.count += 1
                return self.aux
        else:
            if self.count == 0 and self.n1 <= self.max:
                self.count += 1
                return self.n1
            elif self.count == 1 and self.n2 <= self.max:
                self.count += 1
                return self.n2
            elif self.count > 1:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                if self.aux >= self.max+1:
                    raise StopIteration
                self.count += 1
                return self.aux

if __name__ == '__main__':
    fibonacci = FibonacciIter()
    for element in fibonacci:
        print(element)