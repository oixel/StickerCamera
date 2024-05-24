#
# ⚠️ NOTE: If you have not installed OpenCV, run the command "pip install opencv-python" in your terminal
#
# 📸 Controls for Camera:
#     SPACE :: Take a picture*
#     ESC :: Exit camera
#
# * = All pictures taken can be found in pictures folder
#

# Imports needed libraries
import cv2
import os

# Stores what camera sees and outputs it to window
def render_camera():
    # Dumps unneeded return and then stores current image into variable
    _, image = camera.read()

    # Renders camera on screen with window named "Photo Camera"
    cv2.imshow("Photo Camera", image)

    # Returns image so that variable assignment can occur in loop
    return image

# Initializes a video camera; 0 opens the default camera
camera = cv2.VideoCapture(0)

# Initialize camera so the loop can run
render_camera()

# Makes a folder named pictures if it does not currently exist
if not os.path.isdir("pictures"):
    os.mkdir("pictures")

# Sets the picture count to however many photos there are in the pictures folder to prevent overlapping of picture names
files = os.listdir("pictures/")
pic_count = len(files)

# Print empty line for cleaner terminal outputs
print()

# Runs as long as the window is not closed by user (by pressing 'X' in top right)
while cv2.getWindowProperty('Photo Camera', cv2.WND_PROP_VISIBLE) >= 1:
    # Update window to show what camera sees every loop and stores image being rendered
    image = render_camera()

    # Stores any key that is pressed
    key = cv2.waitKey(1)

    # Closes camera when 'ESC' key is pressed on keyboard
    if key % 256 == 27:
        break

    # Detects if 'SPACE' bar is pressed
    if key % 256 == 32:
        # Increment the count of pictures taken
        pic_count += 1

        # Creates a string with the proper count of pictures taken to be used as the name
        pic_name = "pictures/picture_{}.png".format(pic_count)

        # Writes currently rendered image to path given in name!
        cv2.imwrite(pic_name, image)

        # Output message to inform what number picture this is
        print(f"Picture {pic_count} taken!")

# Prints a final farewell when loop finally closes
print("Goodbye!\n")