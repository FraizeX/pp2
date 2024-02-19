class MyNumbers:
    def __init__(self, n):
        self.n = n
        self.a = 1
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= self.n:
            x = self.a ** 2
            self.a += 1
            return x
        else:
            raise StopIteration

n = int(input())
myclass = MyNumbers(n)
myiter = iter(myclass)

for x in myiter:
  print(x)