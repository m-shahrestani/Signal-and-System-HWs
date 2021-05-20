import matplotlib.pyplot as plt
import numpy as np

#time
t = np.arange(-10, 10, 0.1)
n = np.arange(-5, 11, 1)

#Convolution function
def conv(x, h):
    x = np.concatenate([np.zeros((len(h)-1,)) , x , np.zeros((len(h)-1,))])
    h = h[::-1]
    step = len(h)
    y = np.zeros((len(x) - step +1,))
    for i in range(len(y)):
        y[i] = (np.sum(x[i:i+step]*h))
    return y

#sig1
xa = 1/2*np.exp(-2 * t)*np.heaviside(t, 1)
ha = np.heaviside(t, 1) - np.heaviside(t - 5, 1)
y1 = conv(xa, ha)
y1 = y1[int(len(y1)/4) : -1 * int(len(y1)/4) -1]
fig, s1 = plt.subplots()
s1.plot(t, xa, 'b', label="x(t) = 1/2 e^(-2t) u(t)")
s1.plot(t, ha, 'g', label="h(t) = u(t)-u(t-5)")
s1.plot(t, y1, 'r', label="y(t) = x(t)*h(t)")
s1.set(xlabel = 't', title = '(a)')
s1.legend()
s1.grid()

#sig2
xb = np.power(1/3, -n)*np.heaviside(-n-1, 1)
hb = np.heaviside(n-1, 1)
y2 = conv(xb, hb)
y2 = y2[int(len(y2)/4) : -1 * int(len(y2)/4) -1]
fig, s2 = plt.subplots()
s2.stem(n, xb, 'b', markerfmt='bo', label="x[n] = (1/3)^(-n) u[-n-1]")
s2.stem(n, hb, 'g', markerfmt='go', label="h[n] = u[n-1]")
s2.stem(n, y2, 'r', markerfmt='ro', label="y(t) = x(t)*h(t)")
s2.set(xlabel = 'n', title = '(b)')
s2.legend()
s2.grid()

#sig3
xc = np.heaviside(n, 1) - np.heaviside(n-3, 1) + np.heaviside(n-5, 1) - np.heaviside(n-8, 1)
hc = np.power(1/3, n)*np.heaviside(n, 1)
y3 = conv(xc, hc)
y3 = y3[int(len(y3)/4) : -1 * int(len(y3)/4) -1]
fig, s3 = plt.subplots()
s3.stem(n, xc, 'b', markerfmt='bo', label="x[n]")
s3.stem(n, hc, 'g', markerfmt='go', label="h[n]")
s3.stem(n, y3, 'r', markerfmt='ro', label="y(t) = x(t)*h(t)")
s3.set(xlabel = 'n', title = '(c)')
s3.grid()
s3.legend()

plt.show()
