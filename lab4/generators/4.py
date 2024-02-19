class MyNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= self.b:
            square = self.a ** 2
            self.a += 1
            return square
        else:
            raise StopIteration

a = int(input())
b = int(input())

myclass = MyNumbers(a, b)

answer = []
for x in myclass:
    answer.append(str(x))
    
print(",".join(answer))