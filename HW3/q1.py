import matplotlib.pyplot as plt
import numpy as np

#time
step = 0.001
t = np.arange(-3, 3.002, step)

#integrate
def integ(x, start, end):
    return np.sum(x) * step

#a(k)
def a(sig, k, T0):
    w0 = 2*np.pi/T0
    x = sig * np.cos(k*w0*t)
    return (2/T0) * integ(x, -T0/2, T0/2)

#b(k)
def b(sig, k, T0):
    w0 = 2*np.pi/T0
    x = sig * np.sin(k*w0*t)
    return (2/T0) * integ(x, -T0/2, T0/2)

#Fourier Series
def fs(sig, c, T0):
    w0 = 2*np.pi/T0
    y = np.zeros((len(t), ))
    y += a(sig, 0, T0)/2
    for k in range(1, c + 1):
        y += a(sig, k, T0)* np.cos(k*w0*t) + b(sig, k, T0) * np.sin(k*w0*t)
    return y

#sig1
x1 = np.zeros((len(t), ))
for idx, val in enumerate(t):
    if (1000 <= idx and idx < 2000) :
        x1[idx] = val + 2
    if (2000 <= idx and idx < 4000) :
        x1[idx] = -val
    if (4000 <= idx and idx < 5000) :
        x1[idx] = val - 2
fig, s1 = plt.subplots()
s1.plot(t, x1, 'r', label="x1(t)")
for c in range(0, 11):
    if(c % 2 ==0):
        color = 'g'
    else:
        color = 'b'
    s1.plot(t, fs(x1, c, 6), color, label = f'C = {c}')
s1.set(xlabel = 't', title = '(x1)')
s1.legend()
s1.grid()

#sig2
x2 = np.heaviside(-t, 1) + np.heaviside(t-3, 1)
fig, s2 = plt.subplots()
s2.plot(t, x2, 'r', label="x2(t)")
for c in range(0, 11):
    if(c % 2 ==0):
        color = 'g'
    else:
        color = 'b'
    s2.plot(t, fs(x2, c, 6), color, label = f'C = {c}')
s2.set(xlabel = 't', title = '(x2)')
s2.legend()
s2.grid()

plt.show()
