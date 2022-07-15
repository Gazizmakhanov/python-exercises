from function_exercises import is_vowel
print(is_vowel('a'))

from function_exercises import calculate_tip
print(calculate_tip(110,0.15))

import itertools as it
print(len(list(it.product('abc','1,2,3'))))

print(len(list(it.combinations('abcd', 2))))

print(len(list(it.permutations('abcd', 2))))

import json
profiles=json.load(open('profiles.json'))

num_of_users=len(profiles)

print(num_of_users)


num_of_users=0
for i in profiles:
    if i['isActive']==True:
        num_of_users+=1
print(num_of_users)


total_balance=[]
replace1=[]
replace2=[]
total1=[]
for i in profiles:
    total_balance.append(i['balance'])
for i in total_balance:
    replace1.append(i.replace('$',''))
for i in replace1:
    replace2.append(i.replace(',',''))
for i in replace2:
    total1.append(float(i))
grand_total=sum(total1)

print(grand_total)

avg_balance=grand_total/len(profiles)


print(avg_balance)

print(min(total1))
the_name='a'
for i in profiles:
    if i['balance']=='$1,214.10':
        the_name=i['name']
print(the_name)


print(max(total1))
the_name1='a'
for i in profiles:
    if i['balance']=='$3,919.64':
        the_name1=i['name']
print(the_name1)



fruits=[]
for i in profiles:
    fruits.append(i['favoriteFruit'])
fruits=set(fruits)
apple=0
strawberry=0
banana=0
for j in profiles:
    if j['favoriteFruit']=='apple':
        apple+=1
    elif j['favoriteFruit']=='strawberry':
        strawberry+=1
    else:
        banana+=1
print(apple, strawberry, banana)

unread_list=[]
for m in profiles:
    the_digit=""
    for n in m['greeting']:
        if n.isdigit()==True:
            the_digit=the_digit.strip()+n.strip()
    unread_list.append(int(the_digit))

print(sum(unread_list))




    

    
















    # float(i['balance'].replace(z,''))







# print(profiles[0]['isActive'])

