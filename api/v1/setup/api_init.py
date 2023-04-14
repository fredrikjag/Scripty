import random
import string
import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def generate_value():
    value_lengt = 32
    value = ''.join(random.choice(string.ascii_letters) for i in range(value_lengt))
    return value

def create_env_key(key):
    value = generate_value()
    dotenv.set_key(dotenv_file, key, value)

if __name__ == "__main__":
    print("hello")