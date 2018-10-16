from pyzbar.pyzbar import decode
from PIL import Image
print(decode(Image.open('C:/Users/hp/Desktop/Python/hello1.png'))[0][0])
