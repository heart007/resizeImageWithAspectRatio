import cv2
import numpy as np 
import os
import argparse
def width_height_problem():
	img = cv2.imread('img.jpg')
	height = np.size(img,0) 
	width = np.size(img,1)
	height_new = 500
	width_old= (width / height)
	width_new = round((height_new * width_old))
	print (height_new)
	print (width_new)
width_height_problem()
