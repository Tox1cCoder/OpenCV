import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # For images, videos, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # For live video
    capture.set(3, width)
    capture.set(4, height)

# Reading Image
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)

img_resized = rescaleFrame(img)
cv.imshow('Image Resized', img)

# Reading Video
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)