import defisheye as df
import os

dtype = 'linear'
format = 'fullframe'
fov = 200
pfov = 120

pathDir = 'image' 
fileList = os.listdir(pathDir)


for image in fileList:    
    print(image)
    if image.split('.')[0]!='':
        img_out = f"result/{image}_{dtype}_{format}_{pfov}_{fov}.jpg"
        obj = df().Defisheye(image, dtype=dtype, format=format, fov=fov, pfov=pfov)
        obj.convert(img_out)

