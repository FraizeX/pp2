class MyNumbers:
    def __init__(self, n):
        self.n = n
        self.a = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        while self.a <= self.n:
            if self.a % 3 == 0 and self.a % 4 == 0:
                result = self.a
                self.a += 1
                return result
            else:
                self.a += 1
        raise StopIteration

n = int(input())
myclass = MyNumbers(n)

answer = []
for x in myclass:
    if x != 0:
        answer.append(str(x))

print(",".join(answer))