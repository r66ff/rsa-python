import sys, random, string

def random_gen():
    n = random.SystemRandom()
    n = n.getrandbits(7)
    n = bin(n)
    return n

def random_prime():
    n = random_gen()
    while len(n) < 9:
        n = random_gen()
    if n[8] == '0':
        n = n[:8] + '1'
    return n

def main():
    p = random_prime()
    q = random_prime()
    print(p)
    print(q)


main()
