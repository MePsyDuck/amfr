import logging
import os

import cv2

from .config import cascade_dir, detect_method, cascade
from .util import rgb_to_gray


def detect_faces(img):
    gray = rgb_to_gray(img=img)

    cascade_loc = os.path.join(cascade_dir[detect_method], cascade[detect_method])
    face_cascade = cv2.CascadeClassifier(cascade_loc)
    faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=1)

    if len(faces) == 0:
        logging.warning('No faces found in image')
        return None
    else:
        logging.info('%d faces found', len(faces))
        face_imgs = []
        for face in faces:
            x, y, w, h = [v for v in face]
            face_imgs.append(rgb_to_gray(img[y:y + h, x:x + w]))
        return face_imgs


def detect_face(img):
    if detect_faces(img=img) is not None:
        return detect_faces(img=img)[0]
    else:
        return None
