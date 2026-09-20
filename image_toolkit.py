import cv2
from matplotlib import pyplot as plt
import numpy as np

def load_image(image_path):
   image = cv2.imread(image_path)
   if image is None:
      raise FileNotFoundError(f"Image not found at path: {image_path}")
   return image

def convert_to_grayscale(image):
   return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def resize_image(image, width=None, height=None):
   if width is None and height is None:
      return image

   (h, w) = image.shape[:2]
   if width is not None:
      r = width / float(w)
      dim = (width, int(h * r))
   else:
      r = height / float(h)
      dim = (int(w * r), height)

   resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
   return resized_image

def save_image(image, output_path):
   cv2.imwrite(output_path, image)
   print(f"Image saved at: {output_path}")

def display_image(image, title="Image"):
   plt.imshow(image, cmap='gray')
   plt.title(title)
   plt.axis('off')
   plt.show()

def crop_image(image, start_x, start_y, end_x, end_y):
   return image[start_y:end_y, start_x:end_x]

def flip_image(image, flip_code):
   return cv2.flip(image, flip_code)

def rotate_image(image, angle):
   (h, w) = image.shape[:2]
   center = (w // 2, h // 2)
   M = cv2.getRotationMatrix2D(center, angle, 1.0)
   rotated_image = cv2.warpAffine(image, M, (w, h))
   return rotated_image 

def apply_gaussian_blur(image, kernel_size=(5, 5)):
   return cv2.GaussianBlur(image, kernel_size, 0)

def apply_canny_edge_detection(image, threshold1, threshold2):
   return cv2.Canny(image, threshold1, threshold2)

def apply_threshold(image, threshold_value, max_value, threshold_type=cv2.THRESH_BINARY):
   _, thresholded_image = cv2.threshold(image, threshold_value, max_value, threshold_type)
   return thresholded_image