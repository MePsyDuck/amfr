import os

import cv2

from facial_recog.app.config import cascade_dir, default_method


def detect_face(img, class_id):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    classifier_loc = cascade_dir[default_method] + class_id + '.xml'

    if not os.path.exists(classifier_loc):
        print("Classifier not found for " + class_id)

    face_cascade = cv2.CascadeClassifier(classifier_loc)
    faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.2, minNeighbors=5)

    if len(faces) == 0:
        return None, None

    (x, y, w, h) = faces[0]

    return gray[y:y + w, x:x + h], faces[0]
