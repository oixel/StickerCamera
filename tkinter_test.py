#
# ⚠️ If PIL import fails to work run the following command: "pip install pillow" in your terminal.
#
from tkinter import *
from PIL import Image, ImageTk
import cv2
import os

# Renders what the camera views onto the camera_view object in application.
def render_camera():
    # Converts image to rgb format
    rgb_image = cv2.cvtColor(capture.read()[1], cv2.COLOR_BGR2RGB)

    # Creates a renderable Image object from camera's capture
    frame = Image.fromarray(rgb_image)

    # Converts the renderable frame into the proper format for rendering on tkinter's label
    photo_image = ImageTk.PhotoImage(image = frame)

    # Reassigns the camera_view widget's to the most recent rendered frame (in imgtk format)
    camera_view.imgtk = photo_image
    camera_view.configure(image = photo_image)

    # Calls the render_camera() function again after 20 milliseconds -- creating a loop
    camera_view.after(20, render_camera)

# Takes a picture and stores it in the files; called when "Take Picture" button is pressed
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

# Initializes a video camera; 0 opens the default camera
capture = cv2.VideoCapture(0)

# Sets the dimensions of the camera's output--scaling the application's window size in the process
WIDTH, HEIGHT = 800, 250
capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

# Creates a tkinter application and renames the window to "Sticker Camera"
application = Tk()
application.winfo_toplevel().title("Sticker Camera")

# Prevents the window from being resized or full-screened
application.resizable(False, False)

# Camera view is the box at the top of the application which holds the camera's view being rendered
camera_view = Label(application)
camera_view.pack()

# Creates a button with text that says "Take Picture" that runs the take_picture() function
picture_button = Button(application, text="Take Picture",
                command = take_picture)

# Creates a button with text that says "Quit" that closes the application when it is pressed
close_button = Button(application, text = "Quit",
                command = application.quit)

# Places the buttons on the bottom center and bottom right of the screen using tkinter's pack method
picture_button.pack()
close_button.pack(side = "right")

# Calls render_camera() for the first time to start the loop
render_camera()

# Built-in tkinter function that keeps the application running until it is closed by some means
application.mainloop()