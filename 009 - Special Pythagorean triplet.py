import math
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_triplet(x):
    a = x[0]
    b = x[1]
    return(math.sqrt(a**2 + b**2) + (a + b) == 1000)

x = [200,375]
print(math.sqrt(x[0]**2 + x[1]**2) + (x[0] + x[1]))
print(is_triplet([200,375]))

# We know it's generally less than 500 or so per side
tests = [[a,b] for a in range(1,500) for b in range(1,500) if (math.sqrt(a**2 + b**2) + (a + b) == 1000)]

a = tests[0][0]
b = tests[0][1]
c = 1000 - a - b
print(a*b*c)