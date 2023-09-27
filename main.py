import cv2 as cv
img = cv.imread("pics/pic1.jpg")
cv.imshow("Image", img)
resized_image = cv.resize(img, (256, 256))
cv.imshow("Image2", resized_image)
gray_image = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow("Image3", gray_image)
threshold_value = 170
_, binary_image = cv.threshold(gray_image, threshold_value, 255, cv.THRESH_BINARY)

cv.imshow("Image4", binary_image)
blur_image = cv.GaussianBlur(gray_image, (5,5), 0)
canny_image = cv.Canny(blur_image, 30, 200, 3)
dilate_image = cv.dilate(canny_image, (5,5), iterations=5)
contours, _ = cv.findContours(dilate_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(dilate_image, contours, -1, (0,0,255), 2)
print(f"Number of coins: {len(contours)}")
cv.imshow("Image 5",dilate_image)

cv.waitKey(0)
