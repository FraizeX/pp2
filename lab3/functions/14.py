from functions import *

list = [2, 3, 5, 5, 8, 9, 9, 7, 8, 11, 14, 17, 20, 23, 29]
ans = [i for i in list if filter_prime(i)]
uniq = unique(ans)
histo = histogram(uniq)
print(histo)