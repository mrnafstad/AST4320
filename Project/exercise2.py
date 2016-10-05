import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
plt.rc('text', usetex=True)
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18

#Number of steps
N = 100000

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
	
	Sc = (np.pi/sigmasqr)**(1./4)
	delta = np.random.normal(0, sigmasqr)
	deltas = np.zeros(N)

	i=0
	while Sc>=1:
		Scnew = Sc*eps
		beta = np.random.normal(0, newsig(Scnew) - newsig(Sc))
		delta += beta
		
		if delta > 1.0:
			crossing = True

		deltas[i] = delta

		Sc = Scnew	
		i += 1
	return delta, crossing

P = np.zeros(N)
Pcr = np.zeros(N)
deltafinal = np.zeros(N)
deltabelowcrit = []
for i in range(int(N)):	
	deltafinal[i], cross = main()
	if cross == False:
		deltabelowcrit.append(deltafinal[i])
		

delta = np.linspace(min(deltafinal), max(deltafinal), N)
delt = np.linspace(min(deltafinal),max(deltafinal), N)
for i in range(N):
	P[i]=1/(np.sqrt(2)*np.pi)*np.exp(-delta[i]**2/(2*np.sqrt(np.pi)))
	Pcr[i]=1/(np.sqrt(2)*np.pi)*(np.exp(-delt[i]**2/(2*np.sqrt(np.pi))) - np.exp(-(2 -delt[i])**2/(2*np.sqrt(np.pi))))

deltabelowcrit = np.array(deltabelowcrit)


plt.title(r"Histogram of $\delta$")

plt.hist(deltafinal, bins=100, normed=True)
plt.plot(delta, P)
plt.show()

plt.title(r"Histogram of $\delta < \delta_{crit}$")
plt.hist(deltabelowcrit, bins = 100, normed = True)
plt.plot(delt, Pcr)
plt.show()
