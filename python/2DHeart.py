# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pdb

fig, ax = plt.subplots()

x=np.linspace(-10,10,1000)
y=np.linspace(-10,10,1000)

X,Y = np.meshgrid(x,y)

pdb.set_trace()
Z=X**2 +(Y-1.5*X**(2/3))**2-1

ax.contour(-1*X,Y,Z,[1,5,10,15,20,25,30])
ax.contour(X,Y,Z,[1,5,10,15,20,25,30])

ax.text(-0.3,-6.5,r'$\dag$',color='r',alpha=0.8,fontsize=25)

ax.text(-7.5,-8.5,r'$\ell$',fontsize=20,color='r')

ax.text(-5.5,-8.5,r'$x^2+y^2=1$',fontsize=20,color='g')

ax.text(0.8,-8.5,r'$|x|$',fontsize=20,color='b')

ax.text(3.5,-8.5,r'$\lim_{n \to \infty}(1+\frac{1}{n})^n$',
        fontsize=20,color='c')

ax.set_title(r'$x^2 + (y -\sqrt[3]{x^2})^2 = 1$')

ax.set_xlabel(r'$i$',fontsize=20)

ax.set_ylabel(r'$u$',fontsize=20,rotation=0)