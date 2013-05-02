# Enter your answrs for chapter 7 here
# Name: Kelly Chiang

#NOTES
a = 4.0 #example from previous section
x = 3.0

x = y
y = (x + a/x) / 2
while True:
    print x
    y = (x + a/x) / 2
    if y == x:
        break 
    x = y

    
# Ex. 7.5

# Formula 1 = 2√2 ∑∞ (4k)!(1103 + 26390k) π 9801 k=0 (k!)43964k
#solution for 7.5: Need help with forming thoughts to create this in the future o_o (understand the pieces, but not sure how i would create this on my own!!)
import math

def factorial(n):
    """Computes factorial of n."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def estimate_pi():
    """Computes an estimate of pi.

    Algorithm due to Srinivasa Ramanujan, from 
    http://en.wikipedia.org/wiki/Pi
    """
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        term = factor * num / den
        total += term
        
        if abs(term) < 1e-15: break
        k += 1

    return 1 / total

# How many iterations does it take to converge?