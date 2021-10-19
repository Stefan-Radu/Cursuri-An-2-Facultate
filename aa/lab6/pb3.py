# Problema 3 - Stefan-Octavian Radu - 234 - 2

from math import sqrt

a, b, c, d = (), (), (), ()

# citesc punctele
with open('input', 'r') as f:
  lines = f.readlines()
  a = tuple(int(x) for x in lines[0].split())
  b = tuple(int(x) for x in lines[1].split())
  c = tuple(int(x) for x in lines[2].split())
  d = tuple(int(x) for x in lines[3].split())


# swap ca sa nu lucrez cu verticale ca imi da cu infinit la panta
if a[0] == b[0]:
  b, c = c, b


def get_slope(a, b):
  x1, y1 = a
  x2, y2 = b
  return (y2 - y1) / (x2 - x1)


def get_orthogonal_slope(m):
  return -(1 / m)


# mijloc de AB
middle_ab = ((b[0] + a[0]) / 2, (b[1] + a[1]) / 2)
# panta dreptei perpendiculare pe AB
m1 = get_orthogonal_slope(get_slope(a, b))

# mijloc de bc 
middle_bc = ((c[0] + b[0]) / 2, (c[1] + b[1]) / 2)
# panta dreptei perpendiculare pe BC
m2 = get_orthogonal_slope(get_slope(b, c))

# coordonata x a intersectiei mediatoarelor
x = (m1 * middle_ab[0] - m2 * middle_bc[0] + \
     middle_bc[1] - middle_ab[1]) / (m1 - m2)

# coordonata y a intersectiei mediatoarelor
y = m1 * (x - middle_ab[0]) + middle_ab[1]

# verificare
assert y == m2 * (x - middle_bc[0]) + middle_bc[1]

# centrul cercului circumscris
centre = (x, y)

def euclidian(a, b):
  x1, y1 = a
  x2, y2 = b
  return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# distanta de la centru la d
d = euclidian(centre, d)
# raza cercului
r = euclidian(centre, a)
# verircare
assert r == euclidian(centre, b) == euclidian(centre, c)

if d < r:
  print('interior')
elif d > r:
  print('exterior')
else:
  print('pe raza')
