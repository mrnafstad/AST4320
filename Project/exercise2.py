import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
plt.rc('text', usetex=True)
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18

#Number of steps
N = 10000

#Change factor
eps = 0.9


#Sigma^2
def newsig(Sc):
	return np.pi/Sc**4

def main():

	#Initial sigma
	sigmasqr = 5e-5

	#Boolian parameter to check wether we cross the critical density
	crossing = False

	#Array with P
	P = np.zeros(N)

	i=0
	Sc = (np.pi/sigmasqr)**(1./4)
	Scs = np.zeros(N)
	delta = np.random.normal(0, sigmasqr)
	deltas = np.zeros(N)

	while Sc>=1:
		Scnew = Sc*eps
		beta = np.random.normal(0, newsig(Scnew) - newsig(Sc))
		delta += beta

		#Analytical solution 
		P[i]=1/(np.sqrt(2*np.pi*newsig(Sc)))*np.exp(-delta**2/(2*newsig(Sc)))
		if abs(delta) > 1.0:
			crossing = True

		Scs[i] = Sc
		deltas[i] = delta

		Sc = Scnew	
		i += 1
	
	return deltas[i-1], Scs, P, crossing


deltafinal = np.zeros(N)
deltabelowcrit = np.zeros(N)
for i in range(int(N)):	
	deltafinal[i], Scs, P, cross = main()
	if cross == False:
		deltabelowcrit[i] = deltafinal[i]
	
plt.title(r"Histogram of $\delta$")
plt.hist(deltafinal, bins=20)
#plt.plot(Scs, P)
plt.show()

plt.title(r"Histogram of $\delta < \delta_{crit}")
plt.hist(deltabelowcrit, bins = 20)
plt.show()