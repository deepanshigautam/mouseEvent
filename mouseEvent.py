import cv2
import numpy as np

def click_event(event, x, y , flags, param ):
  if event== cv2.EVENT_LBUTTONDOWN:
    blue= img[x, y , 0]
    green= img[x, y , 1]
    red= img[x, y , 2]
    cv2.circle(img , (x,y), 3 , (255,0,0), -1)
    points.append((x,y))

    mycolorimg= np.zeros((512,512,3), np.uint8)

    mycolorimg[:] =[blue, green , red]
    

    cv2.imshow('color', mycolorimg)

img = cv2.imread('lena.jpg')    
cv2.imshow('image', img)

points=[]

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()