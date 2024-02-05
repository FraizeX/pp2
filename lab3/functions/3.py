def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits

heads = 35
legs = 94
chickens, rabbits = solve(heads, legs)
print(chickens, rabbits)
