# pyright: reportUnboundVariable=false

import time
import os
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential, load_model as keras_load_model
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout, Activation
from data_prep import load_data

class convolutional_neural_network():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.model_name = 'TwoClassClassificationModel'

    def classify(self, image):
        return np.argmax(self.model.predict(image))

    def run(self, save_model=False, load_model=False, train=True, evaluate=True, plot=True, num_train=0, num_test=0, epochs=10):        
        (train_images, train_labels), (test_images, test_labels) = load_data(num_train, num_test, self.height, self.width)

        if not load_model and train:
            self.model = Sequential()

            self.model.add(Conv2D(32, (3, 3), input_shape = (self.height, self.width, 3), activation = 'relu'))
            self.model.add(MaxPooling2D(pool_size = (2, 2)))

            self.model.add(Conv2D(32, (3, 3), activation = 'relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2)))

            self.model.add(Conv2D(64, (3, 3), activation = 'relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2)))

            self.model.add(Flatten())

            self.model.add(Dense(units = 64, activation = 'relu'))

            self.model.add(Dropout(0.5))

            self.model.add(Dense(1))
            self.model.add(Activation('sigmoid'))
            
            self.model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

            self.model.summary()

            start_time = time.time()            
            hist = self.model.fit(train_images, train_labels, epochs=epochs, validation_data=(test_images, test_labels))
            end_time = time.time() - start_time

            if end_time > 3600:
                print('Total Training Time: %dhr %.1fmin\n\n' % (int(end_time/3600),((end_time-int(end_time/3600)*3600)/60)))
            elif end_time > 60:
                print("Total Training Time: %dmin %.2fs\n\n" % ((end_time/60), (end_time-int(end_time/60)*60)))
            else:
                print("Total Training Time: %.2fs\n\n" % end_time)

        if load_model and train:
            self.model = keras_load_model('%s.h5' % self.model_name)

        if save_model:
            self.model.save('%s.h5' % self.model_name)

        # if plot and not load_model:            
        #     f = plt.figure()
        #     f.add_subplot(2,1,1)
        #     plt.plot(hist.history['accuracy'], label='train accuracy')
        #     plt.plot(hist.history['val_accuracy'], label ='val accuracy')
        #     plt.title('Model Accuracy (top) and Model Loss (bottom)')     
        #     plt.ylabel('Accuracy')
        #     plt.legend(loc='lower left')
            
        #     f.add_subplot(2,1,2)
        #     plt.plot(hist.history['loss'], label='train loss')
        #     plt.plot(hist.history['val_loss'], label ='val loss')
        #     plt.xlabel('Epoch')
        #     plt.ylabel('Loss')
        #     plt.ylim([0, 2])
        #     plt.legend(loc='lower left')
            
        #     plt.show()