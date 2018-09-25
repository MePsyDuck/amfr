import logging
import os

from .config import recog_dir, recog_method, confidence_threshold
from .face_detection import detect_face
from .util import get_recognizer


def predict(img, class_id):
    recognizer_loc = os.path.join(recog_dir[recog_method], str(class_id) + ".xml")
    logging.info('Using recognizer %s', recognizer_loc)
    face = detect_face(img=img)
    if face is not None:
        face_recognizer = get_recognizer()
        face_recognizer.read(recognizer_loc)
        label, confidence = face_recognizer.predict(face)
        logging.info('Predicted %s with confidence %s', str(label), str(confidence))
        if confidence < confidence_threshold:
            logging.info('Subject belongs to the class')
            return label
        else:
            logging.info('Subject does not belong to the class')
            return None
    else:
        logging.critical('No face detected, cannot predict')
        return None
