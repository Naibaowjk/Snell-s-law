# Snell-s-law
It's implemented with python and matlab, Only the incident and refractive directions on a surface are realized, without considering the amplitude size of the TEM wave

## **Theory**

Wiki has page about Snell's law

in this code, it use time 't' to contral the length of line of light, like **s+t*v**
surface has eqution, so light & surface will get the meeting point **p** and time **t0**
then build some equtions for transmisson and reflection, solve the vector of transmisson **v_t** and reflection light **v_r**

finally plot them all in a figure

![Math Module View1](/Image/Theory1.jpg)

Class: Light, Surface will have this attributes, and Math will do something to get right calculating.

This picture will show the Algorithm of Snell's Law. the Core methond is lightrun()
![Math Module View2](/Image/Theory2.jpg)

as alternative, for transmisson and reflection, we have transmisson2() and reflection2(),transmisson2 works good, reflection2 maybe have bugs, not very reliable .

at last, we will show you some detail of this Algorithm.

- Dont't have metting point :

we get 2 eqautions to solve, if no meeting point, we consider it on first and set t0 = 0, it also has a situation that t0<0 , it means also not hit. so can only judge if t0>0.

for the really hit surface, t0 must be the minimal of list_t0.

- Special case: 

for case2 , case3, we use some if command to get transmisson light

- How to judge the reflection index.

we can calculate surface.get_n()*light.get_v() , if >0 , then from n1 to n2, else from n2 t0 n1.

- What's tree looks like in few times refecltion

![Math Module View3](/Image/Theory3.jpg)



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