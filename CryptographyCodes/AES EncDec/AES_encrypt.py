from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Input data
data = b"Secret Message!"  
key = get_random_bytes(16)  
iv = get_random_bytes(AES.block_size)  
# Encrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(data, AES.block_size))

# Save to file
with open("CryptographyCodes\AES EncDec\key.bin", "wb") as f:
    f.write(key)
with open("CryptographyCodes\AES EncDec\iv.bin", "wb") as f:
    f.write(iv)
with open("CryptographyCodes\AES EncDec\ciphertext.bin", "wb") as f:
    f.write(ciphertext)

print("Encryption complete. Files saved: key.bin, iv.bin, ciphertext.bin")