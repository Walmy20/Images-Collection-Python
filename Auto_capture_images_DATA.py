import cv2
import time
import os

# 0 is to represent the first webcam and only one is connected
capture_video = cv2.VideoCapture(0)
# setting image quality to 1080p
capture_video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture_video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# image counter and total amount of images
img_counter =0
img_total = 40

# path where folders are going to be created
path = r"/media/Walmy20/Images" 

# folder numbers and names
folder_counter = 0
folder_path = "/Images_folder_"
# creating new folders dir
while(True):
    image_folder = path +folder_path + str(folder_counter) # since f"\" doesn't work use str() path + f"\Images_folder_{folder_counter}"
    if not os.path.exists(image_folder):
        os.mkdir(image_folder)
        break
    folder_counter += 1

# capturing data
while capture_video.isOpened():
    start = time.time()
    ret, frame = capture_video.read()
    #cv2.imshow('Title',frame) # Dont need but if you want to test uncomment

    #if cv2.waitKey(1) & 0xff == ord('w'): # Dont need 
        #break 
    if img_counter == img_total:
        print("Done Collecting DATA")
        break


    img_name = "data_{}.jpg".format(img_counter)
    cv2.imwrite(os.path.join(image_folder,img_name),frame)

    img_counter += 1

    time.sleep(13) # run after 13 sec

capture_video.release()
cv2.destroyAllWindows()
