def banan(piles, h):
    k = 1
    new_h = h + 1

    for x in piles:
        if (x < 1):
            return -1

    if(len(piles) > h or len(piles) < 1):
        return -1 

    while (new_h > h):
        new_h = 0
        for x in piles:  
            if (k >= x):
                new_h += 1
            elif (k == 1 or x % k == 0):
                new_h += x // k
            else:
                new_h += 1 + x // k

        if (new_h > h):
                k += 1 
    return k


if __name__ == "__main__":
    print(banan([3, 6, 7, 11], 8))
    print(banan([30, 11, 23, 4, 20], 5))
    print(banan([30, 11, 23, 4, 20], 6))
    print(banan([0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10))
    print(banan([-2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 20))
    print(banan([40, 19], 1))
