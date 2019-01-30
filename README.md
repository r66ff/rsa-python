# Simple implementation of RSA in python 3

### Run
* Clone the repo
* `python3.6 main.py`

### Notes
In this implementation
* E is 3 unless the Extended Euclidean check fails (a*x + b*y = g = gcd(x, y) if g != 1 we know there is a common divisor)
* Primes are probable primes tested by Miller–Rabin algorithm that runs 20 times
* Primes are small
* There is no enc and dec functions... yet