# TODO: Your header

import cmpt120image

def recolor_image(img, color):
  # TODO: Add your code here
  
  img2=cmpt120image.get_black_image(len(img),len(img[0]))
  for rows in range(len(img)):
    for cols in range(len(img[0])):
      if img[rows][cols][0] < 240 or img[rows][cols][1] < 240 or img[rows][cols][2] < 240:
        img2[rows][cols] == color
      else:
        img2[rows][cols] == img[rows][cols]
  return img2

def minify(img):
  # TODO: Add your code here
  pass
  
def mirror(img):
  # TODO: Add your code here
  pass
  
def draw_item(canvas, img, row, col):
  # TODO: Add your code here
  pass
  
def distribute_items(canvas, img, n):
  # TODO: Add your code here
  pass

apple = cmpt120image.get_image('images/apples.png')
recolor_image(apple,[12,200,40])

cmpt120image.wait_for_escape()