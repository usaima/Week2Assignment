# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:01:07 2017

@author: OPS
"""
""" x = a + bj
    x = 3 + 2j
    a=3 , b= 2... find angle theta
"""
import math

def polar(x):
    r = x.real
    i = x.imag
    theta = math.atan2(i,r)
    return theta
    
z = 3+5j
print(polar(z))