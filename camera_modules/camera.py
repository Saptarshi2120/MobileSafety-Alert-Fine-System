# from imutils.video import VideoStream
# import imutils
# import os, urllib.request
import cv2


class webcam:
    def __getframetime(fps) -> int:
        if fps >= 1000 or fps <= 0:
            return 1
        timing = int(1000 / fps)
        return timing

    def __init__(self, fps=30) -> None:
        self.video = cv2.VideoCapture(0)
        self.frametime = webcam.__getframetime(fps)

    # bad practice! to handle it use try finally to release()
    def __del__(self) -> None:
        self.video.release()


    def get_frame(self):
        success, frames = self.video.read()
        cv2.waitKey(self.frametime)
        # convert the all image to gray so model is efficient
        # gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        # send all the image info to model on !!frames!!

        # flipping the image
        frame_flip = cv2.flip(frames, 1)
        ret, jpeg = cv2.imencode(".jpg", frame_flip)

        return jpeg.tobytes()
