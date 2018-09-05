from os.path import pathsep

from .config import recog_dir, recog_method
from .face_detection import detect_face
from .util import get_recognizer


def predict(img, class_id):
    face, rect = detect_face(img=img, class_id=class_id)
    face_recognizer = get_recognizer()
    face_recognizer.load(recog_dir[recog_method] + pathsep + class_id + ".xml")
    label, confidence = face_recognizer.predict(face)
    return label, confidence
