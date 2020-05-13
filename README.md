# Snell-s-law
It's implemented with python and matlab, Only the incident and refractive directions on a surface are realized, without considering the amplitude size of the TEM wave

## **Theory**

Wiki has page about Snell's law

in this code, it use time 't' to contral the length of line of light, like **s+t*v**
surface has eqution, so light & surface will get the meeting point **p** and time **t0**
then build some equtions for transmisson and reflection, solve the vector of transmisson **v_t** and reflection light **v_r**

finally plot them all in a figure

## **for Matlab**
it has been tested working suitable for Matlab2019b, for 2020a or later, it may have errors in solve(), should change the eqn with vertor type into 3 different linear eqn.

it has a lot of Comments to unterstand the programm

## **for Python**

I first done it in Matlab, so python's version is only copy for matlab, I recommand first to see the code in matlab and then in python.

to get the result, should run test_snell.py.

#### 1.Environment

programm has been tested in Win10, Python3.8

have 3 package installed:
1. Numpy
2. Matplotlib
3. Sympy

#### 2.special case test information

- case1:

The light and surface is parallel 

![test1](/Image/Figure_T1.png)

- case2:

The light hits the Surface vertically

![test2](/Image/Figure_T2.png)

- case3:

Total internal reflection TIR case, in code comments we call it burst, it's a mistake

![test3](/Image/Figure_T3.png)

- case4:

The light source is on the plane, we set it don't do anything

![test4](/Image/Figure_T4.png)

- case5:

no light only a point, we don't see anything

![test5](/Image/Figure_T5.png)


- case6:

we test the Surface().plot in special case , if the plane equation is Ax+By+C=0, we make sure when any of A,B,C=0 can plot on figure.

![test6](/Image/Figure_T6.png)

- case7:

The light hits the Surface vertically almost

![test7](/Image/Figure_T7.png)

- case 8:

We have realized the reflection and refraction(in this demo we call it transmisson) of light in any number of planes, and the number of reflections and refractions is also adjustable

But as you can see, we still get some problem to plot the Surface, it has bugs , we are working on it
![test8](/Image/Figure_T8.png)

- case 9:

We have simulated the route of light in non-transparent media or electromagnetic waves in metal conductors, and we have not considered TEM waves

![test9](/Image/Figure_T9.png)


### Powered by Naibaoofficial and SFliang