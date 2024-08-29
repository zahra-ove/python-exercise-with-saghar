# فرض کن یک سری سؤال داری که باید از کاربر بپرسی
# این سوال-جوابها رو به صورت یک لیست آماده کردی
# حالا دونه دونه سؤال رو از کاربر میپرسی و جوابی که کاربر میده رو با پاسخ صحیح مقایسه میکنی 
# و اگر کاربر جواب درست داده بود یک نمره به امتیاز کاربر اضافه میکنیم
# و اگر جوابش درست نبود هیچ امتیازی نمیگیره. در آخر به کاربر میگیم که امتیازش چقدر بوده

# لیست پرسش-پاسخ ها رو واست میذارم که راحت پیش بری

qa_set = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the capital of Spain?", "answer": "Madrid"},
    {"question": "What does CPU stands for?", "answer": "central processing unit"},
]

playing = input('Do you want to play?(yes/no)  ')

if playing.lower() == 'no':
    quit()

print('Ok, Let\'s start')

score = 0

for qa in qa_set:
    answer = input(qa['question']).lower()

    if answer == qa['answer'].lower():
        print('Correct!')
        score = score + 1
    else:
        print('Incorrect')


print('You got ' + str(score) + ' questions correct.')

