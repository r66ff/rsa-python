import sys, random, string

def random_gen():
    n = random.SystemRandom()
    n = n.getrandbits(1) # I thought getrandbits() would be a better solution than extracting the least significant bit
    print('Extracting a random bit out of a random.SystemRandom object...\nExtracted random bit is: %s\n' % n)
    return n

def random_int():
    arr = []
    arr2 = []
    arr.append(1)
    for i in range(1,6):
        n = random_gen()
        arr.insert(1, n)
    arr.append(1)
    for k in range(0,7):
        arr2.insert(0, 2**k)
    # read actual integer representation of the number generated in arr
    s = sum([a*b for a,b in zip(arr,arr2)])
    return s

def is_prob_prime():
    n = random_int()

    return n

def main():
    p = is_prob_prime()
    q = is_prob_prime()
    print(p)
    print(q)

main()
