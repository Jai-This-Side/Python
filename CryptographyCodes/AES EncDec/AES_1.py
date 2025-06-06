from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

key = b"16bytekey1234567"
data = b"Secret 16 bytes"

cipher = AES.new(key, AES.MODE_ECB)
paddedData = pad(data, AES.block_size)
encrypted = cipher.encrypt(paddedData)

print(binascii.hexlify(encrypted).decode())