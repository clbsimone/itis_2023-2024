from Crypto.Cipher import AES

key = b'1234567812345678'
vi = key

cifra_AES = AES.new(key, AES.MODE_CBC, vi)

message = b'12345678123456781234567812345678'
mex_cifrato = cifra_AES.encrypy(message)

print(f'il mex cifrato: {mex_cifrato}')

decifra_AES = AES.new(key, AES.MODE_CBC, vi)
mex_decifrato = decifra_AES.decrypt(mex_cifrato)

print(f'il mex decifrato: {mex_decifrato}')