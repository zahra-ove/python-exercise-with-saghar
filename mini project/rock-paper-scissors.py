# بازی سنگ، کاغذ، قیچی 

# هر بار از کاربر پرسیده شود که حدسش چیه ( کاربر تایپ میکنه که سنگ رو میخواد یا کاغذ یا قیچی)
# خود برنامه ایی که مینویسی که خودش یکی از سه گزینه رو به صورت رندم انتخاب کنه
# بعد هر کدوم که برنده شد رو اعلام میکنیم

import random

options = ['rock', 'paper', 'scissors']
user_guess = ''

while True:
    user_guess = input('Please choose one of rock/paper/scissors option:\n').lower()
    if user_guess == 'finish':
        break
       
    if user_guess not in options:
        continue
        
    system_guess = random.choice(options).lower()

    if system_guess == user_guess:
        print('equal')
        
    if system_guess == 'rock':
        if user_guess == 'paper':
            print('You are the winner!\n system chose the ' + system_guess)
        elif user_guess == 'scissors':
            print('System are the winner!\n system chose the ' + system_guess)
            
    if system_guess == 'paper':
        if user_guess == 'scissors':
            print('You are the winner!\n system chose the ' + system_guess)
        elif user_guess == 'rock':
            print('System are the winner!\n system chose the ' + system_guess)
            
            
    if system_guess == 'scissors':
        if user_guess == 'rock':
            print('You are the winner!\n system chose the ' + system_guess)
        elif user_guess == 'paper':
            print('System are the winner!\n system chose the ' + system_guess)
            

print('Goodbye!')