import pandas as pd
import numpy as np
import scipy.stats as st

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print(a[a<0])

print(a[a>0])

b=a[a>0]
print(b[b%2==0])

c=(a+3)
print(c)
print(len(c[c%2==0]))

mean1=a.mean()
std1=a.std()

print(mean1)
print(std1)

new_a=(a**2)
print(new_a)
mean2=new_a.mean()
std2=new_a.std()
print(mean1,mean2,std1,std2)

z_score=st.zscore(a)

print(z_score)




