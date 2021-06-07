# Liquid Level Detector (Dynamic)		

This project was developed by [me](https://au.linkedin.com/in/sep-kimiaei-b007211b1)  in the hopes of being able to use Computer Vision via OpenCV in a way that would be able to  **not only** determine water levels on a pre-recorded video but to also measure the water level on a live video feed, without the use of any onboard sensors and external object tracking.

## Motivation:

A team of postgraduate researches at the center of Marine Research at the University of Western Australia needed a software solution that would assist in data analysis of an ROV (Remote Operated Vehicle's) depth measurements without the use of onboard sensors. This was my implementation of a solution that worked and helped reduce errors significantly.

## Issues & Milestones:
-- registering shadows of water edges [fixed]
-- registering different colours (with glass over) [fixed]
-- registering different colors of rov model [fixed] 

## Prerequisites (Python)
- cv2
- math
- argparse
- imutils
- collections

## Recent Version Edits <i>3.21</i>

<li>Added new Gaussian Blur Values
<li>Restricted Inital Video Frame Size Scope

## Contributions:
[https://github.com/iftheqhar/opencv2_python](https://github.com/iftheqhar/opencv2_python)


[https://github.com/sashagaz/Hand_Detection](https://github.com/sashagaz/Hand_Detection)


[https://github.com/iftheqhar/OpenCV2-Python](https://github.com/iftheqhar/OpenCV2-Python)


[https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/](https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/)


[https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/](https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/)


[https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/](https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/)

# Methodology:

I practiced detecting liquid (especially transparent ones such as water) using a wide variety of avenues. This resulted in a series of vastly differing performance reports and findings. These methods included **Colour Tracking**, **Frame Change Detection**, **Gaussian Blur**, **Canny Edge Detection** and a combination of all.

## Colour Tracking (with range):

This method  involved specifying a range of values that openCV would then start tracking. This method is a commonly used one within the scope of openCV methodologies.

## Frame Change Detection:	

You can save any file of the workspace to **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Save on**. Even if a file in the workspace is already synced, you can save it to another location. StackEdit can sync one file with multiple locations and accounts.

## Results & Analysis:
The latest version of this program runs at a very high efficiency rate, being able to accurately determine the water depth using a live video feed.
  
