import cv2
import numpy as np
import time
import os

output_directory = "training/dataset"
non_dark_threshold = 40


def current_milli_time():
    return round(time.time() * 1000)


def return_camera_indexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr


def capture_non_dark_images(camera_index):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        time.sleep(0.5)
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('frame', frame)
        if np.average(frame) > non_dark_threshold:
            cv2.imwrite(output_directory + str(current_milli_time()) + ".jpg", frame)


def main():
    camera_indexes = return_camera_indexes()
    capture_non_dark_images(camera_indexes[1])


if __name__ == "__main__":
    exit(main())
    