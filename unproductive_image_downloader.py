import cv2
import os
import shutil
from PIL import Image
import time
from progress.bar import IncrementalBar

def download_youtube_frames(delete_frames=False, frames_needed=0, frames_skipped=200):
    path_and_foldername = "unproductive_images"
    vidcap = cv2.VideoCapture('videos/minecraft.mp4')
    success,image = vidcap.read()
    currentframe = 0
    
    if not os.path.exists(path_and_foldername): os.mkdir(path_and_foldername)
    if not os.path.exists("videos"): os.mkdir("videos")

    if delete_frames:
        while True:
            user_input = input("\nCONFIRM UNPRODUCTIVE DATA DELETION (y/n): ")
            if user_input=='y':
                shutil.rmtree(path_and_foldername)
                os.mkdir(path_and_foldername)
                break
            elif user_input=='n':
                break

    print()
    if frames_needed>0:
        bar = IncrementalBar('DOWNLOADING FRAMES:', max = frames_needed)
        start_time = time.time()
        while success:
            bar.next()
            currentframe += 1
            file_name = "frame{}.jpg".format(currentframe)
            cv2.imwrite(os.path.join(path_and_foldername, file_name), image)
            
            for i in range(frames_skipped-1):
                success,image = vidcap.read()
            
            if currentframe==frames_needed:
                break
        bar.finish()
        end_time = time.time() - start_time
        
        print("DOWNLOAD TIME FOR {} FRAMES:".format(frames_needed), end = " ")
        if end_time > 3600:
            print('%dhr, %.1fmin\n' % (int(end_time/3600),((end_time-int(end_time/3600)*3600)/60)))
        elif end_time > 60:
            print("%dmin, %.2fs\n" % ((end_time/60), (end_time-int(end_time/60)*60)))
        else:
            print("%.2fs\n" % end_time)