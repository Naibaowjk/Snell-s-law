import numpy as np
from functools import singledispatch

class Math:
    """
        provides some static method for matrix calculating.

        method:
        vector_trans(v): static method, return transpose
        dot(t,v): return t.*v'
    """
    # python support not generic function in staticmethod
    @staticmethod
    def vector_trans(v):
        """ this will return the transpose of vector
            args: v: must be np.ndarray
            return transpose of v
        """
        if type(v) != np.ndarray:
            return NotImplemented
        length = np.size(v)
        return np.reshape(v, [length, 1])

    @staticmethod
    # this Method solve for t.*v' is ilegal in Python, so do it myself
    # ATTENTION: IT CAN HANDLE TRANSMISSON
    def dot(t,v):
        """ this Method solve for t.*v' is ilegal in Python, so do it myself
            args : t,v are vectors, must be np.ndaary or u will get nothing
            return:
                    t.*v' 
            for example: 
                    t = np.array([1,2,3])
                    v = np.array([1,2,3])
                    Math.dot(t,v) will return 
                    [[1,2,3],[2,4,6],[3,6,9]]
        """
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
