import cv2

def resize_image(image, new_size):
    resized_image = cv2.resize(image, new_size)
    return resized_image

# Example usage
image = cv2.imread("../images/damage.webp")
resized_image = resize_image(image, (224, 224))
