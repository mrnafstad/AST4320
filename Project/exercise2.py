import numpy as np
import matplotlib.pyplot as mpl

N = 1e5

sigmasqr = 1e-5
eps = 0.99
def newsig(Sc):
	return np.pi/Sc**4

Scs = np.zeros(N)
Scs[0] = np.pi/(sigmasqr)**(1./4)

delta = np.zeros(N)
mean = 0
delta[0] = np.random.normal(mean, sigmasqr)

for i in range(int(N)):

	Scs[i+1] = Scs[i]*eps
	sigmasqr = newsig(Scs[i+1])
	beta = np.random.normal(mean, abs(newsig(Scs[i]) - newsig(Scs[i+1])))
	delta[i+1] = delta[i] + beta

	if Scs[i] <= 1.0:
		break

mpl.plot(Scs, delta)
mpl.show()