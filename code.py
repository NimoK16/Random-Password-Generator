import secrets
import string

def generate_password(length, use_lowercase, use_uppercase=True, use_digits=True, use_symbols=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''
    
    all_characters = lowercase + uppercase + digits + symbols
    
    p = ''.join(secrets.choice(all_characters) for _ in range(length))
    return p
def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length: "))
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").lower() == 'y'
    try :
           
        password = generate_password(length,use_lowercase, use_uppercase, use_digits, use_symbols)
        print(f"Your generated password is: {password}")
    except ValueError as error:
        
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
