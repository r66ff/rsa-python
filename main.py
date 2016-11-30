import sys, random, string

def random_gen():
    n = random.SystemRandom()
    n = n.getrandbits(32)
    b = bin(n)
    b = b[-1]
    b = int(b)
    print('Line # 6:\nGenerating a random number: %s\nExtracted random bit is: %s\n' % (n, b))
    return b

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
                    print('Line # 36:\nNot a prime: %s\n\n' % n)
                    return False  # this one is composite
                elif x == n - 1:
                    a = 0  # so we know loop didn't continue to end to not fall into 'if a:' statement that follows
                    break  # try another a
            if a:
                print('Line # 42:\nNot a prime: %s\n\n' % n)
                return False  # composite
    return True  # probably prime

def is_prob_prime():
    n = random_int()
    if miller_rabin(n):
        return n
    else:
        is_prob_prime()

def egcd(n, m):
    pa, a = 1, 0
    pb, b = 0, 1
    while m:
        k = n // m
        a, pa = pa - k * a, a
        b, pb = pb - k * b, b
        n, m = m, n % m
    return n, pa, pb

def find_e(phi):
    e = 3
    g, x, y = egcd(phi, e)
    print('\nLine # 66:\n g = %s, x = %s, y = %s\n\n' % (g, x, y))
    while g != 1:
        e = e + 1
        g, x, y = egcd(phi, e)
        print('\nLine # 70:\n g = %s, x = %s, y = %s\n\n' % (g, x, y))
    return e

def find_d(n, m):
    g, x, y = egcd(n, m)
    if g != 1:
        raise Exception('Private key d can not be found')
    else:
        return x % m

def generate_p_q():
    p = is_prob_prime()
    q = is_prob_prime()
    # check if overflow happened and check equality
    while (p == None or p == q):
        p = is_prob_prime()
    while (q == None or p == q):
        q = is_prob_prime()
    return p, q

def generate_p_q_n_phi_e():
    p, q = generate_p_q()

    print('Line # 93:\nPrime perhaps.. %s' % p)
    print('Prime perhaps.. %s' % q)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = find_e(phi)

    return p, q, n, phi, e

def main():
    p, q, n, phi, e = generate_p_q_n_phi_e()

    # I don't think e would ever happen to be undefined in this implementation, but just per the instructions including this check
    # Also I'm lame in unit testing and this code won't be sufficient if exception occures, but please give me feedback on how to this right:)
    while (e == None):
            p, q, n, phi, e = generate_p_q_n_phi_e()

    print('Line # 110:\nP is: %s\nQ is: %s\nN is: %s\nE is: %s' % (p, q, n, e))

    d = find_d(e, phi)

    print('D is: %s' % d)
    print("Alice's public key is (%s, %s)" % (n, e))
    print("Alice's private key is (%s, %s)" % (n, d))

    p = '{0:032b}'.format(p)
    q = '{0:032b}'.format(q)
    n = '{0:032b}'.format(n)
    e = '{0:032b}'.format(e)
    d = '{0:032b}'.format(d)
    print('\nNow same in binary:\nP is: %s\nQ is: %s\nN is: %s\nE is: %s\nD is: %s' % (p, q, n, e, d))
    print("Alice's public key is (%s, %s)" % (n, e))
    print("Alice's private key is (%s, %s)" % (n, d))

main()
