import math

print(math.ceil(1.03))
print(math.ceil(-1.03))
# Smallest integer not less than itself

print(math.sqrt(81))
#print(math.sqrt(-81))

print(math.exp(2.0)) # e^2
print(math.exp(3.0)) # e^3

print(math.fabs(-1)) # absolute value

print(math.floor(1.03))  # largest number not greater than it
print(math.floor(-1.03)) 

print(math.log(2.0)) # log base e---as default
print(math.log(1024, 2)) # log(num, base)

print(math.log10(1000)) # log base 10

print(math.pow(3,6)) # 3^6

print(math.sin(30)) # sin(0) in radians
print(math.cos(30)) # sin(0) in radians
print(math.tan(60)) # tan(0) in radians


print(math.fmod(7.4, 3.3)) # returns modulus % resulting from division of x and y

print(math.fmod(-7.4, 3.3)) # this is more preferred for float as it's more precise

print(math.fmod(-8.3, 6))

print(math.pi) # pi

print(math.e) # e

print(math.factorial(5)) # 5!

print(math.gcd(12, 18)) # gcd

print(math.hypot(3, 4)) # hypotenuse

print(math.modf(3.14)) # returns fractional and integer part

print(math.trunc(3.14)) # returns integer part

print(math.remainder(5, 2)) # returns remainder

print(math.isfinite(3.14)) # returns True if finite

print(math.isinf(3.14)) # returns True if infinite

print(math.isnan(3.14)) # returns True if nan

print(math.isclose(3.14, 3.14)) # returns True if close

print(math.isqrt(16)) # returns square root

print(math.prod([1,2,3,4,5])) # returns product

print(math.perm(5, 2)) # returns permutation

print(math.comb(5, 2)) # returns combination

print(math.dist([1,2,3], [4,5,6])) # returns distance

print(math.erf(0.5)) # returns error function

print(math.erfc(0.5)) # returns complementary error function

print(math.gamma(0.5)) # returns gamma function

print(math.lgamma(0.5)) # returns log gamma function

print(math.lcm(12, 18)) # returns lcm

