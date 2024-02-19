class MyNumbers:
    def __init__(self, n):
        self.n = n
        self.a = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= self.n:
            if self.a % 2 == 0:
                result = self.a
                self.a += 2
                return result
            else:
                self.a += 1
        else:
            raise StopIteration

n = int(input())
myclass = MyNumbers(n)
myiter = iter(myclass)

answer = []
for x in myiter:
    answer.append(str(x))
  
print(",".join(answer))