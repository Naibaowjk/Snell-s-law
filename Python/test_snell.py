import matplotlib.pyplot as plt
import numpy as np
from Math import Math
from Light import Light
from Surface import Surface
from Physical import Physical
from Tree import *


def test1():

    fig = plt.Figure()
    ax = plt.axes(projection='3d')

    light_i = Light(np.array([-3, 5, 3]), np.array([-1, 0, -1]))
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())
    surface2 = Surface(np.array(
        [0, 1, -5]), np.array([0, 0, 1]), Surface().get_n_water(), Surface().get_n_air())
    phy = Physical()

    # first time
    light_t = phy.transmisson(surface, light_i)
    light_r = phy.reflection(surface, light_i)

    ms_t0 = phy.get_mp_and_t0(surface, light_i)
    x = float(ms_t0[0])
    y = float(ms_t0[1])
    z = float(ms_t0[2])
    t0 = float(ms_t0[3])

    light_i.set_t(np.arange(0, t0+t0/10, t0/10))

    # second time
    light_r2 = phy.reflection(surface2, light_t)
    light_t2 = phy.transmisson(surface2, light_t)

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

    return 0


def test2():
    fig = plt.Figure()
    ax = plt.axes(projection='3d')

    light_i = Light(np.array([-3, 5, 3]), np.array([-1, 0, -1]))
    surface = Surface(np.array([0, 1, 0]), np.array([0, 0, 1]))
    surface2 = Surface(np.array([0, 1, -5]), np.array([0, 0, 1]))
    list_surface = [surface, surface2]
    phy = Physical()

    # first time
    light_t = phy.transmisson(
        surface, light_i)
    light_r = phy.reflection(surface, light_i)

    list_ms_t0_s = phy.get_mp_t0_and_surface(list_surface, light_i)
    ms_t0 = list_ms_t0_s[0]
    x = float(ms_t0[0])
    y = float(ms_t0[1])
    z = float(ms_t0[2])
    t0 = float(ms_t0[3])

    light_i.set_t(np.arange(0, t0+t0/10, t0/10))

    # second time
    light_r2 = phy.reflection(surface2, light_t)
    light_t2 = phy.transmisson(
        surface2, light_t)

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
    return 0


def test3():
    light_i = Light(np.array([3, 0, 3]), np.array([-1, 0, -1]))
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())
    surface2 = Surface(np.array(
        [0, 1, -5]), np.array([0, 0, 1]), Surface().get_n_water(), Surface().get_n_air())
    surface3 = Surface(np.array(
        [0, 1, -10]), np.array([0, 0, 1]), Surface().get_n_air(), Surface().get_n_air())
    list_surface = [surface, surface2, surface3]
    phy = Physical()

    phy.run_plot(list_surface, light_i, 3, 10)

# ---------------------------------------------FOR SPECIAL CASE-----------------------------

# ------------------------------------------case 1: parallel surface


def test4():
    # light
    light_i = Light(np.array([-3, 5, 3]), np.array([1, 0, 0]))
    # surface
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())
    list_surface = [surface]
    # run
    Physical().run_plot(list_surface, light_i, 1, 5)

# ------------------------------------------case 2: directly


def test5():
    # surface
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())
    list_surface = [surface]
    # light
    light_i = Light(np.array([3, 2, 3]), np.array([0, 0, -1]))
    # run
    Physical().run_plot(list_surface, light_i, 1, 10)

# ------------------------------------------case 3: brust case


def test6():
    # surface
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_water(), Surface().get_n_air())
    list_surface = [surface]
    # light
    light_i = Light(np.array([3, 2, 3]), np.array([-1.4, 0, -1]))
    # run
    Physical().run_plot(list_surface, light_i, 1, 10)

# ------------------------------------------case 4: points on surface


def test7():
    # surface
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())
    list_surface = [surface]
    # light
    light_i = Light(np.array([0, 1, 0]), np.array([-1.4, 0, -1]))
    # run
    Physical().run_plot(list_surface, light_i, 1, 10)

# ------------------------------------------case 5: no light


def test8():
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())
    list_surface = [surface]
    # light
    light_i = Light(np.array([0, 1, 0]), np.array([0, 0, 0]))
    # run
    Physical().run_plot(list_surface, light_i, 1, 10)

# ------------------------------------------case 6: special surface


def test9():
    surface = Surface(np.array([0, 0, 0]), np.array([1, 0, 0]))
    fig = plt.Figure()
    ax = plt.axes(projection='3d')
    surface.plot(fig, ax)
    plt.show()

# ------------------------------------------case 7: almost directly


def test10():
    surface1 = Surface(np.array([0, 0, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())

    list_surface = [surface1]

    light_i = Light(np.array([0, 0, 1]), np.array([0.1, 0.1, -1]))

    Physical().run_plot(list_surface, light_i)
# ------------------------------------------case 8: for fun


def test11():
    surface1 = Surface(np.array([0, 0, 0]), np.array([1, 0, 0]))
    surface2 = Surface(np.array([0, 0, 0]), np.array([0, 0, 1]))
    surface3 = Surface(np.array([3, 0, 0]), np.array([1, 0, 0]))

    list_surface = [surface1, surface2, surface3]

    light_i = Light(np.array([0, 0, 1]), np.array([1, 0, -1]))

    Physical().run_plot(list_surface, light_i, 3, 6)


def test12():
    surface1 = Surface(np.array([0, 0, 0]), np.array(
        [-1, 0, 0]), Surface().get_n_metal(), Surface().get_n_water())
    surface2 = Surface(np.array([3, 0, 0]), np.array(
        [-1, 0, 0]), Surface().get_n_water(), Surface().get_n_metal())

    list_surface = [surface1, surface2]

    light_i = Light(np.array([0, 0, 1]), np.array([1, 0, -1]))
    # run
    Physical().run_plot(list_surface, light_i, 5, 30)


test12()
