import math

a = 1.0
b = -5.0
c = 6.0

d = b*b - 4*a*c

if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Two real roots: {r1:.2f} and {r2:.2f}")
elif d == 0:
    r1 = -b / (2*a)
    print(f"One real root: {r1:.2f}")
else:
    print("No real roots (weather trend unstable)")

