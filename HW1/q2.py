import matplotlib.pyplot as plt
import numpy as np

#time
n = np.arange(-20, 20, 1)

#sig1
y1 = np.heaviside(n, 1) - np.heaviside(n - 3, 1) + np.heaviside(n - 5, 1)
fig, x1 = plt.subplots()
x1.stem(n, y1)
x1.set(xlabel = 'n', ylabel = 'x1[n]', title = 'x1[n] = u[n] - u[n-3] + u[n-5]')
x1.grid()

#sig2
y21 = 2*np.cos(2*np.pi*1*n)
y22 = 2*np.cos(2*np.pi*2*n)
y23 = 2*np.cos(2*np.pi*3*n)
fig, x2 = plt.subplots()
x2.stem(n, y21, 'b', markerfmt='bo', label="2cos(2πn)")
x2.stem(n, y22, 'r', markerfmt='ro', label="2cos(4πn)")
x2.stem(n, y23, 'g', markerfmt='go', label="2cos(6πn)")
x2.set(xlabel = 'n', ylabel = 'x2[n]', title = 'x2[n] = 2cos(2πkn) ;(k=1, 2, 3)')
x2.grid()
x2.legend()

#sig3
y31 = 2*np.cos(2*1*n)
y32 = 2*np.cos(2*2*n)
y33 = 2*np.cos(2*3*n)
fig, x3 = plt.subplots()
x3.stem(n, y31, 'b', markerfmt='bo', label="2cos(2n)")
x3.stem(n, y32, 'r', markerfmt='ro', label="2cos(4n)")
x3.stem(n, y33, 'g', markerfmt='go', label="2cos(6n)")
x3.set(xlabel = 'n', ylabel = 'x3[n]', title = 'x3[n] = 2cos(2kn) ;(k=1, 2, 3)')
x3.grid()
x3.legend()

plt.show()
