# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:15:05 2020

@author: hdafa
"""

def fact(n):
    """
    Returns the factorial of n

    Parameters
    ----------
    n : positive integer
        n! = 2 x 3 x ... x (n-1) x n.

    Returns 
    -------
    int
        the factorial.

    """
    if n==0 or n==1:
        return 1
    return fact(n-1)*n

