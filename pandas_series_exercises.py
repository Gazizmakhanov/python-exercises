import pandas as pd
In [3]:
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

type(fruits)
len(fruits)
fruits.index

fruits.values

fruits.dtypes
fruits.head()

fruits.tail(3)
fruits.sample(2)
fruits.describe()

fruits.unique()

fruits.value_counts()
fruits.value_counts().head(1)

fruits.value_counts().nlargest(1)
fruits.value_counts().tail()
fruits.value_counts().nsmallest(keep='all')

fruits.str.capitalize()
fruits.str.count('a')
fruits.str.count('[aeiou]')

word = 'strawberry'
In [60]:
def count_vowels(word):
    count = 0 

    for char in word:
        if char in 'aeiou':
            count += 1

    return count
count_vowels('helloworld')
count_vowels('thisisanothertest')
fruits.apply(count_vowels)

fruits [fruits.str.len().idxmax()]
fruits [fruits.str.len() >= 5]
fruits [fruits.str.count('o') >= 2]
fruits [fruits.str.contains('berry')]
fruits [fruits.str.contains('apple')]
fruits [fruits.str.count('[aeiou]').idxmax()]
letters = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')

type(letters)
letters = pd.Series(letters)
letters.value_counts()
letters.value_counts().nsmallest(1).index

letters.apply(count_vowels).sum()
len(letters) - letters.apply(count_vowels).sum()
letters.str.upper()

letters.value_counts().head(6)

letters.value_counts().head(6).plot.bar()

numbers = numbers.str.strip('$').str.replace(',','').astype(float)
numbers
numbers.max()

numbers.min()
numbers.max() - numbers.min()
pd.cut(numbers, 4).value_counts()
pd.cut(numbers, 4).value_counts().sort_index().plot.bar(title='our numbers in 4 bins').set(xlabel='bins', ylabel='count')
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
exam_scores
len(exam_scores)
exam_scores.describe()
exam_scores.median()
exam_scores.mode()
exam_scores.plot.hist(title='distribution of exam scores').set(xlabel='exam scores', ylabel='frequency')
Out[178]:

curved_grades = (100 - exam_scores.max()) + exam_scores
curved_grades
Out[185]:

letter_grades = pd.cut(curved_grades, bins=[0,60,70,80,90,100], labels=['F','D','C','B','A'])
letter_grades
letter_grades.value_counts().sort_index(ascending=False).plot.bar(title='letter grade distribution').set(xlabel='letter grades', ylabel='count')


