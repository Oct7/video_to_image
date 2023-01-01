import numpy as np
from PIL import Image, ImageDraw
import os


pathDir = 'image'
fileList = os.listdir(pathDir)
if '.DS_Store' in fileList:
    fileList.remove('.DS_Store')

for folder in fileList:
    fileList_second = os.listdir(pathDir+'/'+folder)
    if '.DS_Store' in fileList_second:
        fileList_second.remove('.DS_Store')
    for image in fileList_second:
        if image.split('.')[0] == 'jpg' and image.find('origin') != -1:
            # Open the input image as numpy array, convert to RGB
            img = Image.open(folder+'/'+image).convert("RGB")
            npImage = np.array(img)
            h, w = img.size

            # Create same size alpha layer with circle
            alpha = Image.new('L', img.size, 0)
            draw = ImageDraw.Draw(alpha)
            draw.pieslice([50, -450, h-50, w+450], 0, 360, fill=255)

            # Convert alpha Image to numpy array
            npAlpha = np.array(alpha)

            # Add alpha layer to RGB
            npImage = np.dstack((npImage, npAlpha))

            # Save with alpha
            Image.fromarray(
                npImage[:, 50:h-50]).save(pathDir+'/'+folder+'/'+image.split('.')[0]+'.png')
