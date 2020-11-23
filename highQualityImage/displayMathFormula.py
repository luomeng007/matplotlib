# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/1912:21
software: PyCharm

Description:
"""
import matplotlib.pyplot as plt


def f(x, c):
    m1 = plt.np.sin(2 * plt.np.pi * x)
    m2 = plt.np.exp(-c * x)
    return plt.np.multiply(m1, m2)


x = plt.np.linspace(0, 4, 100)
sigma = 0.5
# two kind of method to use science mode
# plt.style.use(['science', 'no-latex'])
with plt.style.context(['science', 'no-latex']):
    plt.plot(x, f(x, sigma), 'r', linewidth=2)
    plt.xlabel(r'$\rm{time}  \  t$', fontsize=16)
    plt.ylabel(r'$\rm{Amplitude} \ f(x)$', fontsize=16)
    plt.title(r'$f(x) \ \rm{is \ damping  \ with} \ x$', fontsize=16)
    plt.text(2.0, 0.5, r'$f(x) = \rm{sin}(2 \pi  x^2) e^{\sigma x}$', fontsize=20)

plt.show()
