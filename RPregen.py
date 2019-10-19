from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv

line1 = ('1 28376U 04026A   19291.92920195  .00000086  00000-0  29195-4 0  9991')
line2 = ('2 28376  98.2052 233.1216 0001349  69.4330 290.7013 14.57111056811603')

satellite = twoline2rv(line1, line2, wgs72)

for i in range(0, 60):
    position, velocity = satellite.propagate(2019, 10, 19, 19, 0+i, 0)
    print(position)
 