import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from Math import Math
from Light import Light
from Surface import Surface
from Tree import *


class Physical:
    ''' this class handle the transmisson and reflection of light, base on matlab code
        it have 2 method one is transmisson -> transmisson() 
        the other one is reflection -> reflection()  we need also to calcute the metting point of light and surface, method -> get_mp_and_t0()  will handle it

        more information pls see Readme on github. https://github.com/Naibaowjk/Snell-s-law
    '''

    def transmisson(self, surface=Surface(), light_in=Light()):
        # in parameter will get error, when set n1, n2 to n_air and n_water, so directly use value
        # return the transmisson light

        # get n vector , v_i
        n = surface.get_n()
        v_i = light_in.get_v()
        # set n1,n2 must judge the light way with n
        if np.dot(n, v_i) < 0:
            n1 = surface.get_n1()
            n2 = surface.get_n2()
        else:
            n2 = surface.get_n1()
            n1 = surface.get_n2()
            n = -n
        # get meeting point and time
        mp_t0 = self.get_mp_and_t0(surface, light_in)

        # set the source and time
        light_t = Light()
        light_t.set_s(np.array([mp_t0[0], mp_t0[1], mp_t0[2]]))
        light_t.set_t(np.arange(0, mp_t0[3]+mp_t0[3]/10, mp_t0[3]/10))

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
                # eq4 = Eq(np.dot(v_ts, v_i) /
                #          sqrt(np.dot(np.dot(v_ts, v_i), np.dot(v_ts, v_i))), 1)
                # solve equtions
                sol = solve([eq1, eq2, eq3], v_ts)
                # change type of sol
                v_ts1 = np.array([sol[0][0], sol[0][1], sol[0][2]])
                v_ts2 = np.array([sol[1][0], sol[1][1], sol[1][2]])
                # select on as solve
                if np.dot(v_i, v_ts1) > np.dot(v_i, v_ts2):
                    v_t = v_ts1
                else:
                    v_t = v_ts2
        light_t.set_v(np.array([v_t[0], v_t[1], v_t[2]]))
        return light_t

    def transmisson2(self, surface=Surface(), light_in=Light(), n1=1, n2=1.3330):
        # teacher's way
        # in parameter will get error, when set n1, n2 to n_air and n_water, so directly use value
        # return the transmisson light

        # get n vector , v_i
        n = surface.get_n()
        v_i = light_in.get_v()

        # set n1,n2 must judge the light way with n
        if np.dot(n, v_i) < 0:
            n1 = surface.get_n1()
            n2 = surface.get_n2()
        else:
            n2 = surface.get_n1()
            n1 = surface.get_n2()
            n = -n

        # get meeting point and time
        mp_t0 = self.get_mp_and_t0(surface, light_in)

        # set the source and time
        light_t = Light()
        light_t.set_s(np.array([mp_t0[0], mp_t0[1], mp_t0[2]]))
        light_t.set_t(np.arange(0, mp_t0[3]+mp_t0[3]/10, mp_t0[3]/10))

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
                v_tx = np.cross(np.cross(n, v_i), n)*n1/n2
                v_ty = -sqrt(np.dot(v_i, v_i)-np.dot(v_tx, v_tx))*n

                v_t = v_tx+v_ty
        light_t.set_v(np.array([v_t[0], v_t[1], v_t[2]]))
        return light_t

    def get_mp_and_t0(self, surface=Surface(), light=Light()):
        # mp is meetingpoint , t0 is the meeting time
        mp_t0 = np.array([0, 0, 0, 0])

        # get n,v_i,s
        n = surface.get_n()
        v_i = light.get_v()
        s = light.get_s()
        # for the case light and surface parallel, n*v' =0, and source is on surface, (s-p)*n'=0
        # let the point and time be 100
        if np.dot(n, v_i) == 0:
            t0 = 0
            mp_t0 = [0, 0, 0, 0]
        # source on surface
        else:
            if np.dot((s-surface.get_p()), n) == 0:
                mp_t0 = [s[0], s[1], s[2], 0]
            else:
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
        light_r.set_t(np.arange(0, mp_t0[3]+mp_t0[3]/10, mp_t0[3]/10))

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
            v_r = [sol[x_r], sol[y_r], sol[z_r]]
        else:
            v_r = next(iter(sol))

        light_r.set_v(np.array([v_r[0], v_r[1], v_r[2]]))

        return light_r

    def reflection2(self, surface=Surface(), light_in=Light()):
        # second way to get reflection

        # first to get meeting point
        mp_t0 = self.get_mp_and_t0(surface, light_in)

        # set the source and time
        light_r = Light()
        light_r.set_s(np.array([mp_t0[0], mp_t0[1], mp_t0[2]]))
        light_r.set_t(np.arange(0, mp_t0[3]+mp_t0[3]/10, mp_t0[3]/10))

        # get n vector , v_i
        n = surface.get_n()
        v_i = light_in.get_v()

        # get v_i shadow on n vector
        v_is = np.dot(-v_i, n)/sqrt(np.dot(n, n))
        # get sin vector p
        p = v_is+v_i
        # get v_r
        v_r = 2*p-v_i

        # set light_r._v
        light_r.set_v(v_r)
        return light_r

    def lightrun(self, list_surface=[Surface()], light_in=Light(), i_t=1):
        # i_t is reflection times and trans times
        # this function will simulate the ray, and return a tree and list_surface
        tree_light = Tree()
        tree_light.add(light_in)
        # this will be a for command for i_t
        for i in range(i_t):
            # calcute for list_surface
            # get myQueue length
            q_length = len(tree_light.myQueue)
            # run over myQueue,to add new light in tree, but we build a new list, queue is dynamic
            # select light
            list_light_temp = []
            for index in range(q_length):
                light_temp = tree_light.myQueue[index].elem
                list_light_temp.append(light_temp)

            for light_temp in list_light_temp:
                if light_temp == None:
                    # no light to reflect
                    tree_light.add(None)
                    tree_light.add(None)
                else:
                    # get p,t,surface
                    list_mpts = self.get_mp_t0_and_surface(
                        list_surface, light_temp)
                    mp_t0 = list_mpts[0]
                    surface_m = list_mpts[1]
                    # judge if surface is None
                    if surface_m == None:
                        # no reflect and transmisson
                        tree_light.add(None)
                        tree_light.add(None)
                    else:
                        # set the current light_in time
                        # find light_temp index in tree, through it's dynamic, bud no influence, cause if light_temp is finish , we dont need that
                        for i in range(len(tree_light.myQueue)):
                            if tree_light.myQueue[i].elem == light_temp:
                                index = i

                        tree_light.myQueue[index].elem.set_t(
                            np.arange(0, mp_t0[3]+mp_t0[3]/10, mp_t0[3]/10))
                        # set the point in surface is meeting point to save the value to plot
                        list_surface_index = list_surface.index(surface_m)
                        # mp = [mp_t0[0], mp_t0[1], mp_t0[2]]
                        # list_surface[list_surface_index].set_p(np.array(mp))

                        # calcute trans and ref
                        light_t_temp = self.transmisson2(surface_m, light_temp)
                        light_r_temp = self.reflection(surface_m, light_temp)
                        # add to tree
                        tree_light.add(light_t_temp)
                        tree_light.add(light_r_temp)
        return [tree_light, list_surface]

    def run_plot(self, list_surface=[Surface()], light_in=Light(), i=1, size=2 , isshow= True):
        # i is the times to t and r, size is the large of surface
        list_tree_surface = self.lightrun(list_surface, light_in, i)
        tree_light = list_tree_surface[0]
        list_surface = list_tree_surface[1]

        fig = plt.Figure()
        ax = plt.axes(projection='3d')
        # get all light to plot
        list_light = tree_light.level_queue(tree_light.root)
        # plot light and surface
        for light in list_light:
            light.plot(fig, ax)
        for surface in list_surface:
            x_p = surface.get_p()[0]
            y_p = surface.get_p()[1]
            surface.plot(fig, ax, x=np.arange(-size+x_p, size+x_p,
                                              size/5), y=np.arange(-size+y_p, size+y_p, size/5))
        if isshow :
            plt.show()

    def get_mp_t0_and_surface(self, list_surface=[Surface()], light_temp=Light()):
        # temp list to check min
        list_mp_t0_temp = []

        # get mp_t0 for all surface
        for surface_temp in list_surface:
            list_mp_t0_temp.append(
                self.get_mp_and_t0(surface_temp, light_temp))

        # check value , t >0 open a new list
        list_mp_t0_temp2 = []
        for mp_t0_temp in list_mp_t0_temp:
            if mp_t0_temp[3] > 0:
                list_mp_t0_temp2.append(mp_t0_temp)

        # get mp_t0 and the meeting surface
        # new time list to check
        list_t = []
        for mp_t0_temp2 in list_mp_t0_temp2:
            list_t.append(mp_t0_temp2[3])

        # get min index
        # if empty
        if(len(list_t)):
            # not empty
            index = list_t.index(min(list_t))
            mp_t0 = list_mp_t0_temp2[index]
            surface_m = list_surface[list_mp_t0_temp.index(mp_t0)]
        else:
            # empty
            # 从这里开始，先考虑平行的情况，如果时间数组为空，说明没有交点（此时没有考虑平行，正在改进），需要返回一个值
            mp_t0 = [0, 0, 0, 0]
            surface_m = None
            pass

        # return them on a list
        list_mpts = [mp_t0, surface_m]
        return list_mpts
