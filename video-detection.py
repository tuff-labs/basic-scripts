import os
import cv2

# This creates a path to a video file. Replace 'folder-name' with your folder and replace 'example-video.mp4' with video

video_path = os.path.join('.', 'folder-name', 'example-video.mp4')

# Opens the video file and creates a video capture object that will let you read frames from the video.
video = cv2.VideoCapture(video_path)

# This initalizes a variable ret to true. This will be used to track if we successfully read a frame.
ret = True

# This starts a loop that will continue as long as the ret variable is set to true. Meaning we can stil read frames from the video.
while ret: 
    # This reads the next frame the video. Ret will be tue if a frame was successfully read. False if we've reached the end of the video. Frame will contain the actual image data.
    ret, frame = video.read()
    # check if frame was successfully read
    if ret: 
        # This displays the current frame in a widow title frame
        cv2:imshow('frame', frame)

        # This waits for 40 millieseconds before continuing. This controls the playback speed of the video. (25 frames per second would approxmiately 40ms per frame.)
        cv2.waitKey(40)

        video.release()
        cv2.destroyAllWindows()

        # After the loop ends (when we've reached the end of the video these lines release the video file resources) and close all CV windows


        #Key for millieseconds 
       
       # Frame Rate Reference Table
# -------------------------
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
# -------------------------
# Formula: Milliseconds = 1000 / Frames Per Second
# Use in cv2.waitKey(milliseconds)
