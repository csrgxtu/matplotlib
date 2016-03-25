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

def funca(gamma, x):
  return (gamma * gamma - gamma * gamma * x) / (2 * x * x)

def run():
  X = [x/100.0 for x in range(10, 101, 1)]
  Y = []

  for x in X:
    # Y.append(func(x))
    Y.append(funca(0.125, x))

  print X
  print Y
  # plt.figure(figsize=(8,6), dpi=80)
  plt.plot(X, Y)
  plt.xlabel(r'$\gamma$', fontsize=20)
  plt.ylabel('p', fontsize=20)
  plt.savefig('./coordinates.eps', format='eps')
  plt.savefig('./coordinates.png')
  plt.show()

if __name__ == '__main__':
  run()
