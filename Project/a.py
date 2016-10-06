#going to implement FFT to calculate the fourier conjugate of W. Need an iftest to check wether |x| < R, boom

import numpy as np
import matplotlib.pyplot as mpl
from scipy.interpolate import UnivariateSpline

mpl.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
mpl.rc('text', usetex=True)
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18

R = 1.0 #or what?
N = 1000

def check(x_i):

	if abs(x_i) < R:
		return 1.0
	else:
		return 0.0

x = np.linspace(-15*R, 15*R, N)
W = np.zeros(N)
W_f = np.zeros(N)
k = x

for i in range(N):
	W[i] = check(x[i])

#main

W_f = np.sin(2.0*R*k)/(2.0*np.pi*k) 

spline = UnivariateSpline(x, W_f-max(W_f)/2, s=0)
r1, r2 = spline.roots() # find the roots

mpl.title(r'$\tilde{W}(k)$ with FWHM marked', size=18)
mpl.plot(x, W_f)
mpl.axvspan(r1,r2, facecolor='g', alpha=0.5)
mpl.grid('on')
mpl.ylabel(r'$\tilde{W}_f$', size=18)
mpl.xlabel(r'$k$', size=18)
mpl.savefig('wk')
mpl.show()
