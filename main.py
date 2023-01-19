from productive_image_downloader import download_rand_image
from unproductive_image_downloader import download_youtube_frames

download_rand_image(delete_images=False, num_to_download=0, image_width=1000, image_height=625)
download_youtube_frames(delete_frames=True, frames_needed=1000, link="https://www.youtube.com/watch?v=IvuefbvVmcI")