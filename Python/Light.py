import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Math import Math
from sympy import Eq, Symbol, symbols


class Light:
    ''' Light class is object of Light, it has a lightsource -> self.s, and a vector -> self.v 
        in this class, it has a time to contral the length of light, for easier, the lightspeed c 
        has been setted 10 , time goes 0.1, axis goes 1
    '''
    # stcrution method, python only have one?
    # 4 name, source, vector ,time, and light

    def __init__(self, s=np.array([0, 0, 0]), v=np.array([0, 0, 1]), t=np.arange(0,10,1)):

        self._s = s
        self._v = v
        self._t = t
        self._light = Math.vector_trans(s)+Math.dot(t, v)

    def get_s(self):
        return self._s

    def set_s(self, s):
        self._s = s
        self.__set_light()

    def get_v(self):
        return self._v

    def set_v(self, v):
        self._v = v
        self.__set_light()

    def get_t(self):
        return self._t

    def set_t(self, t):
        self._t = t
        self.__set_light()

    def get_light(self):
        return self._light

    def __set_light(self):
        self._light = Math.vector_trans(self._s)+Math.dot(self._t, self._v)

    # we need get the light at a specfic time to solve formula, so we need to set t0 als Symbol
    def get_light_in_t0(self, t0: Symbol):
        # for solve , we need return in a array with three axis alone...
        x = self._s[0]+t0*self._v[0]
        y = self._s[1]+t0*self._v[1]
        z = self._s[2]+t0*self._v[2]
        return [x, y, z]

    # plot the light in 3D
    def plot(self, fig=plt.figure(), ax=plt.axes(projection='3d'), color='b'):
        # ax = fig.gca(projection='3d')
        ax.plot(self._light[0], self._light[1], self._light[2], color)
