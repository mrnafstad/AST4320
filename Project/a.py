#going to implement FFT to calculate the fourier conjugate of W. Need an iftest to check wether |x| < R, boom

import numpy as np
import matplotlib.pyplot as mpl

#mpl.rc('font', **{'family': 'serif', ['Computer Modern']})
#mpl.rc('text', usetex=True)
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18

R = 1.0 #or what?
N = 1000

def check(x_i):

	if abs(x_i) < R:
		return 1.0
	else:
		return 0.0

x = np.linspace(-50*R, 50*R, N)
W = np.zeros(N)
W_f = np.zeros(N)
k = x

for i in range(N):
	W[i] = check(x[i])

#main

x_f = np.fft.fft(x)
W_f = np.sin(2.0*R*k)/(2.0*np.pi*k) 

k = np.max(W_f)
r1 = np.argmin(np.abs(W_f[:N/2.]-0.5*k))
r2 = np.argmin(np.abs(W_f[N/2.:]-0.5*k))

mpl.plot(x, W_f)
mpl.axvspan(r1, r2, facecolor='g', alpha=0.5)
mpl.show()