import base32hex
import hashlib
from Crypto.Cipher import DES

# Encryption
password = "Password"
salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
key = password + salt
m = hashlib.md5(key.encode('utf-8'))
key = m.digest()
(dk, iv) = (key[:8], key[8:])
crypter = DES.new(dk, DES.MODE_CBC, iv)

plain_text = "I see you"
print("The plain text is:", plain_text)

# Padding the plain text to be a multiple of 8 bytes
plain_text += '\x00' * (8 - len(plain_text) % 8)
ciphertext = crypter.encrypt(plain_text.encode('utf-8'))
encode_string = base32hex.b32encode(ciphertext)
print("The encoded string is:", encode_string.decode('utf-8'))
import base32hex
import hashlib
from Crypto.Cipher import DES

# Decryption
password = "Password"
salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
key = password + salt
m = hashlib.md5(key.encode('utf-8'))
key = m.digest()
(dk, iv) = (key[:8], key[8:])
crypter = DES.new(dk, DES.MODE_CBC, iv)

encrypted_string = 'UH562EGM8RCHHTOUC5CTRS59OG======'
print("The encrypted string is:", encrypted_string)

encrypted_string = base32hex.b32decode(encrypted_string)
decrypted_string = crypter.decrypt(encrypted_string)
# Remove the padding
decrypted_string = decrypted_string.decode('utf-8').rstrip('\x00')
print("The decrypted string is:", decrypted_string)
