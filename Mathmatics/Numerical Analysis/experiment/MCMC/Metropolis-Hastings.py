'''
Date:20160703
@author: zhaozhiyong
'''
import random
import math
from scipy.stats import norm
import matplotlib.pyplot as plt

def bivexp(theta1, theta2):
    lam1 = 0.5
    lam2 = 0.1
    lam = 0.01
    maxval = 8
    y = math.exp(-(lam1 + lam) * theta1 - (lam2 + lam) * theta2 - lam * maxval)
    return y

T = 5000
sigma = 1
thetamin = 0
thetamax = 8
theta_1 = [0.0] * (T + 1)
theta_2 = [0.0] * (T + 1)
theta_1[0] = random.uniform(thetamin, thetamax)
theta_2[0] = random.uniform(thetamin, thetamax)

t = 0
while t < T:
    t = t + 1
    theta_star_0 = random.uniform(thetamin, thetamax)
    theta_star_1 = random.uniform(thetamin, thetamax)
    # print theta_star
    alpha = min(1, (bivexp(theta_star_0, theta_star_1) / bivexp(theta_1[t - 1], theta_2[t - 1])))

    u = random.uniform(0, 1)
    if u <= alpha:
        theta_1[t] = theta_star_0
        theta_2[t] = theta_star_1
    else:
        theta_1[t] = theta_1[t - 1]
        theta_2[t] = theta_2[t - 1]
plt.figure(1)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
plt.ylim(thetamin, thetamax)
plt.sca(ax1)
plt.plot(range(T + 1), theta_1, 'g-', label="0")
plt.sca(ax2)
plt.plot(range(T + 1), theta_2, 'r-', label="1")
plt.show()

plt.figure(2)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
num_bins = 50
plt.sca(ax1)
plt.hist(theta_1, num_bins, normed=1, facecolor='green', alpha=0.5)
plt.title('Histogram')
plt.sca(ax2)
plt.hist(theta_2, num_bins, normed=1, facecolor='red', alpha=0.5)
plt.title('Histogram')
plt.show()