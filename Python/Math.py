import numpy as np
from functools import singledispatch

class Math:
    # python support not generic function in staticmethod
    @staticmethod
    def vector_trans(v):
        if type(v) != np.ndarray:
            return NotImplemented
        length = np.size(v)
        return np.reshape(v, [length, 1])

    @staticmethod
    # this Method solve for t.*v' is ilegal in Python, so do it myself
    # ATTENTION: IT CAN HANDLE TRANSMISSON
    def dot(t,v):
        # check type...
        b= (type(t)!=np.ndarray) & (type(v)!=np.ndarray)
        if b:
            return 0
        # transmisson v
        v=Math.vector_trans(v)
        # row,columns for result
        r=np.size(v)
        c=np.size(t)
        # init result array
        l=np.zeros([r,c])
        # check whether np.ndarray
        # no do-while
        for i in range(c):
            for j in range(r):
                l[j,i]=t[i]*v[j]
        return l
