from pydataset import data
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

iris = sns.load_dataset('iris')

iris2 = data('iris')

iris2.head()

iris.head()

iris.info()

iris.head(5)

iris.species.value_counts()

sns.displot(iris.petal_length, kde =True)

sns.relplot(data = iris, x = 'petal_length', y = 'petal_width', hue = 'species')

sns.relplot(data = iris, x = 'sepal_length', y = 'sepal_width', hue = 'species')

sns.boxplot(y = 'sepal_length', x = 'species', data = iris)

sns.pairplot(data = iris, hue = 'species')

df = sns.load_dataset('anscombe')

df.head(3)

df.info()

df.groupby('dataset').describe()

sns.relplot(data = df, x = 'x', y = 'y', col = 'dataset')

sns.lmplot(data = df, x = 'x', y = 'y', col = 'dataset')

InsectSprays = data('InsectSprays')
data('InsectSprays', show_doc = True)

InsectSprays.head()

plt.figure(figsize=(8, 6))
sns.boxplot(y = 'count', data = InsectSprays, x = 'spray')
plt.title('Comparing effectiveness of insect sprays')
plt.show()

swiss = data('swiss')
data('swiss', show_doc=True)

swiss.head()
swiss['is_catholic'] = swiss.Catholic > 50

swiss.head(2)

sns.boxplot(x = 'is_catholic', y = 'Fertility', data = swiss)

swiss.iloc[:, :-1]

sns.pairplot(data = swiss)

swiss.corr().Fertility

def get_db_url(db):
    from env import user, password, host
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

url = get_db_url('chipotle')
query = "SELECT * FROM orders"
orders = pd.read_sql(query, url)
orders.head()

orders.info()

orders['item_price'] = orders.item_price.str.replace('$', '').astype('float')

orders.head(6)

chicken_bowl = orders[orders.item_name == 'Chicken Bowl']
chicken_bowl.sort_values('quantity', ascending = False)

best_sellers = orders.groupby('item_name').quantity.sum().nlargest(4)
best_sellers

best_sellers.index

revenue = orders[orders.item_name.isin(best_sellers.index)].groupby('item_name').item_price.sum()
revenue

orders.groupby('item_name').item_price.sum().reset_index()

best_sellers.reset_index().merge(orders.groupby('item_name').item_price.sum().reset_index(), on='item_name')

revenue = revenue.sort_values(ascending = False).reset_index()
revenue


plt.figure(figsize = (8, 5))
sns.barplot(y = 'item_name', x = 'item_price', data = revenue)
plt.title('Most popular items and revenue')

plt.ylabel("") # to get remove the column_name
plt.xlabel("Gross Revenue")
plt.suptitle("Revenue from Top 4 selling Items")

sleepstudy = data('sleepstudy')
sleepstudy['Subject'] = 'Subject_' + sleepstudy.Subject.astype(str) 

plt.figure(figsize=(16, 9))

sns.lineplot(data = sleepstudy, x = 'Days', y = 'Reaction', hue = 'Subject', legend=False)
sns.lineplot(data = sleepstudy, x = 'Days', y = 'Reaction', color = 'black', linestyle='--', estimator = 'mean')
plt.annotate('Average',(0,265),fontsize=17)



