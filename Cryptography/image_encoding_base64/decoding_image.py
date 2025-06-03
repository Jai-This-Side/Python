import base64
from encoding_image import data

transmitted_data = data

decoded_data = base64.b64decode(transmitted_data)

with open('image1.jpg', 'wb') as f:
    data = f.write(data)