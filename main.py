from productive_image_downloader import download_rand_image
from unproductive_image_downloader import download_youtube_frames
from PIL import Image
from cnn import convolutional_neural_network
import os

delete_images = False
images_needed = 0
total_images = len(os.listdir('productive_images')) + len(os.listdir('unproductive_images'))
save_model = True
load_model = False
num_train = 1500
num_test = 500
epochs = 20

download_youtube_frames(delete_frames=delete_images, frames_needed=images_needed)
img = Image.open("unproductive_images/frame1.jpg")
img_width = img.width
img_height = img.height

download_rand_image(delete_images=delete_images, num_to_download=images_needed, image_width=img_width, image_height=img_height)

# img2 = Image.open("productive_images/image1.jpg")
# if (img2.height==img_height and img2.width==img_width):
#     print("\nIMAGE SIZES SAME\n")

cnn = convolutional_neural_network(img_height, img_width)
cnn.run(save_model=save_model, load_model=load_model, num_train=num_train, num_test=num_test, epochs=epochs)