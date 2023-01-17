from split_image import split_image
import os
from tkinter import simpledialog
import tkinter as tk
import time


def dialog(text):
    ROOT = tk.Tk()
    ROOT.withdraw()
    USER_INP = simpledialog.askstring(title="저장 폴더명",
                                      prompt=text)
    return USER_INP


pathDir = 'image'
fileList = os.listdir(pathDir)
cutNum = dialog('자를 갯수를 입력하세요.')
for image in fileList:
    print(image)
    if image.split('.')[0] != '':
        # 인풋 image, 세로컷수, 가로컷수
        if os.path.isdir('image'+'/%s' % image.split('.jpg')[0]+'/image'+'/%s' % image.split('.jpg')[0]) == False:
            os.makedirs('image'+'/%s' % image.split('.jpg')
                        [0]+'/image'+'/%s' % image.split('.jpg')[0])
            time.sleep(1)

        split_image("image/"+image, int(cutNum), 1, False, False,
                    output_dir='image'+'/%s' % image.split('.jpg')[0])
