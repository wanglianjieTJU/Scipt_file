import os
from PIL import Image

img = Image.open('G://000000498856.jpg')
if img.mode == 'L':
    img=Image.open('G://000000498856.jpg').convert('RGB')
    print img.mode
else:
    print'nochange'