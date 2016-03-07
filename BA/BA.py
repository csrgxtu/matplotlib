#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 07/Mar/2016
# File: BA.py
# Desc: draw ba graph
#
# Produced By CSRGXTU
import matplotlib.pyplot as plt

def BA(m, k):
    return (2 * m * (m + 1)) / (k * (k + 1) * (k + 2))

def ABA(m, k):
    return (2 * m * m * m) / (k * k * k)


X = [x / 50.0 for x in range(1, 101)]

# m = 1.0 k = 1.0
Y1 = [BA(1.0, x) for x in X]
YA1 = [ABA(1.0, x) for x in X]

print Y1

plt.plot(X, Y1, 'k*')
plt.plot(X, YA1, 'k')

plt.ylim(0, 100)
plt.xlabel('k')
plt.ylabel('P(k)')

plt.show()
