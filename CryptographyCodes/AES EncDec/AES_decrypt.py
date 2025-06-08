from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open("CryptographyCodes\AES EncDec\key.bin", "rb") as f:
    key = f.read()
with open("CryptographyCodes\AES EncDec\iv.bin", "rb") as f:
    iv = f.read()
with open("CryptographyCodes\AES EncDec\ciphertext.bin", "rb") as f:
    ciphertext = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("Decrypted message:", decrypted.decode())
