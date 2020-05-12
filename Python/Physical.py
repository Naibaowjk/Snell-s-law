import numpy as np
from sympy import *
from Math import Math
from Light import Light
from Surface import Surface


class Physical:
    ''' this class handle the transmisson and reflection of light, base on matlab code
        it have 2 method one is transmisson -> transmisson() 
        the other one is reflection -> reflection()  we need also to calcute the metting point of light and surface, method -> get_meetingpoint()  will handle it
    '''

    def __init__(self):
        # somebasical refractive index, also private
        self._n_water = 1.3330
        self._n_ice = 1.306
        self._n_air = 1

    def get_n_water(self):
        return self._n_water

    def get_n_ice(self):
        return self._n_ice

    def get_n_air(self):
        return self._n_air

    def transmisson(self, surface=Surface(), light_in=Light(), n1=1, n2=1.3330):
        # in parameter will get error, when set n1, n2 to n_air and n_water, so directly use value
        # return the transmisson light
        # get meeting point and time

        mp_t0 = self.get_mp_and_t0(surface, light_in)

        # set the source and time
        light_t = Light()
        light_t.set_s(np.array([mp_t0[0], mp_t0[1], mp_t0[2]]))
        light_t.set_t(np.arange(0, mp_t0[3]+mp_t0[3]/10, mp_t0[3]/10))

        # get n vector , v_i
        n = surface.get_n()
        v_i = light_in.get_v()

        # sin（theta1),sin(theta2),cos(theta1),cos(theta2)
        cos1 = np.dot(-v_i, n)/sqrt(np.dot(v_i, v_i)*np.dot(n, n))
        sin1 = sqrt(1-cos1**2)
        sin2 = n1*sin1/n2
        cos2 = sqrt(1-sin2**2)

        # calculate brust angle
        sin2_b = 1
        sin1_b = n2*sin2_b/n1

        # check special case, n vector is equal with -v_i, directly trans
        if (np.cross(n, -v_i) == [0, 0, 0]).all():
            v_t = v_i
        else:
            # check brust case
            if (n1 >= n2) & (sin1 >= sin1_b):
                v_t = np.array([0, 0, 0])

            # normal case
            else:
                # 3 symbols to calculate v_t
                x_t, y_t, z_t = symbols('x_t y_t z_t')
                # v_t need to solve
                v_ts = [x_t, y_t, z_t]

                # 3 equtions
                eq1 = Eq(np.dot(v_ts, np.cross(v_i, n)))
                eq2 = Eq(np.dot(v_ts, v_ts), np.dot(v_i, v_i))
                eq3 = Eq(np.dot(v_ts, -n) /
                         sqrt(np.dot(v_ts, v_ts)*np.dot(-n, -n)), cos2)
                eq4 = Eq(np.dot(v_ts, v_i) /
                         sqrt(np.dot(np.dot(v_ts, v_i), np.dot(v_ts, v_i))), 1)
                # solve equtions
                sol = solve([eq1, eq2, eq3, eq4], v_ts)

                # change type of sol
                v_t = next(iter(sol))
        light_t.set_v(np.array([v_t[0], v_t[1], v_t[2]]))
        return light_t

    def get_mp_and_t0(self, surface=Surface(), light=Light()):
        # mp is meetingpoint , t0 is the meeting time
        mp_t0 = np.array([0, 0, 0, 0])
        # to diffcult to do this in Python, but we need do it
        x, y, z, t0 = symbols('x y z t0')
        light_in_t0 = light.get_light_in_t0(t0)
        # get surface eqn for 1
        eq1 = surface.get_eqn(x, y, z)
        # eqn2 for x
        eq2 = Eq(x, light_in_t0[0])
        eq3 = Eq(y, light_in_t0[1])
        eq4 = Eq(z, light_in_t0[2])
        sol = linsolve([eq1, eq2, eq3, eq4], [x, y, z, t0])
        mp_t0 = next(iter(sol))
        return mp_t0

    def reflection(self, surface=Surface(), light_in=Light()):
        # this methond handled reflection
        mp_t0 = self.get_mp_and_t0(surface, light_in)

        # set the source and time
        light_r = Light()
        light_r.set_s(np.array([mp_t0[0], mp_t0[1], mp_t0[2]]))
        light_r.set_t(np.arange(0, mp_t0[3]+mp_t0[3]/10,mp_t0[3]/10))

        # get n vector , v_i
        n = surface.get_n()
        v_i = light_in.get_v()

        # 3 sysmols to solve equation
        x_r, y_r, z_r = symbols('x_r y_r z_r')
        # v_r need to solve
        v_rs = [x_r, y_r, z_r]

        # 2 equations
        eq1 = Eq(np.dot(-v_i, n), np.dot(v_rs, n))
        eq2 = Eq(np.cross(-v_i+v_rs, n)[0])
        eq3 = Eq(np.cross(-v_i+v_rs, n)[1])
        eq4 = Eq(np.cross(-v_i+v_rs, n)[2])

        # solve equation
        sol = solve([eq1, eq2, eq3, eq4], v_rs)
        # change type of sol
        # sb python will return want ever it like...
        if type(sol) == dict:
            x_r
            v_r = [sol[x_r], sol[y_r], sol[z_r]]
        else:
            v_r = next(iter(sol))

        light_r.set_v(np.array([v_r[0], v_r[1], v_r[2]]))

        return light_r
