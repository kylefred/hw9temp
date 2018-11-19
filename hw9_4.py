import sys
import scipy.stats

mu = float(sys.argv[1])
sd = float(sys.argv[2])
x = float(sys.argv[3])

print("PDF:",scipy.stats.norm.pdf(x, mu, sd))
print("CDF:",scipy.stats.norm.cdf(x, mu, sd))

