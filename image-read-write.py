import os
import cv2  # Make sure to import cv2 library

# ===== Read an image =====
# Replace 'new-folder' with your actual folder name
# Replace 'image-example.jpg' with your actual image filename
image_path = os.path.join('.', 'new-folder', 'image-example.jpg')

# This loads the image from the path
# If the image can't be found, img will be None
img = cv2.imread(image_path)

# Always good to add a check to see if image was loaded successfully
if img is None:
    print("Error: Could not read image")
    exit()

# ===== Write an image =====
# Replace 'new-folder' with your desired output folder
# Replace 'image-example-1.jpg' with your desired output filename
# The second parameter (img) is the image data to save
cv2.imwrite(os.path.join('.', 'new-folder', 'image-example-1.jpg'), img)

# ===== Visualize an image =====
# The first parameter ('image') is the window name - you can change this to anything
# The second parameter (img) is the image data to display
cv2.imshow('image', img)

# waitKey(0) means wait indefinitely until a key is pressed
# Replace 0 with a number (milliseconds) to wait that amount of time:
# - waitKey(1000) = wait 1 second
# - waitKey(5000) = wait 5 seconds
# - waitKey(0) = wait until key press
# The return value is the ASCII code of the key pressed or -1 if no key was pressed
key = cv2.waitKey(0)

# Always destroy all windows when done
cv2.destroyAllWindows()

# ===== Frame Rate Reference Table =====
# | Frame Rate (FPS) | Milliseconds (ms) |
# |------------------|-------------------|
# | 60 FPS           | 16.7 ms           |
# | 50 FPS           | 20 ms             |
# | 30 FPS           | 33.3 ms           |
# | 25 FPS           | 40 ms             |
# | 24 FPS           | 41.7 ms           |
# | 20 FPS           | 50 ms             |
# | 15 FPS           | 66.7 ms           |
# | 10 FPS           | 100 ms            |
# | 5 FPS            | 200 ms            |
# | 1 FPS            | 1000 ms           |
# Formula: Milliseconds = 1000 / Frames Per Second