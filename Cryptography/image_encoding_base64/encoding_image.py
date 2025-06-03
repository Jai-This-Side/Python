import base64

with open('original_image.jpg', 'rb') as f:
    encoding_data = f.read()

print(base64.b64encode(encoding_data))