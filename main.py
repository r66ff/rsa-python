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

def miller_rabin(n):
    # we know that n is an odd number between 65 and 127
    # running test 20 times
    for i in range(0,20):
        s, d = 0, n - 1
        while d & 1 == 0:
            s, d = s + 1, d >> 1
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x != 1 and x + 1 != n:
            for r in range(1, s):
                x = pow(x, 2, n)
                if x == 1:
                    return False  # this one is composite
                elif x == n - 1:
                    a = 0  # so we know loop didn't continue to end
                    break  # try another a
            if a:
                return False  # composite
    return True  # probably prime

def is_prob_prime():
    n = random_int()
    if miller_rabin(n):
        return n
    else:
        is_prob_prime()

def main():
    p = is_prob_prime()
    q = is_prob_prime()
    while (p == None):
        p = is_prob_prime()
    while (q == None):
        q = is_prob_prime()
    print(p)
    print(q)

main()
