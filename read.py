import cv2 as cv
 
img = cv.imread('images/cat.png')

cv.imshow('cat',img)

def rescaleFrame(frame, scale=0.75):
     width=int(frame.shape[1]*scale)
     height=int(frame.shape[0]*scale)

     dimension=(width,height)


     return cv.resize(frame, dimension,interpolation=cv.INTER_AREA)
resized_image=rescaleFrame(img)
cv.imshow('Image', resized_image)
cv.waitKey(0)
#live videos
#def changeRes(width,height):
  #  capture.set(3,width)
   # capture.set(4,height)
#reading videos
# capture=cv.VideoCapture('videos/vi.mp4')

# while True:
#     isTrue, frame=capture.read()

#     frame_resized= rescaleFrame(frame, scale=.2)


#     cv.imshow('videos', frame)
#     cv.imshow('video Resized', frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

 