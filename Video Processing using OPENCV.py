from cv2 import *
import os
c=os.getcwd()
a=os.path.dirname(c)
print(a)
addr=os.path.join(a,'Generated')
c=os.path.join(a,'Python Programs','RoseBloom.mp4')
print(c)
video = VideoCapture(c)
#while True:
#    check,frame=video.read()
#    imshow('captured',frame)
#    k = waitKey(1)
#    if k==ord('b'):
#        break

frame_no=video.get(5)*6
video.set(0,frame_no)
check,frame=video.read()
path=os.path.join(addr,'frame_as_6.jpg')
imwrite(path,frame)
frame[:,:,0]=0
frame[:,:,1]=0
path=os.path.join(addr,'frame_as_6_red.jpg')
imwrite(path,frame)
video.release()
destroyAllWindows
