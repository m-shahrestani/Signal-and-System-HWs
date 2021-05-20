import matplotlib.pyplot as plt
import numpy as np

#time
t = np.arange(-3, 3, 0.001)

#sig1
y1 = np.exp(-3 * t)
fig, x1 = plt.subplots()
x1.plot(t, y1)
x1.set(xlabel = 't', ylabel = 'x1(t)', title = 'x1(t) = e^-3t')
x1.grid()

#sig2
y2 = y1 * np.heaviside(t, 1)
fig, x2 = plt.subplots()
x2.plot(t, y2)
x2.set(xlabel = 't', ylabel = 'x2(t)', title = 'x2(t) = e^-3t*u(t)')
x2.grid()

#sig3
y3 = y2 + 2*np.sin(t+2)
fig, x3 = plt.subplots()
x3.plot(t, y3)
x3.set(xlabel = 't', ylabel = 'x3(t)', title = 'x3(t) = e^-3t*u(t) + 2sin(t+2)')
x3.grid()

#sig4
y4 = np.exp(-t)*(np.sin(t)+np.cos(t)) * np.heaviside(t, 1)
for idx, val in enumerate(y4):
    if (-2000 <= idx and idx <= 4000) :
        y4[idx] = 1
    if idx < 2000 :
        y4[idx] = 0
fig, x4 = plt.subplots()
x4.plot(t, y4)
x4.set(xlabel = 't', ylabel = 'x4(t)', title = 'x4(t)')
x4.grid()

plt.show()
