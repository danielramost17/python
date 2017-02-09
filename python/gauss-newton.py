#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 09:36:22 2017

@author: daniel
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

#Les valeurs initiales
X = [1, 2, 3, 4, 5, 6, 7, 8]
Y = [0.127, 0.2, 0.3, 0.25, 0.32, 0.5, 0.7, 0.9]
iterations = 10
rows = 8
cols = 6
B = np.matrix([[1],[1],[1],[1],[3],[6]])
sumOfResid_initial = sumOfResid_diff = 1000

#Le Jacobian de r
Jf = np.zeros((rows,cols))
r = np.zeros((rows,1)) 
approx = np.zeros((rows,1)) 

#Les derivees de r
def partialDerB1(B2,B3,B4,B5,B6,x):
   return np.exp(-0.5*((x-B5)/B3)**2) 

def partialDerB2(B1,B3,B4,B5,B6,x):
   return np.exp(-0.5*((x-B6)/B4)**2)

def partialDerB3(B1,B2,B3,B4,B5,B6,x):
   return (((x-B5)**2)/B3**3)*B1*np.exp((-(x-B5)**2)/(2*B3**2)) 

def partialDerB4(B1,B2,B3,B4,B5,B6,x):
   return (((x-B6)**2)/B4**3)*B2*np.exp((-(x-B6)**2)/(2*B4**2))
   
def partialDerB5(B1,B2,B3,B4,B5,B6,x):
   return (((x-B5))/B3**2)*B1*np.exp((-(x-B5)**2)/(2*B3**2)) 

def partialDerB6(B1,B2,B3,B4,B5,B6,x):
   return (((x-B6))/B4**2)*B2*np.exp((-(x-B6)**2)/(2*B4**2))

def residual(x,y,B1,B2,B3,B4,B5,B6):
   return (y - B1*np.exp((-(x-B5)**2)/(2*B3**2)) - B2*np.exp((-(x-B6)**2)/(2*B4**2)))
   
def g(x,B1,B2,B3,B4,B5,B6):
   return (B1*np.exp((-(x-B5)**2)/(2*B3**2)) + B2*np.exp((-(x-B6)**2)/(2*B4**2)))

#On calcule le jacobian
for i in range(iterations):
   sumOfResid=0
   for j in range(rows):
      r[j,0] = residual(X[j],Y[j],B[0],B[1],B[2],B[3],B[4],B[5])
      approx[j,0] = g(X[j],B[0],B[1],B[2],B[3],B[4],B[5])
      sumOfResid += (r[j,0] * r[j,0])
      sumOfResid_diff = sumOfResid_initial - sumOfResid
      sumOfResid_initial = sumOfResid
      Jf[j,0] = partialDerB1(B[1],B[2],B[3],B[4],B[5],X[j])
      Jf[j,1] = partialDerB2(B[0],B[2],B[3],B[4],B[5],X[j])
      Jf[j,2] = partialDerB3(B[0],B[1],B[2],B[3],B[4],B[5],X[j])
      Jf[j,3] = partialDerB4(B[0],B[1],B[2],B[3],B[4],B[5],X[j])
      Jf[j,4] = partialDerB5(B[0],B[1],B[2],B[3],B[4],B[5],X[j])
      Jf[j,5] = partialDerB6(B[0],B[1],B[2],B[3],B[4],B[5],X[j])

   Jft =  Jf.T
   B_copy = B
   B = B_copy + np.dot(np.dot( inv(np.dot(Jft,Jf)),Jft),r)
   plt.plot(approx, label="n = {0}".format(i))
   plt.plot(Y)
   
#On trace le graphique   
plt.plot(approx)
plt.plot(Y, label="Y real")
plt.title('Méthode de Gauss-Newton')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(shadow=True, fancybox=True)
plt.show()