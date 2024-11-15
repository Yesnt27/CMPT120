# Check if a pixel is green

# Import custom module for image processing
import cmpt120images

# def is_green(r, g, b):
#     return True
import cmpt120images
# Return true when green is within 30 of 255
# and red and blue are within 30 of 0
def is_pixel_green(pixel):
    THRESHOLD = 74
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    # if r < THRESHOLD and g > 255 - THRESHOLD and b < THRESHOLD:
    #     return True
    # else:
    #     return False
    low_red = r < THRESHOLD
    high_green = g > 255 - THRESHOLD
    low_blue = b < THRESHOLD
    return low_red and high_green and low_blue

# Main program
# --------------------------------------------------

# Load images
img = cmpt120images.get_image('images/green_computer.jpg')

pixel = img[60][200]
# print(is_green(pixel[0], pixel[1], pixel[2]))
print(is_pixel_green(pixel))