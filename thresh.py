import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh =  cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold_inv, thresh_inv =  cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv. THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholded', adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv. THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Thresholded Inverse', adaptive_thresh_inv)

cv.waitKey(0)