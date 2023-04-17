import random
import string


def generate_value():
    value_lengt = 32
    value = ''.join(random.choice(string.ascii_letters) for i in range(value_lengt))
    return value


def generate_env():
    try:
        with open(".env", "w") as f:
            f.write("host=127.0.0.1\n")
            f.write("port=5433\n")
            f.write("database=scripty_db\n")
            f.write("user=scripty\n")
            f.write(f"password={generate_value()}\n")
            f.write(f"jwt_key={generate_value()}\n")
    except:
        print("Could not write to file")
    

        
if __name__ == "__main__":
    generate_env()
    print("Wrote to .env")