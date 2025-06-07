import hashlib

# hash_code = hashlib.new("md5", "HELLO".encode()).hexdigest() // other way to encode
hash_code = hashlib.new("md5", b"HELLO").hexdigest() 
print(hash_code)