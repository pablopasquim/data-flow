from matplotlib import *
from pylab import *
from numpy import *
from scipy import *
from scipy import stats

# --- Code English ---

X = stats.poisson(3.5)

n = arange(0,15)
fig, axes = subplots(3,1, sharex=True)

axes[0].step(n, X.pmf(n))

axes[1].step(n, X.cdf(n))

axes[2].hist(X.rvs(size=1000));

show()

# Create a (continous) random variable with normal distribution
y = stats.norm()
x = linspace( -


              5,5,100)
fig, axes = subplots(3,1, sharex=True)
# plot the probability distribution function (PDF)
axes[0].plot(x, y.pdf(x))
# plot the commulative distribution function (PDF)
axes[1].plot(x, y.cdf(x));
# plot histogram of 1000 random realizations of the stochastic variable Y
axes[2].hist(y.rvs(size=1000), bins =50);

show()

x.mean(), x.std(), x.var()
y.mean(), y.std(), x.var()

t_statistic, p_value = stats.ttest_ind(X.rvs(size=1000), X.rvs(size=1000))
print("t-statistic =", t_statistic)
print("p-value", p_value)


