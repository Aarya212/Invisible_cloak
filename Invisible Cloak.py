#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
import cv2


# In[41]:


import time


# In[56]:


cap = cv2.VideoCapture(0)

#2 sec of buffer time for the camera to adjust
time.sleep(2)

#Allowing the code to capture the backgroung for over 30 iterations
background = 0
for i in range(30):
    ret, background = cap.read()

while(cap.isOpened()):
    ret, img = cap.read()
    
    if not ret:
        break;
        
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    
    mask1=mask1+mask2
    
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=5)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=3)
    
    mask2 = cv2.bitwise_not(mask1)
    
    res1 = cv2.bitwise_and(background, background, mask = mask1) 
    res2 = cv2.bitwise_and(img, img, mask = mask2) 
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    cv2.imshow("BOMBARDA!!", final_output)
    k = cv2.waitKey(1)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:




