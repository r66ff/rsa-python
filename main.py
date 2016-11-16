import sys, random, string

def random_gen():
    n = random.SystemRandom()
    n = n.getrandbits(1)
    return n

def random_prime():
    arr = []
    arr.append(1)
    for i in range(1,6):
        n = random_gen()
        arr.insert(1, n)
    arr.append(1)
    arr = map(str, arr)
    s = ''.join(arr)
    s = int(s)
    return s

def main():
    p = random_prime()
    q = random_prime()
    print(type(p))
    print(q)


main()
