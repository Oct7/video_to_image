import cv2
# 비디오 폴더명
vidCap = cv2.VideoCapture('video/origin_1_lrv.mp4')
success, image = vidCap.read()
count = 0
while success:
    if count > 420 and count < 833:
    #비디오 출력명
        cv2.imwrite("result/origin_1/%06d.png" %
                    count, image)     # save frame as JPEG file
        success, image = vidCap.read()
        print('Read a new frame: ', success)
    success, image = vidCap.read()
    count += 1

