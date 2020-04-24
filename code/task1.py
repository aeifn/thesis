#!/usr/bin/env python3
import numpy, math
import matplotlib.pyplot as plt
from scipy.special import binom
from sys import argv


N=int(argv[1])
M=int(argv[2])

t=1
tau=2
T=3

Qs=(T-tau)/(T-t)

def calc(p):
  answer = 0
  for i in range(N):
    b = binom(N,i)
    p_1=p**i
    p_2=(1-p)**(N-i)
    if i>=M:
      k_1=M/(i+1)
    else:
      k_1=1
    answer = answer + b*p_1*p_2*k_1
  return answer

plt_x=[]
plt_y=[]
for i in numpy.arange(0,1,.01):
  x=i
  y=calc(i)
  plt.scatter(x,y)

plt.title("M="+str(M)+", N="+str(N))
plt.show()
