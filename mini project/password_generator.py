import random;
import string;

def password_generator(min_length=5, has_number=False, has_special=False):
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation
    
    pwd = ''
    while len(pwd) < min_length:
        pwd += random.choice(letters)
        if has_number:
            pwd += random.choice(numbers)
        if has_special:
            pwd += random.choice(special_characters)
            
    return pwd

print(password_generator(10, True, True))