# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:50:56 2019

@author: Andrew
"""

def nonlinear_regression(x1,x2,y):
    
    m1 = 0
    m2 = 0
    m3 = 0
    b = 0

    def partialD_m1(x1,x2,y,m1,m2,m3,b):
        n = len(x1)
        deriv = 0
        for i in range (0,n):
            y_pred = m1*x1[i]+ m2*x2[i] + m3*x2[i]**2 +b
            deriv = deriv + (x1[i]*(y[i]-y_pred))
        output = (-2/n)*deriv
        return output

    def partialD_m2(x1,x2,y,m1,m2,m3,b):
        n = len(x1)
        deriv = 0
        for i in range (0,n):
            y_pred = m1*x1[i]+ m2*x2[i] + m3*x2[i]**2 +b
            deriv = deriv + (x2[i]*(y[i]-y_pred))
        output = (-2/n)*deriv
        return output
    
    def partialD_m3(x1,x2,y,m1,m2,m3,b):
        n = len(x1)
        deriv = 0
        for i in range (0,n):
            y_pred = m1*x1[i]+ m2*x2[i] + m3*x2[i]**2 +b
            deriv = deriv + (x2[i]**2*(y[i]-y_pred))
        output = (-2/n)*deriv
        return output
    
    def partialD_b(x1,x2,y,m1,m2,m3,b):
        n = len(x1)
        deriv = 0
        for i in range (0,n):
            y_pred = m1*x1[i]+ m2*x2[i] + m3*x2[i]**2 +b
            deriv = deriv + (y[i]-y_pred)
        output = (-2/n)*deriv
        return output
    
    lr = 1*10**-3
    precision = 1*10**-8
    
    m1_diff = 100
    m2_diff = 100
    m3_diff = 100
    b_diff = 100
    
    while m1_diff > precision:
        m1_prev = m1
        m1 = m1 - lr*partialD_m1(x1,x2,y,m1,m2,m3,b)
        m1_diff = abs(m1_prev - m1)
        
    while m2_diff > precision:
        m2_prev = m2
        m2 = m2 - lr*partialD_m2(x1,x2,y,m1,m2,m3,b)
        m2_diff = abs(m2_prev - m2)
        
    while m3_diff > precision:
        m3_prev = m3
        m3 = m3 - lr*partialD_m3(x1,x2,y,m1,m2,m3,b)
        m3_diff = abs(m3_prev - m3)
        
    while b_diff > precision:
        b_prev = b
        b = b - lr*partialD_b(x1,x2,y,m1,m2,m3,b)
        b_diff = abs(b_prev - b)

    return [m1,m2,m3,b]
    
# Creating data to test the gradient descent

studytimes = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
gymtimes = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5]

n_test = len(studytimes)
grades = []

m1_test = 2
m2_test = 3
m3_test = 4
b_test = 5

for i in range (0,n_test):
    x1 = studytimes[i]
    x2 = gymtimes[i]
    y = m1_test*x1+m2_test*x2+m3_test*x2**2+b_test
    grades.append(y)

print(nonlinear_regression(studytimes,gymtimes,grades))
