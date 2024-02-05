def histogram(values):
    for i in values:
        print("*" * i)

values = list(map(int, input().split()))
histogram(values)