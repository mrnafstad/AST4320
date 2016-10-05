import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
plt.rc('text', usetex=True)
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18

#Number of steps
N = 1e5

#Change factor
eps = 0.99

#array with final deltas
deltafinal = np.zeros(N)

#Sigma^2
def newsig(Sc):
	return np.pi/Sc**4

def main():

	#Initial sigma
	sigmasqr = 5e-5

	#Array with Sc
	Scs = np.zeros(N)
	Scs[0] = (np.pi/sigmasqr)**(1./4)

	mean = 0
	#Array with deltas	
	delta = np.zeros(N)
	delta[0] = np.random.normal(mean, sigmasqr)

	#Array with P
	P = np.zeros(N)

	for i in range(int(N)):

		Scs[i+1] = Scs[i]*eps
		sigmasqr = newsig(Scs[i+1])
		beta = np.random.normal(mean, abs(newsig(Scs[i]) - newsig(Scs[i+1])))
		delta[i+1] = delta[i] + beta

		#Analytical solution 
		P[i]=1/(np.sqrt(2*np.pi*newsig(Scs[i])))*np.exp(-delta[i]**2/(2*newsig(Scs[i])))

		#Break if Sc = 1
		if Scs[i] <= 1.0:
			break
	"""
	plt.title("Random walk")	
	plt.plot(Scs, delta)
	plt.show()
	"""
	return delta[-1]

for i in range(int(N)):
	deltafinal[i] = main()

plt.title(r"Histogram of $\delta$")
plt.hist(deltafinal)
plt.plot(Scs, P)
plt.show()


