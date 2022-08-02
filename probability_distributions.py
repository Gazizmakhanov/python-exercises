import pandas as pd
import numpy as np
from scipy import stats

num_of_cars=stats.poisson(2).pmf(0)
print(num_of_cars)

more_than_three=stats.poisson(2).sf(3)
print(more_than_three)

less_or_one=1-(stats.poisson(2).cdf(1))
print(less_or_one)

top_five=stats.norm(3.0, 0.3).isf(0.05)
print(top_five)

bottom_15=stats.norm(3.0, 0.3).cdf(.15)
print(bottom_15)

higher_than_40=stats.norm(3.0, 0.3).isf(.6)
print(higher_than_40)
less_than_30=stats.norm(3,.3).ppf(0.3)
