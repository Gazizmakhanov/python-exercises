# import numpy for all that good mathematic application
import numpy as np
# import pandas for all that good tabular manipulation
import pandas as pd
# get the data function from pydataset to grab some extra content
from pydataset import data
# grab the specific stuff from your env file (but dont print it out in your notebook!!)
import env
# from env import user, host, password (if ya like)

# set a random seed if you want things to be repeatable when you invoke np.random calls
np.random.seed(1349)
import os
os.path.exists('env.py')
myvar1, myvar2 = (1, 5)
myvar1
def get_db_url(db, env_file=os.path.exists('env.py')):
    '''
    returns a formatted string ready to utilize as a sql url connection
    
    args: db: a string literal representing a schema
    env_file: bool: checks to see if there is an env.py present in the cwd
    
    make sure that if you have an env file that you import it outside of the scope 
    of this function call, otherwise env.user wont mean anything ;)
    '''
    if env_file:
        user, password, host = (env.user, env.password, env.host)
        return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    else:
        return 'yo you need some credentials to access a database usually and I dont want you to type them here.'
# write a test query that doesnt pull a ton of data 
# (remember you can always do this in workbench to test!!)
query = '''SELECT * FROM employees limit 10'''
# read in data from employee
pd.read_sql(query, get_db_url('employees'))

# do it for realsies
url = get_db_url("employees")
sql = """
SELECT * FROM employees
"""

employees = pd.read_sql(sql, url)
employees.shape
# cache the data so that we can access this dataframe in the future without having
# to ping the cloud database every time:
employees.to_csv('employees.csv', index=False)
# loading it up in the future looks like:
# employees = pd.read_csv('employees.csv')
sql = """
SELECT * FROM titles

"""

titles = pd.read_sql(sql, url)
titles.head()
titles.shape
employees.describe()
titles.describe(include='all')
pd.read_sql("SELECT COUNT(DISTINCT title) AS unique_title_count from titles", url)
len(titles.title.unique())
len(titles['title'].value_counts())
titles['title'].nunique()
pd.read_sql("SELECT MIN(to_date) FROM titles", url)
pd.read_sql("SELECT MAX(to_date) FROM titles", url)

titles.to_date.max()
titles.to_date.min()
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles
right_join = pd.merge(users, 
                      roles, 
                      left_on='role_id', 
                      right_on='id', 
                      how='right',
                      indicator=True)
right_join
clean_right = pd.merge(users, 
                    roles, 
                    left_on='role_id', 
                    right_on='id', 
                    how='right').drop(columns='role_id').rename(columns={'id_x': 'id', 
                                                                         'name_x': 'employee',
                                                                         'id_y': 'role_id',
                                                                         'name_y': 'role'}
                                                                )
clean_right
pd.merge(users, 
         roles, 
         left_on='role_id', 
         right_on='id', 
         how='outer',
        indicator=True)

pd.merge(users, 
         roles, 
         left_on='role_id', 
         right_on='id', 
         how='outer').drop(columns='role_id').rename(columns={'id_x': 'id', 
                                                            'name_x': 'employee',
                                                            'id_y': 'role_id',
                                                            'name_y': 'role'}
data('mpg', show_doc=True)
mpg = data('mpg')
mpg.head()
mpg.shape
mpg.columns
mpg.columns.tolist()
list(mpg)
mpg.columns = ['manufacturer', 'model', 'displacement', 'year', 'cylinders', 'transmission', 'drive', 'city','highway', 'fuel', 'class']
mpg.manufacturer.nunique()
mpg.model.unique()
mpg.model.nunique()
mpg['mileage_difference'] = mpg.highway - mpg.city
mpg['average_mileage'] = round(2 / ((1/mpg.highway) + (1/mpg.city)), 2)
mpg.head()
mpg.transmission.unique()
mpg['is_automatic'] = mpg.transmission.str.contains('auto')

mpg.head()
mpg.groupby('manufacturer').average_mileage.mean().sort_values(ascending = False)
mpg.groupby('manufacturer').average_mileage.mean().nlargest(n = 1, keep = 'all')
mpg['transmission_category']= np.where(
    mpg.transmission.str.contains('auto'), 'automatic', 'manual')
mpg.head()
mpg.groupby('transmission_category')[['average_mileage']].mean().round(1)
query = '''
                     SELECT *
                     FROM orders;
                     '''
In [48]:
orders = pd.read_sql(query, get_db_url('chipotle'))
orders.head()
chipotle_sql_query = '''
                     SELECT *
                     FROM orders;
                     '''
orders = pd.read_sql(chipotle_sql_query, get_db_url('chipotle'))
orders.head()
orders.shape
orders.info()
orders['item_price'] = orders.item_price.str.replace('$', '').astype(float)
orders.info()
order_totals = orders.groupby('order_id').item_price.sum()
order_totals.sample(10)
top_three = orders.groupby('item_name').quantity.sum().sort_values(ascending=False).head(3)
top_three
top_three.plot(kind='barh',
             color='blueviolet', 
             ec='black', 
             width=.8)

plt.title('The Big Three at Chipotle')
plt.xlabel('Number of Items Ordered')
plt.ylabel('Menu Item')

# reorder y-axis of horizontal bar chart
plt.gca().invert_yaxis()

plt.show()
orders.sample(5)
orders.groupby('item_name').item_price.sum().nlargest(1)
orders.groupby('item_name').item_price.sum().nlargest(1)
orders.groupby('item_name').item_price.sum().sort_values(ascending=False).head(1)
employees.shape
titles.shape
all_emp_titles = employees.merge(titles, on='emp_no')
all_emp_titles.shape
all_emp_titles.head()
all_emp_titles.shape
all_emp_titles.info()
all_emp_titles.groupby('emp_no').title.count().value_counts()
all_emp_titles.groupby('title').hire_date.max()
x = pd.Series(['John', 'Madeleine', 'Ryan'])
x.max()
y = pd.Series(['1999-12-24', '1999-12-31'])
y.max()
dept_title_query = '''

                    SELECT t.emp_no, 
                    t.title, 
                    t.from_date, 
                    t.to_date, 
                    d.dept_name 
                    FROM departments AS d 
                    JOIN dept_emp AS de USING(dept_no) 
                    JOIN titles AS t USING(emp_no);

                    '''
dept_titles = pd.read_sql(dept_title_query, get_db_url('employees'))
dept_titles.head()
dept_titles.shape
all_titles_crosstab = pd.crosstab(dept_titles.dept_name, dept_titles.title)
all_titles_crosstab
current_titles = dept_titles[dept_titles.to_date == dept_titles.to_date.max()]
current_titles.head(1)
current_titles.shape
current_titles_crosstab = pd.crosstab(current_titles.dept_name, current_titles.title)
current_titles_crosstab
current_titles_crosstab.style.highlight_max(axis=1)                    

