import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
plt.rc('text', usetex=True)
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18


#Sigma^2
def newsig(Sc):
	return np.pi/Sc**4

def main():

	#Initial sigma
	sigmasqr = 5e-5

	#Boolian parameter to check wether we cross the critical density
	crossing = False

	Sc = (np.pi/sigmasqr)**(1./4.)
	delta = np.random.normal(loc=0.0, scale=np.sqrt(sigmasqr))
	while Sc>=1:
		Scnew = Sc*eps
		beta = np.random.normal(loc=0.0, scale=np.sqrt(newsig(Scnew)-newsig(Sc)))
		delta += beta
		Sc = Scnew	

		if delta > 1.0:
			crossing = True

	return delta, crossing


#Number of steps
N = 100000

#Change factor
eps = 0.99

#-----------Numerical solution-------------
delta_last_element = np.zeros(N)
delta_below_crit = []
for i in range(int(N)):	
	delta_last_element[i], cross = main()

	#Saving elements that cross critical delta
	if cross == False:
		delta_below_crit.append(delta_last_element[i])
		
delta_below_crit = np.array(delta_below_crit)

#-----------Exact Solution-------------
# for all elements
Sc=1
delta_analytic = np.linspace(min(delta_last_element),max(delta_last_element),N)
P=1.0/np.sqrt(2.0*np.pi*newsig(Sc))*np.exp(-delta_analytic**2/(2.0*newsig(Sc)))

plt.title(r"Histogram of $\delta$")
plt.hist(delta_last_element, bins=100, normed=True)
plt.plot(delta_analytic, P,'-o')
plt.grid('on')
plt.xlabel(r'$\delta$', size=18)
plt.legend(['analytical','Numerical Histogram'])
plt.savefig('lastdeltahist')
plt.show()

# For elements crossing critical delta
N=len(delta_below_crit)
delta_analytic = np.linspace(min(delta_below_crit),max(delta_below_crit),N)

Pnc = 1.0/np.sqrt(2.0*np.pi*newsig(Sc))*(np.exp(-delta_analytic**2/(2.0*newsig(Sc)))-np.exp(-(2.0 - delta_analytic)**2/(2*newsig(Sc))))

#Normalizing
normPnc = Pnc*2.


plt.hist(delta_below_crit, bins = 100, normed = True)
plt.plot(delta_analytic, normPnc,'-o')
plt.grid('on')
plt.xlabel(r'$\delta$', size=18)
plt.legend(['analytical','Numerical Histogram'])
plt.title(r"Histogram of $\delta < \delta_{crit}$")
plt.savefig('belowcrithist')
plt.show()

