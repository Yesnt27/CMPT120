# TODO: Your header
import random
import cmpt120image

def recolor_image(img, color):
  # TODO: Add your code here
  
  img2=cmpt120image.get_black_image(len(img),len(img[0]))
  for rows in range(len(img)):
    for cols in range(len(img[0])):
      if img[rows][cols][0] < 240 or img[rows][cols][1] < 240 or img[rows][cols][2] < 240:
        img2[rows][cols] = color
      else:
        img2[rows][cols] = img[rows][cols]
  return img2

def minify(img):
  # TODO: Add your code here
  pass
  
def mirror(img):
  img2=cmpt120image.get_black_image(len(img),len(img[0]))
  for rows in range(len(img)):
    for cols in range(len(img[0])):
      if img[rows][cols][0] < 240 or img[rows][cols][1] < 240 or img[rows][cols][2] < 240:
        img[cols][rows] = img2[cols][(len(img)) - rows - 1]

  return img2
  
def draw_item(canvas, img, row, col):

  for rows in range(len(img)):
    for cols in range(len(img[0])):
      #if img is non-white
      if img[rows][cols][0] < 240 or img[rows][cols][1] < 240 or img[rows][cols][2] < 240:
        canvas[rows+row][cols+col] = img[rows][cols]
  return canvas
  
def distribute_items(canvas, img, n):
  for i in range(n):
    row = random.randint(0,(len(canvas)-len(img)))
    col = random.randint(1,(len(canvas[0])-len(img[0])))
    draw_item(canvas,img,row,col)
  return canvas
  


# apple = cmpt120image.get_image('images/apples.png')
# recolor_image(apple,[12,200,40])
# cmpt120image.show_image(draw_item(apple),"yessir")
# cmpt120image.wait_for_escape() 
