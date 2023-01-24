import string
import random

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    # Lista zawierająca słowa zabronione
    forbidden_words = ["password", "qwerty", "1234"]
    while True:
        password = ''.join(random.choice(characters) for _ in range(8))
        if (any(i.islower() for i in password) and
                any(i.isupper() for i in password) and
                any(i.isdigit() for i in password) and
                any(i in string.punctuation for i in password) and
                not any(i in forbidden_words for i in password.split())):
            return password

# Przykład:
print(generate_password())