import logging
import os

from .config import recog_dir, recog_method
from .face_detection import detect_faces
from .util import get_recognizer


def predict(img, class_id):
    recognizer_loc = os.path.join(recog_dir[recog_method], class_id + ".xml")
    logging.info('Using recognizer %s', recognizer_loc)
    face = detect_faces(img=img)
    face_recognizer = get_recognizer()
    face_recognizer.load(recognizer_loc)
    label, confidence = face_recognizer.predict(face)
    logging.info('Predicted %s with confidence %s', str(label), str(confidence))
    return label, confidence
