from re import A, T


def is_two(x):
    if x==2:
        y=True
    elif str(x).isdigit()==False:
        y=False
    elif int(x)==2:
        y=True
    else:
        y=False
    return print(y)

# # Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(x):
    voewls=['a', 'e', 'i', 'o', 'u']
    if x in voewls:
        y=True
    else:
        y=False
    return print(y)


# # Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_constant(x):
    voewls=['a', 'e', 'i', 'o', 'u']
    if len(str(x))==1 and x in voewls:
        y=False
    else:
        y=True
    return y


# # Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_fisrt_letter(x):
    voewls=['a', 'e', 'i', 'o', 'u']
    if type(x)==str and len(str(x))>=2 and x[0] not in voewls:
       y=x.capitalize()
    elif type(x)!=str:
        y="Please enter a string"
    else:
        y='Your word does not start with consonant'
    return y

# print(cap_fisrt_letter(688787))

#Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(a, b):
    tip=a*b

    return f'Your tip amount is {tip}'



def apply_discount(the_price, discount):
    x=the_price-the_price*discount/100
    return f'Your discounted price is {x}'



def handle_commas(str1):
    if (type(str1)==str) and  (',' in str1):
        str1=str1.replace(',','')
    else:
        print('Your string does not contain a number')
    if(str1).isdigit()==True:
        str1=int(str1)
        return str1


def get_letter_grade(x):
    if x<=100 and x>=90:
        grade="A"
    elif x<=89 and x>=80:
        grade="B"
    elif x<=79 and x>=70:
        grade="C"
    elif x<=69 and x>=60:
        grade="D"
    elif x<60:
        grade="F"
    else:
        grade="Invalid input"
    return grade


def remove_vowels(string):
    for i in string:
        if i in 'aeiou':
            string=string.replace(i, '')
    return string

print(remove_vowels('gaziz'))


def normalize_name(somestring):
    newstring = ''
    for letter in somestring:
        if letter.isidentifier() or letter == ' ':
            newstring += letter
    return newstring.strip().lower().replace(' ', '_')
 

def cumulative_sum(oldlist):
    newlist = []
    for n in mylist:
        cumusum = sum(oldlist[:n])
        newlist.append(cumusum)
    return newlist
    
assert cumulative_sum([1, 2, 3, 4]) == [1, 3, 6, 10]





        
    






