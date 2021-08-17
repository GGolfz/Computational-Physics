import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output
# sx = ucos(theta)(t)
# sy = usin(theta)(t) - (1/2)(g)(t^2)
u = 30
theta = 45
g = 9.8
sy = 0
sx = 0
START_Y = 0
ux = u* np.cos(theta)
uy = u* np.sin(theta)
x = []
y = []
ms = 0
while sy >= -START_Y:
  t = ms / 1000
  sx = ux * t
  sy = uy * t - (1/2) * (g) * (t*t)
  y.append(sy)
  x.append(sx)
  ms += 1
plt.plot(x,y)
