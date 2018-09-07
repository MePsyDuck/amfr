import logging
import os

import cv2

from .config import cascade_dir, detect_method


def detect_face(img, class_id):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cascade_loc = os.path.join(cascade_dir[detect_method], class_id + '.xml')
    face_cascade = cv2.CascadeClassifier(cascade_loc)
    faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.2, minNeighbors=5)

    if len(faces) == 0:
        logging.warning('No faces found in image')
        return None, None
    else:
        logging.info('%d faces found')
        (x, y, w, h) = faces[0]
        return gray[y:y + w, x:x + h], faces[0]
