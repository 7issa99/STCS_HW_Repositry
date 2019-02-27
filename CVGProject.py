# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:19:21 2018

@author: Muneera
"""

import numpy as np
import cv2


# Initialization of src 4-point : top left, top right, bottom left, bottom right
pts = [(0,0),(0,0),(0,0),(0,0)]
pointIndex = 0 # pointer for the above array index

path ='C:\\Users\\user\\Desktop\\t1.jpg'
img = cv2.imread(path)



#-----------------------------------------------


ASPECT_RATIO = (500,600) # initilaize the output window ratio

#the below line is to define the destination points where the four input points will be mapped to this ponits
pts2 = np.float32([[0,0],[ASPECT_RATIO[1],0],[0,ASPECT_RATIO[0]],[ASPECT_RATIO[1],ASPECT_RATIO[0]]])


# the below function is for trigger mouse double clicking 
# it will drow red circle on the clicking point and store the clicking location on pts array 
def draw_circle(event,x,y,flags,param):
	global img
	global pointIndex
	global pts

	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img,(x,y),5,(0,0,255),-1)
		pts[pointIndex] = (x,y)
		pointIndex = pointIndex + 1
        
        
# the below function is for checking if the user select four points or not
def selectFourPoints():
	global img
	global pointIndex

	print ("Please select 4 points, by double clicking on each of them in the order: \n\
	top left, top right, bottom left, bottom right.")


	while(pointIndex != 4):
		cv2.imshow('image',img)
		key = cv2.waitKey(20) & 0xFF
		if key == 27: #to exit the app
			return False

	return True


cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle) # set the mouse trigger function to the mouse event

while(1):
	if(selectFourPoints()):

		# coverting the four selected points to float 
		pts1 = np.float32([\
			[pts[0][0],pts[0][1]],\
			[pts[1][0],pts[1][1]],\
			[pts[2][0],pts[2][1]],\
			[pts[3][0],pts[3][1]] ])
    
        # pre-define function to calculate the transformation matrix using the source and destination points
		M = cv2.getPerspectiveTransform(pts1,pts2)

		while(1):

			cv2.imshow('image',img)
			k = cv2.waitKey(20) & 0xFF
           
            # pre-define function to apply the transformation matrix on the image to get frontal view of the selected points
			dst = cv2.warpPerspective(img,M,(600,500))
			cv2.imshow("output",dst)

			key = cv2.waitKey(10) & 0xFF
			if key == 27:#ESC key
				break
	else:
		print ("Exit") #this line will be executed if the user press ESC before select 4 ponits "close the app before the output"

	break
    
#-----------------------------------------------

#cv2.imshow('ImageWindow', img)
#cv2.waitKey(0)
cv2.destroyAllWindows()