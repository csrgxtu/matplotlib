#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: coordinates.py
# Date: 14/Mar/2016
# Desc: generate coordinates
#
# Produced By CSRGXTU
import matplotlib.pyplot as plt

def func(x):
  return (0.167 * 0.167 - 0.167 * 0.167 * x) / (2 * x * x)

def run():
  X = [x/10.0 for x in range(1, 11, 1)]
  Y = []

  for x in X:
    Y.append(func(x))

  # print X
  # print Y
  plt.plot(X, Y)
  plt.show()

if __name__ == '__main__':
  run()