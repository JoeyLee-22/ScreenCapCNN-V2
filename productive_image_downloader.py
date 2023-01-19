import requests
import os
import shutil
import time
from progress.bar import IncrementalBar

def download_rand_image(delete_images=False, num_to_download=0, image_width=500, image_height=500):
    path_and_foldername = "productive_images"
    url = "https://picsum.photos/{}/{}".format(image_width, image_height) # website to generate random photos given size
    
    if delete_images:
        while True:
            user_input = input("\nCONFIRM PRODUCTIVE DATA DELETION (y/n): ")
            if user_input=='y':
                shutil.rmtree(path_and_foldername)
                os.mkdir(path_and_foldername)
                break
            elif user_input=='n':
                break
    
    if num_to_download>0:
        num_images = len(os.listdir(path_and_foldername))
        print(),
        bar = IncrementalBar('DOWNLOADING RANDOM IMAGES:', max = num_to_download)
        start_time = time.time()
        for i in range(num_to_download):
            bar.next()
            response = requests.get(url)
            if response.status_code == 200:
                file_name = 'productive_{}.jpg'.format(i+1+num_images)
                file_path = path_and_foldername + "/" + file_name
                with open(file_path, 'wb') as f:
                    f.write(response.content)
        bar.finish()
        end_time = time.time() - start_time
        
        print("TOTAL IMAGES: {}".format(len(os.listdir(path_and_foldername))))
        print("DOWNLAOD TIME FOR {} IMAGES:".format(num_to_download), end = " ")
        if end_time > 3600:
            print('%dhr, %.1fmin\n' % (int(end_time/3600),((end_time-int(end_time/3600)*3600)/60)))
        elif end_time > 60:
            print("%dmin, %.2fs\n" % ((end_time/60), (end_time-int(end_time/60)*60)))
        else:
            print("%.2fs\n" % end_time)