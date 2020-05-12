import matplotlib.pyplot as plt
import numpy as np
from Math import Math
from Light import Light
from Surface import Surface
from Physical import Physical

fig = plt.Figure()
ax = plt.axes(projection='3d')

light_i = Light(np.array([-3, 5, 3]), np.array([-1, 0, -1]))
surface = Surface(np.array([0, 1, 0]), np.array([0, 0, 1]))
surface2 = Surface(np.array([0, 1, -5]), np.array([0, 0, 1]))
phy = Physical()

# first time
light_t = phy.transmisson(surface, light_i, phy.get_n_air(), phy.get_n_water())
light_r = phy.reflection(surface, light_i)

ms_t0 = phy.get_mp_and_t0(surface, light_i)
x = float(ms_t0[0])
y = float(ms_t0[1])
z = float(ms_t0[2])
t0 = float(ms_t0[3])

light_i.set_t(np.arange(0, t0+t0/10, t0/10))

# second time
light_r2 = phy.reflection(surface2, light_t)
light_t2 = phy.transmisson(
    surface2, light_t, phy.get_n_water(), phy.get_n_air())

ms_t1 = phy.get_mp_and_t0(surface2, light_t)
x2 = float(ms_t1[0])
y2 = float(ms_t1[1])
z2 = float(ms_t1[2])
t2 = float(ms_t1[3])

light_t.set_t(np.arange(0, t2+t2/10, t2/10))

# plot light and surface
surface.plot(fig, ax, np.arange(-5+x, 5+x, 0.2), np.arange(-5+y, 5+y, 0.2))
surface2.plot(fig, ax, np.arange(-5+x2, 5+x2, 0.2),
              np.arange(-5+y2, 5+y2, 0.2))
light_i.plot(fig, ax, 'b')
light_t.plot(fig, ax, 'g')
light_r.plot(fig, ax, 'g')
light_r2.plot(fig, ax, 'r')
light_t2.plot(fig, ax, 'r')


# plot n,n2
light_n = Light(np.array([x, y, z]), surface.get_n())
light_n.plot(fig, ax, 'y')

light_n2 = Light(np.array([x2, y2, z2]), surface2.get_n())
light_n2.plot(fig, ax, 'y')

plt.show()

