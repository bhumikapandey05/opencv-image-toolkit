import cv2
import matplotlib.pyplot as plt
from image_toolkit import *

def main():
    image = load_image('images/dog.jpg')
    grayscale_image = convert_to_grayscale(image)
    resized_image = resize_image(grayscale_image, width=300)
    cropped_image = crop_image(resized_image, 50, 50, 250, 250)
    display_image(cropped_image, title="Processed Dog Image")
    save_image(cropped_image, 'output/dog_processed.jpg')
    flipped_image = flip_image(cropped_image, flip_code=1)
    display_image(flipped_image, title="Flipped Dog Image")
    rotated_image = rotate_image(flipped_image, angle=45)
    display_image(rotated_image, title="Rotated Dog Image")
    blurred_image = apply_gaussian_blur(rotated_image, kernel_size=(5, 5))
    display_image(blurred_image, title="Blurred Dog Image")
    edges = apply_canny_edge_detection(blurred_image, threshold1=100, threshold2=200)
    display_image(edges, title="Canny Edges Dog Image")
    thresholded_image = apply_threshold(edges, threshold_value=127, max_value=255)
    display_image(thresholded_image, title="Thresholded Dog Image")

if __name__ == "__main__":
    main()