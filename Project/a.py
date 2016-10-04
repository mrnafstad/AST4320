#going to implement FFT to calculate the fourier conjugate of W. Need an iftest to check wether |x| < R, boom

import numpy as np
import matplotlib.pylab as mpl

R = 1.0 #or what?
N = 10000

def check(x_i):

	if abs(a) < R:
		return 1.0
	else:
		return 0.0

x = np.linspace(-2*R, 2*R, N)
W = np.zeros(N)
W_f = np.zeros(N)

for i in range(N);
	W[i] = check(x[i])

#main

for i in range(N):
	s = 0
	for j in range(N):
		#need to use imaginary shiet
		s += x[j]*np.exp(-2*np.pi*Im*j*i/N)
	W_f[i] = s