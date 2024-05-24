import cv2

# Stores what camera sees and outputs it to window
def render_camera():
    # Dumps unneeded return and then stores current image into variable
    _, image = camera.read()

    # Renders camera on screen with window named "Photo Camera"
    cv2.imshow("Photo Camera", image)

# Initializes a video camera; 0 opens the default camera
camera = cv2.VideoCapture(0)

# Initialize camera so the loop can run
render_camera()

# Runs as long as the window is not closed by user (by pressing 'X' in top right)
while cv2.getWindowProperty('Photo Camera', cv2.WND_PROP_VISIBLE) >= 1:
    # Update window to show what camera sees every loop
    render_camera()

    # Stores any key that is pressed
    key = cv2.waitKey(1)

    # Closes camera when 'ESC' key is pressed on keyboard
    if key % 256 == 27:
        print("Goodbye!")
        break

    # Detects if 'SPACE' bar is pressed
    if key % 256 == 32:
        print("Say Cheese!")