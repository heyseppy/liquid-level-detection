import cv2
import cv2 as cv
import numpy as np
import math
import argparse
import imutils
from collections import deque


cap = cv2.VideoCapture(1)


while( cap.isOpened() ) :
	ret,img = cap.read()
	rest,img1 = cap.read()
	img = img[5:600, 0:43]
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	ret,thresh1 = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
  
	contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	drawing = np.zeros(img.shape,np.uint8)
	drawing = drawing[20:500, 22:24]
	max_area=0
   
	for i in range(len(contours)):
			cnt=contours[i]
			area = cv2.contourArea(cnt)
			if(area>max_area):
				max_area=area
				ci=i
	cnt=contours[ci]
	hull = cv2.convexHull(cnt)
	moments = cv2.moments(cnt)
	if moments['m00']!=0:
				cx = int(moments['m10']/moments['m00']) # cx = M10/M00
				cy = int(moments['m01']/moments['m00']) # cy = M01/M00
			  
	centr=(cx,cy)       
	cv2.circle(drawing,centr,1,[0,0,255],2)       
	#cv2.drawContours(drawing,[cnt],0,(0,255,0),2) 
	cv2.drawContours(drawing,[hull],0,(0,0,255),2) 
	
	
	
	
	
	
	
		# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-v", "--video",
		help="path to the (optional) video file")
	ap.add_argument("-b", "--buffer", type=int, default=64,
		help="max buffer size")
	args = vars(ap.parse_args())
	
	greenLower = (0, 120, 70)
	greenUpper = (180, 255, 255)
	pts = deque(maxlen=args["buffer"])
	# if a video path was not supplied, grab the reference
	# to the webcam
	if not args.get("video", False):
		vs = drawing
	# otherwise, grab a reference to the video file
	else:
		vs = cv2.VideoCapture(args["video"])
	
	
	frame = drawing
	# handle the frame from VideoCapture or VideoStream
	frame = frame[1] if args.get("video", False) else frame
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
	# resize the frame, blur it, and convert it to the HSV
	# color space
	#frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)    


	
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None
	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		centerx = int(M["m10"] / M["m00"])
		centery = int(M["m01"] / M["m00"]) - int(radius)
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			 #cv2.circle(img1, (int(x), int(y)), int(radius),(0, 255, 255), 2)
			 cv2.circle(img1, (40,centery), 5, (255, 0, 0), -1)
			 cv2.putText(img1, "Water Elevation: " +str(centery), (40, centery - 20), cv2.FONT_HERSHEY_SIMPLEX , 0.5,  (172, 90, 0), 2, cv2.LINE_AA, False) 

	# update the points queue
	pts.appendleft(center)
	
	
	for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue
		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break

	cv2.imshow('output',img1)
	cv2.imshow('input',img)
				
	k = cv2.waitKey(10)
	if k == 27:
		break