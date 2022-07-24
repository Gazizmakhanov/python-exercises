# import pandas as pd
# In [3]:
# fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# type(fruits)
# len(fruits)
# fruits.index

# fruits.values

# fruits.dtypes
# fruits.head()

# fruits.tail(3)
# fruits.sample(2)
# fruits.describe()

# fruits.unique()

# fruits.value_counts()
# fruits.value_counts().head(1)

# fruits.value_counts().nlargest(1)
# fruits.value_counts().tail()
# fruits.value_counts().nsmallest(keep='all')

# fruits.str.capitalize()
# fruits.str.count('a')
# fruits.str.count('[aeiou]')

# word = 'strawberry'
# In [60]:
# def count_vowels(word):
#     count = 0 

#     for char in word:
#         if char in 'aeiou':
#             count += 1

#     return count
# count_vowels('helloworld')
# count_vowels('thisisanothertest')
# fruits.apply(count_vowels)

# fruits [fruits.str.len().idxmax()]
# fruits [fruits.str.len() >= 5]
# fruits [fruits.str.count('o') >= 2]
# fruits [fruits.str.contains('berry')]
# fruits [fruits.str.contains('apple')]
# fruits [fruits.str.count('[aeiou]').idxmax()]
# letters = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')

# type(letters)
# letters = pd.Series(letters)
# letters.value_counts()
# letters.value_counts().nsmallest(1).index

# letters.apply(count_vowels).sum()
# len(letters) - letters.apply(count_vowels).sum()
# letters.str.upper()

# letters.value_counts().head(6)

# letters.value_counts().head(6).plot.bar()

# numbers = numbers.str.strip('$').str.replace(',','').astype(float)
# numbers
# numbers.max()

# numbers.min()
# numbers.max() - numbers.min()
# pd.cut(numbers, 4).value_counts()
# pd.cut(numbers, 4).value_counts().sort_index().plot.bar(title='our numbers in 4 bins').set(xlabel='bins', ylabel='count')
# exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
# exam_scores
# len(exam_scores)
# exam_scores.describe()
# exam_scores.median()
# exam_scores.mode()
# exam_scores.plot.hist(title='distribution of exam scores').set(xlabel='exam scores', ylabel='frequency')
# Out[178]:

# curved_grades = (100 - exam_scores.max()) + exam_scores
# curved_grades
# Out[185]:

# letter_grades = pd.cut(curved_grades, bins=[0,60,70,80,90,100], labels=['F','D','C','B','A'])
# letter_grades
# letter_grades.value_counts().sort_index(ascending=False).plot.bar(title='letter grade distribution').set(xlabel='letter grades', ylabel='count')


from turtle import title
import pandas as pd
import numpy as np

fruits=pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
)
print(fruits)
element_length=len(fruits)
print(element_length)

fruit_indexes=fruits.index
print(fruit_indexes)

fruit_values=fruits.values
print(fruit_values)

data_type=fruits.dtype
print(data_type)

first_five=fruits.head(5)
print(first_five)

last_three=fruits.tail(3)
print(last_three)

random_value=fruits.sample(1)
print(random_value)

describe_fruits=fruits.describe()
print(describe_fruits)

value_count=fruits.value_counts()
print(value_count)

most_occured=value_count.head(1)
print(most_occured)

least_occured=value_count.tail(1)
print(least_occured)

capitalized=fruits.str.capitalize()
print(capitalized)

num_a=sum(fruits.str.count('a'))
print(num_a)

num_vowels=sum(fruits.str.count('[aeiou]'))
print(num_vowels)

total_num=sum(fruits.str.len())
print(total_num)

cont_num=total_num-num_vowels

print(cont_num)

letters=pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
))
print(letters)
most_seen=(letters.value_counts().head(1))
print(most_seen)

least_seen=(letters.value_counts().tail(1))
print(least_seen)

vowel_num=sum(letters.str.count('[aeiou]'))
print(vowel_num)


def c_counter(a):
    cont_count=0
    for i in letters:
        if i not in 'aeiou':
            cont_count+=1
    return cont_count

print(c_counter(letters))

uppercase=letters.str.upper()
print(uppercase)

top_six=letters.value_counts().head(6)
print(top_six)

the_bar=top_six.plot.bar()
print(the_bar)

numbers=pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
print(numbers)

num_element=len(numbers)
print(num_element)

numbers=numbers.str.replace('$','').str.replace(',','').astype(float)
print(numbers)

max_value=max(numbers)
print(max_value)

min_value=min(numbers)
print(min_value)

num_range=max_value-min_value
print(num_range)

my_bins=pd.cut(numbers, 4)
print(my_bins.value_counts())

my_plot=my_bins.value_counts().plot(title='my_plot').set(xlabel='x', ylabel='y')
print(my_plot)

exam_scores=pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
)
num_of_elem1=len(exam_scores)
print(num_of_elem1)

my_mean=exam_scores.mean()
my_median=exam_scores.median()
ex_max=max(exam_scores)
ex_min=min(exam_scores)
print(my_mean,my_median,ex_max,ex_min)

exam_plot=exam_scores.plot(title='exam_score').set(xlabel='name',ylabel='score')
print(exam_plot)

curved_grades=exam_scores+(100-max(exam_scores))
print(curved_grades)

grades=pd.cut(curved_grades, bins=[0,60,70,80,90,100], label=['F', 'D', 'C', 'B', 'A'])

curved_plot=grades.value_counts().plot().bar(title='exam_grades',).set(xlabel='grade', ylabel='score')
print(curved_grades)
