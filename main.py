import cv2
import numpy as np
import math

img = cv2.imread("rolls1.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("roll1.jpg", cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.43)

pts = []

for pt in zip(*loc[::-1]):
    pts.append(pt)

pts = set(pts)

pt0 = 0
pt1 = 0
circles = []

for pt in pts:
    if (pt[0] not in range(pt0 - 150, pt0 + 150) and pt[1] not in range(pt1 - 150, pt1 + 150)):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)
        #cv2.circle(img, (pt[0] + math.floor(w/2), pt[1] + math.floor(h/2)), 5, (255, 255, 255), 1)
        circles.append((pt[0] + math.floor(w/2), pt[1] + math.floor(h/2)))
    pt0 = pt[0]
    pt1 = pt[1]

circles.sort()
cv2.line(img, circles[0], circles[-1], (255, 255, 255), 3)
pxs = math.sqrt((circles[-1][0] - circles[0][0])**2 + (circles[-1][1] - circles[0][1])**2)
print('Расстояние между рулонами = ', round(pxs), 'px')

cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()