#
# pip install pillow
#
from tkinter import *
from PIL import Image, ImageTk
import cv2
import os

def render_camera():
    rgb_image = cv2.cvtColor(capture.read()[1], cv2.COLOR_BGR2RGB)

    frame = Image.fromarray(rgb_image)

    photo_image = ImageTk.PhotoImage(image = frame)

    widget.imgtk = photo_image
    widget.configure(image = photo_image)

    widget.after(20, render_camera)

def take_picture():
    # Sets the picture count to however many photos there are in the pictures folder + 1 to prevent overlapping of picture names
    files = os.listdir("pictures/")
    pic_count = len(files) + 1

    # Creates a string with the proper count of pictures taken to be used as the name
    pic_name = "pictures/picture_{}.png".format(pic_count)

    # Writes currently rendered image to path given in name!
    cv2.imwrite(pic_name, capture.read()[1])

    # Output message to inform what number picture this is
    print(f"Picture {pic_count} taken!")

capture = cv2.VideoCapture(0)

WIDTH, HEIGHT = 500, 250
capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

application = Tk()

widget = Label(application)
widget.pack()

picture_button = Button(application, text="Take Picture",
                command = take_picture)

close_button = Button(application, text = "Quit",
                command = application.quit)

picture_button.pack()
close_button.pack()

render_camera()

application.mainloop()