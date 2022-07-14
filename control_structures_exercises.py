day = input('Enter a day of the week: ')

if day.lower() == 'monday':
    print('This is Monday')
else: 
    print('This is not Monday')

day = input('Enter a day of the week: ')


if day.lower() in ['saturday','sunday']:
    print('This is a weekend')
else:
    print('This is a weekday')


hours_worked = 55
hourly_rate = 15

if hours_worked <= 40:
    paycheck = hours_worked * hourly_rate
    print(paycheck)
    
elif hours_worked > 40:
    print('overtime worked')
    ot_hours = (hours_worked - 40)
    ot_rate = hourly_rate * 1.5
    
    ot_paycheck = (40 * hourly_rate) + (ot_hours * ot_rate)
    print(ot_paycheck)

i = 5 

while i <= 15:
    print(i)
    i += 1

i = 0 

while i <= 100:
    print(i)
    i += 2 

i = 100 

while i >= -10:
    print(i)
    i -= 5

i = 2 

while i < 1_000_000: 
    print(i)    
    i = i**2

i = 100 

while i >= 5:
    print(i)
    i -= 5

user_numb = input('Enter a number: ')
type(user_numb)
for x in range(1,11):
    print(f'{user_numb} x {x} = {int(user_numb) * x}')

for x in range(1,10):
    print(x * str(x))

while True:
    user_numb = input('Enter an odd number between 1 and 50: ')

    if user_numb.isdigit() == True:
        print('this is a digit.')
        if int(user_numb) % 2 == 1:
            print('this is odd.')
            if (int(user_numb) > 1) and (int(user_numb) < 50):
                print('this number is in range.')
                break
                
user_numb = int(user_numb)
                
for x in range(1,50):
    if x == user_numb:
        continue
    if x % 2 == 1:
        print(x)



while True:
    user_numb = input('Enter an positive number: ')

    if user_numb.isdigit() == True:
        print('this is a digit.')
        if int(user_numb) > 0:
            print('this is positive.')
            break
        
for x in range(int(user_numb)+1):
    print(x)


while True:
    user_numb = input('Enter an positive number: ')

    if user_numb.isdigit() == True:
        print('this is a digit.')
        if int(user_numb) > 0:
            print('this is positive.')
            break

user_numb = int(user_numb)        
for x in range(user_numb,0,-1):
    print(x)


for x in range(1,101):
    if x % 15 == 0: 
        print('FizzBuzz')
        continue
    if x % 3 == 0:
        print('Fizz')
        continue
    if x % 5 == 0:
        print('Buzz')
        continue
    print(x)


user_numb = input('Enter an integer: ')
user_numb = int(user_numb)
user_numb, user_numb**2, user_numb**3
for x in range(1,user_numb+1):
    print(f'{x}   |{x**2}   |{x**3}  ')


while True:
    user_numb = input('Enter an integer: ')
    user_numb = int(user_numb)
    
    for x in range(1,user_numb+1):
        print(f'{x}   |{x**2}   |{x**3}  ')
    
    user_yn = input('Would you like to continue? (y/n) ')
    if user_yn.lower() != 'y':
        break


user_grade = input('Enter a numerical grade from 0 - 100: ')
user_grade = int(user_grade)
if user_grade >= 88:
    print('A')
elif user_grade >= 80:
    print('B')
elif user_grade >= 67:
    print('C')
elif user_grade >= 60:
    print('D')
else:
    print('F')


while True:
    user_grade = input('Enter a numerical grade from 0 - 100: ')
    user_grade = int(user_grade)

    if user_grade >= 88:
        print('A')
    elif user_grade >= 80:
        print('B')
    elif user_grade >= 67:
        print('C')
    elif user_grade >= 60:
        print('D')
    else:
        print('F')
        
    user_yn = input('Would you like to continue? (y/n) ')
    if user_yn.lower() != 'y':
        break



books = [{'title': 'title111', 'author': 'author1', 'genre': 'genre1'},
 {'title': 'title222', 'author': 'author1', 'genre': 'genre2'},
 {'title': 'title333', 'author': 'author2', 'genre': 'genre2'},
 {'title': 'title444', 'author': 'author3', 'genre': 'genre2'}]
 for book in books:
    print(book)
user_genre = input('Enter a genre: ')
for book in books:
    if book['genre'] == user_genre:
        book['title']