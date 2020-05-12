import matplotlib.pyplot as plt
import numpy as np
from Math import Math
from Light import Light
from Surface import Surface
from Physical import Physical

fig = plt.Figure()
ax = plt.axes(projection='3d')

light_i=Light(np.array([-3,5,3]),np.array([-1.4,0,-1]))
surface= Surface(np.array([0,1,0]),np.array([0,0,1]))

phy=Physical()


light_t=phy.transmisson(surface,light_i,phy.get_n_water(),phy.get_n_air())
light_r=phy.reflection(surface,light_i)

ms_t0=phy.get_mp_and_t0(surface,light_i)
x=float(ms_t0[0])
y=float(ms_t0[1])
t0=float(ms_t0[3])

light_i.set_t(np.arange(0,t0+t0/10,t0/10))

surface.plot(fig,ax,np.arange(-5+x,5+x,0.2),np.arange(-5+y,5+y,0.2))
light_i.plot(fig,ax,'b')
light_t.plot(fig,ax,'g')
light_r.plot(fig,ax,'g')

plt.show()


