def filter_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = [i for i in list if filter_prime(i)]
print(ans)