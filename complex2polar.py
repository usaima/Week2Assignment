import math

def r(c1):
    rofc = c1.real
    iofc = c1.imag
    result = rofc**2 + iofc**2
    result = math.sqrt(result)
    return result

def angle(c1):
    return math.atan2(c1.imag , c1.real)

a = 5 + 2j

print("r = ",r(a))
print("angle = ",angle(a))
