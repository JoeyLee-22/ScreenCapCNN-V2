import numpy as np
import time
import cv2
import pyautogui
from PIL import Image
import os

def start_monitor(cnn_instance, seconds=300):    
    productive_counter = 1
    unproductive_counter = 1
    
    while(True):
        screenshot = pyautogui.screenshot() # (2100, 3360, 4)
        # screenshot.save('screenshots/screenshot.png')
        
        # screenshot = Image.open('screenshots/screenshot.png')
        resized_screenshot = screenshot.resize((1280,720))
        # resized_screenshot.save('screenshots/resized_screenshot.png')
        
        screenshot = cv2.cvtColor(np.array(resized_screenshot), cv2.COLOR_RGB2BGR)        
        
        result = cnn_instance.classify(np.asarray(screenshot))
        
        # productive = num close to 0, unproductive = num close to 1
        if (result<=0.5):
            print("\n\n{}: Productive".format(result))
            resized_screenshot.save('productive_screenshots/productive_screenshot{}.png'.format(productive_counter))
            productive_counter+=1
        else:
            print("\n\n{}: Unproductive".format(result))
            resized_screenshot.save('unproductive_screenshots/unproductive_screenshot{}.png'.format(unproductive_counter)) 
            unproductive_counter+=1
            
            title = "Unproductive Actvity Detected"
            message = "Check ____ to confirm"
            command = f'''
            osascript -e 'display notification "{message}" with title "{title}"'
            '''
            os.system(command)
        for secs in range (seconds):
            time.sleep(0.99)
            print(str(seconds-int(secs)) + "/" + str(seconds), end='\r')