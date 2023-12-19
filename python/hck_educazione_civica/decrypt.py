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

def read_key():
    with open('chiave.key', 'rb') as chiave:
        return chiave.read()

def encrypt_files(files, key):
    for file in files:
        with open(file, 'rb') as file_r:
            contenuto = file_r.read()
        contenuto_decriptato = Fernet(key).decrypt(contenuto)
        with open(file, 'wb') as file_w:
            file_w.write(contenuto_decriptato)

def main():
    files = read_files()
    encrypt_files(files, read_key())

if __name__ == '__main__':
    main()