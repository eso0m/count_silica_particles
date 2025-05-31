import cv2
import numpy as np
import os

#insert image path
image_path = 'SEM_image.jpg'

#check if the file exists
if not os.path.exists(image_path):
    print(f"Error: The file {image_path} does not exist.")
else:
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load the image.")
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #optional: edge detection before HoughCircles
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        blurred = cv2.GaussianBlur(edges, (9, 9), 2)
        
        #ddjusted parameters
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                                   param1=100, param2=25, minRadius=5, maxRadius=50)
        
        circle_count = 0
        if circles is not None:
            circles = np.uint16(np.around(circles))
            circle_count = len(circles[0])

            #draw circles on the original image for visualization
            for i in circles[0, :]:
                cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

            #display the result
            cv2.imshow('Detected Circles', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        print(f"Total number of circles detected: {circle_count}")
