import numpy as np
from matplotlib import pyplot as plt
from sympy import Eq,Symbol,symbols

class Surface():
    ''' Suface must have a plot, and n vector, u can init this object by given a plot and vector.
        it provide a method to plot, use self.plot()
    '''
    
    def __init__(self, p=np.array([0, 0, 0]), n=np.array([0, 0, 1])):
    # init method
        self._p = p
        self._n = n

    # encapsulation s,n
    def get_p(self):
        return self._p

    def set_p(self, p):
        self._p = p

    def get_n(self):
        return self._n

    def set_n(self, n):
        self._n = n

    def get_eqn(self,X:Symbol,Y:Symbol,Z:Symbol):
        return Eq((X-self._p[0])*self._n[0]+(Y-self._p[1]) *
             self._n[1]+(Z-self._p[2])*self._n[2])

    def plot(self, fig=plt.Figure(),
             ax=plt.axes(projection='3d'), x=np.arange(-2, 2, 0.2), y=np.arange(-2, 2, 0.2) ):
        X, Y = np.meshgrid(x, y)
        Z = ((X-self._p[0])*self._n[0]+(Y-self._p[1]) *
             self._n[1]-self._p[2]*self._n[2])/-self._n[2]
        ax.plot_surface(X, Y, Z)
    
    
