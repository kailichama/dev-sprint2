# Enter your answrs for chapter 6 here
# Name: Kelly Chiang


# Ex. 6.6



# Ex 6.8
#The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.
#One way to find the GCD of two numbers is Euclid’s algorithm, which is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.
#Write a function called gcd that takes parameters a and b and returns their greatest common divisor. If you need help, see http: // en. wikipedia. org/ wiki/ Euclidean_ algorithm .

def gcd(a, b):
    if a % b == 0;
    and b > a
        return b

#stackoverflow solution -- can someone explain?
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a