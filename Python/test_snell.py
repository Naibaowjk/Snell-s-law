import matplotlib.pyplot as plt
import numpy as np
from Math import Math
from Light import Light
from Surface import Surface
from Physical import Physical
from Tree import *


def test1():
    ''' Test 3 speicial case
            1. When Light is parallel the surface, the Light don't hit the Surface.
            2. When Light source is on the surface.
            3. When no Light, it's is equal situation with parallel
        This 3 cases will judge in Physical.get_mp_and_t0(), it will return t0=0
    '''
    # the light parallel to surface
    light_i1 = Light(np.array([-3, 5, 3]), np.array([1, 0, 0]))
    light_i2 = Light(np.array([0, 1, 0]), np.array([-1.4, 0, -1]))
    light_i3 = Light(np.array([0, 1, 0]), np.array([0, 0, 0]))
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_air(), Surface().get_n_water())
    phy = Physical()
    ms_t0_1 = phy.get_mp_and_t0(surface, light_i1)
    ms_t0_2 = phy.get_mp_and_t0(surface, light_i2)
    ms_t0_3 = phy.get_mp_and_t0(surface, light_i3)
    t1 = ms_t0_1[3]
    t2 = ms_t0_2[3]
    t3 = ms_t0_3[3]
    assert (t1 == 0) & (t2 == 0) & (t3 == 0)


def test2():
    ''' Test when the Light vertically hits the Surface
        we set the hits time only by 1 and only have 1 surface
        the light transmision light_t.v will equal with  light_i.v
    '''
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_water(), Surface().get_n_air())
    list_surface = [surface]
    # light
    light_i = Light(np.array([3, 2, 3]), np.array([0, 0, -1]))

    phy = Physical()

    list_tree_surface = phy.lightrun(list_surface, light_i, 1)
    tree_light = list_tree_surface[0]
    list_surface = list_tree_surface[1]
    list_light = tree_light.level_queue(tree_light.root)

    assert (list_light[0].get_v() == list_light[1].get_v()).all()


def test3():
    ''' Test total internal reflection TIR case
        when no transmission, it will be no light_t,
        if
            the hits times is 1
        the light_t.get_v() is [0,0,0]
    '''
    # surface
    surface = Surface(np.array([0, 1, 0]), np.array(
        [0, 0, 1]), Surface().get_n_water(), Surface().get_n_air())
    list_surface = [surface]
    # light
    light_i = Light(np.array([3, 2, 3]), np.array([-1.4, 0, -1]))
    # Physical object
    phy = Physical()

    list_tree_surface = phy.lightrun(list_surface, light_i, 1)
    tree_light = list_tree_surface[0]
    list_surface = list_tree_surface[1]
    list_light = tree_light.level_queue(tree_light.root)

    assert (list_light[1].get_v() == np.array([0, 0, 0])).all()


def test4():
    ''' Normal case, one time reflection and one time transmisson , light in air through the air.
        data : light source [-1 0 1], light vector [1 0 -1], surface is xoy,n1=1 n2=1
        esay to hand calculate 
               light_r.s = [0,0,0] light_r.vector = [1,0,1]
               light_t.s = [0,0,0] lgiht_t.vector = [1,0,-1]
    '''
    light_i = Light(np.array([-1, 0, 1]), np.array([1, 0, -1]))
    surface = Surface()
    list_surface = [surface]
    phy = Physical()

    list_tree_surface = phy.lightrun(list_surface, light_i, 1)
    tree_light = list_tree_surface[0]
    list_surface = list_tree_surface[1]
    list_light = tree_light.level_queue(tree_light.root)

    light_r = list_light[2]
    light_t = list_light[1]

    b1 = (light_r.get_s() == np.array([0, 0, 0])).all()
    b2 = (light_r.get_v() == np.array([1, 0, 1])).all()
    b3 = (light_t.get_s() == np.array([0, 0, 0])).all()
    b4 = (light_t.get_v() == np.array([1, 0, -1])).all()
    assert b1 & b2 & b3 & b4
