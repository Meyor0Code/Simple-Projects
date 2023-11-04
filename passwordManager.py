from cryptography.fernet import Fernet
import os

# Function to generate a key for encryption/decryption
def generate_key():
    return Fernet.generate_key()

# Function to load the key from a file or generate a new one
def load_key(key_file):
    if os.path.exists(key_file):
        with open(key_file, 'rb') as file:
            return file.read()
    else:
        key = generate_key()
        with open(key_file, 'wb') as file:
            file.write(key)
        return key

# Function to encrypt a password
def encrypt_password(key, password):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

# Function to decrypt a password
def decrypt_password(key, encrypted_password):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()

# Function to save passwords to a file
def save_passwords(filename, passwords):
    with open(filename, 'w') as file:
        for site, password in passwords.items():
            file.write(f"{site}: {password}\n")

# Function to load passwords from a file
def load_passwords(filename):
    passwords = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(': ')
                if len(parts) == 2:
                    site, encrypted_password = parts
                    passwords[site] = encrypted_password
    return passwords

# Main function
def main():
    key = load_key('key.key')
    passwords_file = 'passwords.txt'
    passwords = load_passwords(passwords_file)

    while True:
        print("\nOptions:")
        print("1. Add/Update Password")
        print("2. Retrieve Password")
        print("3. List Stored Sites")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            site = input("Enter the site or application name: ")
            password = input("Enter the password: ")
            encrypted_password = encrypt_password(key, password)
            passwords[site] = encrypted_password
            save_passwords(passwords_file, passwords)
            print(f"Password for {site} saved/updated.")
        elif choice == "2":
            site = input("Enter the site or application name: ")
            if site in passwords:
                encrypted_password = passwords[site]
                password = decrypt_password(key, encrypted_password)
                print(f"Password for {site}: {password}")
            else:
                print(f"No password found for {site}.")
        elif choice == "3":
            print("Stored Sites:")
            for site in passwords.keys():
                print(site)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
