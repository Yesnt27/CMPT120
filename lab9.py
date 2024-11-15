#lab 9 featuring a car image

import cmpt120images

car = cmpt120images.get_image('images/mercedes AMG.jpg')
green = cmpt120images.get_image("images/colorgreen.jpg")


def find_length(image):
    return len(image[0]) #this returns the first column of the image, hence the amount of pixels it has sideways

def change_boarder(image):
    height = len(image)
    width = len(image[0])
    border = 5
    border_color = [65,45,240]
    for row in range(height):
        for col in range(width):
            if row < border or row >= height-border or col >= width-border or col < border :
                image[row][col] = border_color
    cmpt120images.show_image(image,"Hello world")

# def is_green(r, g, b):
#     return True

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


def change_background(image):
    
    height = len(image)
    width = len(image[0])
    white = [255,255,255]
    gray = [128,128,128]

    for row in range(height):
        if (row // 15 %2==0):
            band_color = white
        else:
            band_color = gray
        
        for col in range(width):
            pixel = is_pixel_green(image[row][col])
            if(pixel):
                    image[row][col] = band_color
               
                
    cmpt120images.show_image(image,"Hello world")

def grid(image):
    
    height = len(image)
    width = len(image[0])
    white = [255,255,255]
    gray = [128,128,128]

    for row in range(height):
        if (row // 15 %2==0):
            band_color = white
        else:
            band_color = gray
        
        for col in range(width):
            if (col // 15 %2==0):
                band_color = white
            else:
                band_color = gray
            pixel = is_pixel_green(image[row][col])
            if(pixel):
                    image[row][col] = band_color
                    image[col][row] = band_color
                
    cmpt120images.show_image(image,"Hello world")


def main():
    print(f"Image size {find_length(car)}x{len(car)}") #len(car) returns the total amount of rows in 
    #the whole image from top to bottom similar to a data file
    change_boarder(car)
    cmpt120images.wait_for_escape()
    change_background(green)
    cmpt120images.wait_for_escape()
    grid(green)
    cmpt120images.wait_for_escape()
    
    




    
main()



