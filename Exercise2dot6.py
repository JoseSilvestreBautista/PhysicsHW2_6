import math

G = float(6.6738E-11)
M = float(1.9891e30)
print("Please enter the perihelion distance in meters")
L1 = float(input())
print("Please enter the perihelion velocity in meters per second")
V1 = float(input())

# obtaining V2
a = 1
b = -(2.0 * G * M) / (L1 * V1)
c = -((V1 ** 2) - ((2.0 * G * M) / L1))

d = (b ** 2) - (4 * a * c)

sol1 = (-b - math.sqrt(d)) / (2 * a)
sol2 = (-b + math.sqrt(d)) / (2 * a)

if sol2 < V1:
    V2 = sol2
else:
    V2 = sol2

V2 = sol1

print("The aphelion velocity is", V2, "meters per second.")

# obtaining L2
L2 = (L1 * V1) / V2
print("The aphelion distance is", L2, "meters or", L2/1000,"kilometers.")

# obtaining Orbital period
semiMajorAxis = (1 / 2) * (L1 + L2)
semiMinorAxis = math.sqrt(L1 * L2)
T = (2.0 * math.pi * semiMajorAxis * semiMinorAxis) / (L1 * V1)
secondsInAYear = 60 * 60 * 24 * 365
print("The orbital period is", T, "seconds or", T / secondsInAYear, "year(s).")

# obtaining the orbital eccentricity:
e = (L2 - L1) / (L2 + L1)
print("The orbital eccentricity is", e)

# Results using earth's perihelion distance and velocity: L1 = float(1.4710e11) and V1 = float(3.0287e4)
# The aphelion velocity is 29305.39917726127 meters per second.
# The aphelion distance is 152027197208.65994 meters.
# The orbital period is 31543060.207886923 seconds or 1.0002238777234564 year(s).
# The orbital eccentricity is 0.01647191313474219

# Results using Halley’s comet perihelion distance and velocity: L1 = float(8.7830e10) and V1 = float(5.4529e4)
# The aphelion velocity is 906.6806969191493 meters per second.
# The aphelion distance is 5282214660876.441 meters.
# The orbital period is 2399312511.8451877 seconds or 76.08170065465461 year(s).
# The orbital eccentricity is 0.9672889126454061
