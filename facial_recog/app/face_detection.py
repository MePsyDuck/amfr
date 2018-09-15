import logging
import os

import cv2

from .config import cascade_dir, detect_method, cascade


def detect_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cascade_loc = os.path.join(cascade_dir[detect_method], cascade[detect_method])
    face_cascade = cv2.CascadeClassifier(cascade_loc)
    faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=1)

    if len(faces) == 0:
        logging.warning('No faces found in image')
        return None
    else:
        logging.info('%d faces found')
        return faces
