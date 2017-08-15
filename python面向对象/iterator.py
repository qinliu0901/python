#构造迭代器
class Iter:

    def __init__(self,start,end):
        self.count = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.end:
            r = self.count
            self.count += 1
            return r
        else:
            raise StopIteration

if __name__ == '__main__':
    for i in Iter(1,10):
        print(i)