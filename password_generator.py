import random
import string
def generate_password(length=12):
    characters=string.ascii_letters+ string.digits.punctuation
    password=''.join(random.choice(characters)for_in range(length))
return password
