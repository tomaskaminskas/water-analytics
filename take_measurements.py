import cv2
import numpy as np
import os

folder = '/home/pi/images/'
os.system('fswebcam -r 640x480 -S 3 --jpeg 50 --save /home/pi/images/%H%M%S.jpg')
for filename in os.listdir(folder):
	img = cv2.imread(os.path.join(folder,filename))
	if img is not None:
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		os.remove(os.path.join(folder,filename))
