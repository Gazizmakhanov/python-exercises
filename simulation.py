

from xxlimited import foo
import numpy as np
import pandas as pd
import itertools as it

# dice1=[1,2,3,4,5,6]
# dice2=[1,2,3,4,5,6]
# outcomes=list(it.product(dice1, dice2))
# num_tries=10_000
# rolls=np.random.choice(outcomes, num_tries)
# print(rolls)


dice1=np.random.choice([1,2,3,4,5,6], size=10_000)
dice2=np.random.choice([1,2,3,4,5,6], size=10_000)

num_of_tries=(dice1==dice2).sum()
print(dice1)
print(dice2)
print((num_of_tries)/len(dice2))

num_of_tries1=10_000
num_of_coins=8

tosses=np.random.choice(['T', 'H'], num_of_tries1*num_of_coins).reshape(num_of_tries1, num_of_coins)
print(tosses)
print(((tosses=='H').sum(axis=1)==3).sum()/len(tosses))


num_of_trials=10_000
num_of_bilboards=2
student=np.random.choice(['DS', 'WD', 'WD', 'WD'], num_of_trials*num_of_bilboards).reshape(num_of_trials, num_of_bilboards)
print(student)
print(((student=='DS').sum(axis=1)==2).sum()/len(student))


num_of_package=np.random.normal(3, 1.5, 10_000).reshape(2000, 5)
print(((num_of_package).sum(axis=1)<17).sum()/len(num_of_package))

women=np.random.normal(170, 6, 10_000)
men=np.random.normal(178, 8, 10_000)
women_higher=(women>men).sum()
print(women_higher/len(women))


num_fails=np.random.choice(['F', 'S'], 50_000, p=[1/250, 249/250]).reshape(1000,50)

print(((num_fails=='F').sum(axis=1)==0).sum()/len(num_fails))

food_truck=np.random.choice([1, 0], 3000, p=[0.7, 0.3]).reshape(1000,3)
print((food_truck.sum(axis=1)==0).sum()/len(food_truck))

birth_date=np.random.choice(365, 230000).reshape(10000,23)
birth_date=pd.DataFrame(birth_date)
print((birth_date.nunique(axis=1)<23).sum()/len(birth_date))



# heads1=0
# for i in tosses:
#     if tosses[i].str.value_counts()['H']>3:
#         heads1+=1