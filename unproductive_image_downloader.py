import cv2
import os
import shutil
from PIL import Image

def download_youtube_frames(delete_frames=False, frames_needed=0, link="", frames_skipped=500):
    path_and_foldername = "unproductive_images"
    vidcap = cv2.VideoCapture('minecraft.mp4')
    success,image = vidcap.read()
    currentframe = 0
   
    if delete_frames:
        while True:
            user_input = input("\nCONFIRM UNPRODUCTIVE DATA DELETION (y/n): ")
            if user_input=='y':
                shutil.rmtree(path_and_foldername)
                os.mkdir(path_and_foldername)
                break
            elif user_input=='n':
                break

    if frames_needed>0:
        while success:
            currentframe += 1
            file_name = "frame{}.jpg".format(currentframe)
            cv2.imwrite(os.path.join(path_and_foldername, file_name), image)
            
            for i in range(frames_skipped-1):
                success,image = vidcap.read()
            
            if currentframe==frames_needed:
                break
        
        print("\nFRAMES DOWNLOADED: {}\n".format(currentframe))