import base64

with open("sample.txt", 'rb') as f:
    c = f.read()
    
encoded = base64.b64encode(c)

print(encoded)

decoded = base64.b64decode(encoded)

print(decoded)