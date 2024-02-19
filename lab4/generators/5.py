class MyNumbers:
    def __init__(self, n):
        self.n = n
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= self.n:
            answer = self.n
            self.n -= 1
            return answer
        else:
            raise StopIteration

n = int(input())


myclass = MyNumbers(n)

answer = []
for x in myclass:
    answer.append(str(x))
    
print(",".join(answer))