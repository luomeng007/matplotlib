# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/1912:21
software: PyCharm

Description:
    points:磅
"""
import matplotlib.pyplot as plt

# we know that numpy module is contained in matplotlib
x = plt.np.linspace(-4, 4, 200)
f1 = plt.np.power(10, x)
# e function is also contained in numpy module
f2 = plt.np.power(plt.np.e, x)
f3 = plt.np.power(2, x)

plt.plot(x, f1, 'r', x, f2, 'b', x, f3, 'g', linewidth=2)
plt.axis([-4, 4, -0.5, 8])
plt.text(1, 7.5, r'$10^x$', size=16)
plt.text(2.2, 7.5, r'$e^x$', size=16)
plt.text(3.2, 7.5, r'$2^x$', size=16)
plt.title('A simple example', size=16)

plt.show()
