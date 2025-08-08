import os
import cv2

# ===== Read webcam =====
# The parameter 0 indicates the default webcam (usually built-in)
# To use a different camera, change the number (1, 2, etc.)
# You can also use a string with an IP camera URL instead of a number
webcam = cv2.VideoCapture(0)

# Check if webcam was opened successfully
if not webcam.isOpened():
    print("Error: Could not open webcam")
    exit()

# ===== Visualize webcam =====
# This loop will run until 'q' is pressed
while True:
    # Read a frame from the webcam
    # ret: Boolean indicating if frame was successfully read (True/False)
    # frame: The actual image data if ret is True
    ret, frame = webcam.read()
    
    # Check if frame was successfully read
    if not ret:
        print("Error: Failed to capture frame")
        break
        
    # There's a typo in the original - it should be imshow not imgshow
    # 'frame' is the window name - you can change this to anything
    cv2.imshow('frame', frame)
    
    # The original condition has syntax errors. The correct version is:
    # Wait for 40ms (about 25 FPS) and check if 'q' key was pressed
    # 0xFF is used to get the last 8 bits, which is important on some systems
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

# ===== Clean up =====
# Always release the webcam and destroy all windows when done
webcam.release()
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

# ===== Glossary =======

# The ret variable tells you if a frame was successfully captured:

# ret = True means the frame was successfully captured, and frame contains valid image data
# ret = False means the operation failed - which could happen if:

# You've reached the end of a video file
# The webcam is disconnected
# There was some other error reading from the video source