import cv2
import os
import shutil
from PIL import Image
from vidgear.gears import CamGear

def download_youtube_frames(delete_frames=False, frames_needed=0, link="", frames_skipped=500):
    stream = CamGear(source=link, stream_mode=True, time_delay=1).start()
    path_and_filename = "unproductive_images"
    currentframe = 0
   
    if delete_frames:
        while True:
            user_input = input("\nCONFIRM UNPRODUCTIVE DATA DELETION (y/n): ")
            if user_input=='y':
                shutil.rmtree(path_and_filename)
                os.mkdir(path_and_filename)
                break
            elif user_input=='n':
                break

    if frames_needed>0:
        while True:
            for i in range(frames_skipped):
                frame = stream.read() ### using functions from vidGear module
            if frame is None:
                break
            
            currentframe+=1
            file_name = 'screenshot_{}.jpg'.format(currentframe)
            file_path = path_and_filename + "/" + file_name
            with open(file_path, 'wb') as f:
                f.write(frame)
                
            if currentframe==frames_needed:
                break

        cv2.destroyAllWindows()
        stream.stop()
        print("\nFRAMES DOWNLOADED: {}\n".format(currentframe))