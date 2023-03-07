import numpy as np
from scipy.stats import *

mean1, mean2 = 225, 265
std1, std2 = 100, 75
nobs1, nobs2 = 30, 40

res = ttest_ind_from_stats(mean1=mean1, std1=std1, nobs1=nobs1, mean2=mean2, std2=std2, nobs2=nobs2, equal_var=False, alternative='less')
print(res)

