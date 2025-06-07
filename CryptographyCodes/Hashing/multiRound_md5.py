import hashlib

p = "password"
h = p.encode()

for i in range (10):
    hash_result = hashlib.new("md5", h).hexdigest()
    print (i+1, hash_result)