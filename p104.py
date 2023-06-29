import cv2
solar=cv2.imread("solar-system.jpg")
cv2.putText(solar, "sun", (20,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(250,0,0))
cv2.putText(solar, "mercury", (110,180), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,250,0))
cv2.putText(solar, "venus", (190,270), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,0,250))
cv2.putText(solar, "earth", (300,270), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(250,0,0))
cv2.putText(solar, "mars", (375,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,250,0))
cv2.putText(solar, "jupiter", (500,270), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,0,250))
cv2.putText(solar, "saturn", (700,90), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(250,0,0))
cv2.putText(solar, "uranus", (920,110), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,250,0))
cv2.putText(solar, "neptune", (1150,130), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,0,250))
cv2.imshow("planets", solar)
cv2.waitKey(0)

