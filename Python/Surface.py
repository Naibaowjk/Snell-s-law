import numpy as np
from matplotlib import pyplot as plt
from sympy import Eq,Symbol,symbols

class Surface():
    ''' Suface must have a plot, and n vector, u can init this object by given a plot and vector.
        it provide a method to plot, use self.plot()

        p: a point
        n: n vector
        n1: reflective index in above, the same way with n vector
        n2: reflective index in under, the different way with n vector
    '''
    
    def __init__(self, p=np.array([0, 0, 0]), n=np.array([0, 0, 1]),n1=1,n2=1):
    # init method
        self._p = p
        self._n = n
        self._n_water = 1.3330
        self._n_ice = 1.306
        self._n_air = 1
        self._n_metal = 0.05
        self._n1 = n1
        self._n2 = n2


    def get_n_water(self):
        return self._n_water

    def get_n_ice(self):
        return self._n_ice

    def get_n_air(self):
        return self._n_air

    def get_n_metal(self):
        return self._n_metal

    # encapsulation p,n
    def get_p(self):
        return self._p

    def set_p(self, p):
        self._p = p

    def get_n(self):
        return self._n

    def set_n(self, n):
        self._n = n
    
    def get_n1(self):
        return self._n1

    def set_n1(self, n1):
        self._n1 = n1

    def get_n2(self):
        return self._n2

    def set_n2(self, n2):
        self._n2 = n2

    def get_eqn(self,X:Symbol,Y:Symbol,Z:Symbol):
        return Eq((X-self._p[0])*self._n[0]+(Y-self._p[1]) *
             self._n[1]+(Z-self._p[2])*self._n[2])

    def plot(self, fig=plt.Figure(),
             ax=plt.axes(projection='3d'), x=np.arange(-2, 2, 0.2), y=np.arange(-2, 2, 0.2) ):
        if self._n[2]!=0:
            X, Y = np.meshgrid(x, y)
            Z = ((X-self._p[0])*self._n[0]+(Y-self._p[1]) *
                self._n[1]-self._p[2]*self._n[2])/-self._n[2]
        else :
            if self._n[1]!=0:
                z=x
                X,Z=np.meshgrid(x,z)
                Y= ((X-self._p[0])*self._n[0]+(Z-self._p[2]) *
                    self._n[2]-self._p[1]*self._n[1])/-self._n[1]
            else :
                z=y
                Y,Z=np.meshgrid(y,z)
                X=((Z-self._p[2])*self._n[2]+(Y-self._p[1]) *
                self._n[1]-self._p[0]*self._n[0])/-self._n[0]
        ax.plot_surface(X, Y, Z)
    
    
