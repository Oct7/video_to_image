import numpy as np
from PIL import Image, ImageDraw
import os


pathDir = 'image'
fileList = os.listdir(pathDir)


for image in fileList:    
    print(image)
    if image.split('.')[0]!='':
        # Open the input image as numpy array, convert to RGB
        img=Image.open('image/'+image).convert("RGB")
        npImage=np.array(img)

        h,w=img.size

        # Create same size alpha layer with circle
        alpha = Image.new('L', img.size,0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([50,-450,h-50,w+450],0,360,fill=255)

        # Convert alpha Image to numpy array
        npAlpha=np.array(alpha)

        # Add alpha layer to RGB
        npImage=np.dstack((npImage,npAlpha))

        # Save with alpha
        Image.fromarray(npImage[:,50:h-50]).save('result/'+image.split('.')[0]+'.png')



