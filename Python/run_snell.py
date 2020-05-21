import matplotlib.pyplot as plt
import numpy as np
from Math import Math
from Light import Light
from Surface import Surface
from Physical import Physical
from Tree import *

# ---------------------------------------------RUN FOR SPECIAL CASE-----------------------------
# ------------------------------------------case 1: parallel surface
def run1():
    # light
    light_i = Light(np.array([-3, 5, 3]), np.array([1, 0, 0]))
    # surface
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())
    list_surface = [surface]
    # run
    Physical().run_plot(list_surface, light_i, 1, 5)
# ------------------------------------------case 2: directly
def run2():
    # surface
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())
    list_surface = [surface]
    # light
    light_i = Light(np.array([3, 2, 3]), np.array([0, 0, -1]))
    # run
    Physical().run_plot(list_surface, light_i, 1, 10)
# ------------------------------------------case 3: total internal reflection TIR case
def run3():
    # surface
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_water(), Surface().get_n_air())
    list_surface = [surface]
    # light
    light_i = Light(np.array([3, 2, 3]), np.array([-1.4, 0, -1]))
    # run
    Physical().run_plot(list_surface, light_i, 1, 10)
# ------------------------------------------case 4: points on surface
def run4():
    # surface
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())
    list_surface = [surface]
    # light
    light_i = Light(np.array([0, 1, 0]), np.array([-1.4, 0, -1]))
    # run
    Physical().run_plot(list_surface, light_i, 1, 10)
# ------------------------------------------case 5: no light
def run5():
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())
    list_surface = [surface]
    # light
    light_i = Light(np.array([0, 1, 0]), np.array([0, 0, 0]))
    # run
    Physical().run_plot(list_surface, light_i, 1, 10)
# ------------------------------------------case 6: special surface
def run6():
    surface = Surface(np.array([0, 0, 0]), np.array([1, 0, 0]))
    fig = plt.Figure()
    ax = plt.axes(projection='3d')
    surface.plot(fig, ax)
    plt.show()
# ------------------------------------------case 7: almost directly
def run7():
    surface1 = Surface(np.array([0, 0, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())

    list_surface = [surface1]

    light_i = Light(np.array([0, 0, 1]), np.array([0.1, 0.1, -1]))

    Physical().run_plot(list_surface, light_i)
# ------------------------------------------case 8: for fun
def run8():
    surface1 = Surface(np.array([0, 0, 0]), np.array([1, 0, 0]))
    surface2 = Surface(np.array([0, 0, 0]), np.array([0, 0, 1]))
    surface3 = Surface(np.array([3, 0, 0]), np.array([1, 0, 0]))

    list_surface = [surface1, surface2, surface3]

    light_i = Light(np.array([0, 0, 1]), np.array([1, 0, -1]))

    Physical().run_plot(list_surface, light_i, 3, 6)
# ------------------------------------------case 9: only reflction in Metal
def run9():
    surface1 = Surface(np.array([0, 0, 0]), np.array(
        [-1, 0, 0]), Surface().get_n_metal(), Surface().get_n_water())
    surface2 = Surface(np.array([3, 0, 0]), np.array(
        [-1, 0, 0]), Surface().get_n_water(), Surface().get_n_metal())

    list_surface = [surface1, surface2]

    light_i = Light(np.array([0, 0, 1]), np.array([1, 0, -1]))
    # run
    Physical().run_plot(list_surface, light_i, 5, 30)
