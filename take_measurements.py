import cv2
import numpy as np
import os

os.system('fswebcam -r 320x240 -S 3 --jpeg 50 --save /home/pi/%H%M%S.jpg')
