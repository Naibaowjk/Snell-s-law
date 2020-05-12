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

#### -*Environment*

programm has been tested in Win10, Python3.8

have 3 package installed:
1. Numpy
2. Matplotlib
3. Sympy


