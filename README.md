# Motion Detection with Python

This project uses OpenCV and Python to detect motion in a video stream.

## Requirements

* Python 3
* OpenCV
* winsound (only for Windows)

## Instructions

1. Install the required Python packages:

~~~
    pip install opencv-python
    pip install winsound
~~~
2. Run the `motion_detection.py` script:

~~~
    python motion_detection.py
~~~

The script will open a window showing the video stream from your webcam. If any motion is detected, an alarm will sound and the moving object will be highlighted in the window.

## How it works

The script first captures two frames from the webcam. The first frame is used as the background, and the second frame is compared to it to detect any changes. If the difference between the two frames is above a certain threshold, it is considered to be motion.

The moving object is then identified by finding the contours in the difference frame. A contour is a closed curve in an image. The contours of the moving object are highlighted in the window.

An alarm is sounded if the moving object is large enough. The size of the moving object is determined by its area.
