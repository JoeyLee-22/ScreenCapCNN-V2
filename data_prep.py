from PIL import Image
from numpy import asarray
import numpy as np
import os
import time
from progress.bar import IncrementalBar  

def convert_images(array, label, start_index, end_index, type_array):
    start_time = time.time()
    bar = IncrementalBar('PREPPING {} IMAGES:'.format(type_array), max = (end_index-start_index)*2)
    for i in range(start_index, end_index):
        bar.next()
        img = Image.open('productive_images/image{}.jpg'.format(i+1))
        array.append(asarray(img)/255.0) # divide by 255 to normalize between 0 and 1
        label.append(0)
        
        bar.next()
        img = Image.open('unproductive_images/frame{}.jpg'.format(i+1))
        array.append(asarray(img)/255.0) # divide by 255 to normalize between 0 and 1
        label.append(1)
    bar.finish()
    end_time = time.time() - start_time
    
    print("CONVERT TIME FOR {} IMAGES:".format((end_index-start_index)*2), end = " ")
    if end_time > 3600:
        print('%dhr, %.1fmin\n' % (int(end_time/3600),((end_time-int(end_time/3600)*3600)/60)))
    elif end_time > 60:
        print("%dmin, %.2fs\n" % ((end_time/60), (end_time-int(end_time/60)*60)))
    else:
        print("%.2fs\n" % end_time)

def load_data(num_train, num_test, height, width):
    train_images, train_labels = [], []
    test_images, test_labels = [], []
    total_images = len(os.listdir('productive_images')) + len(os.listdir('unproductive_images'))
    
    # gives number of images to use as training images
    # convert_images takes half from productive and half from unproductive 
    convert_images(train_images, train_labels, 0, int(num_train/2), 'TRAIN') 
    train_images = np.asarray(train_images)
    train_labels = np.asarray(train_labels)
    
    # gives number of images to use as testing images
    # convert_images takes half from productive and half from unproductive
    convert_images(test_images, test_labels, int(num_train/2), int(num_train/2)+int(num_test/2), 'TEST') 
    test_images = np.asarray(test_images)
    test_labels = np.asarray(test_labels)

    print(train_images.shape)
    print(train_labels.shape)
    print(test_images.shape)
    print(test_labels.shape)
    print()

    return (train_images, train_labels), (test_images, test_labels)