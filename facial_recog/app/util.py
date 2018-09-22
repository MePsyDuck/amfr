import logging
import os

import cv2

from .config import recog_method, db_dir, log_dir, cascade_dir, detect_method, recog_dir, training_dir
from .db_util import all_subjects_for_class, all_classes


def get_recognizer():
    logging.info('Getting recognizer for %s', recog_method)
    face_recognizer = None
    if recog_method == 'lbph':
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    elif recog_method == 'eigen':
        face_recognizer = cv2.face.EigenFaceRecognizer_create()
    elif recog_method == 'fisher':
        face_recognizer = cv2.face.FisherFaceRecognizer_create()
    else:
        logging.critical('Recognition method %s not valid', recog_method)
    return face_recognizer


def get_class_subjects(class_id):
    return [i[0] for i in all_subjects_for_class(class_id)]


def get_all_classes():
    return [i[0] for i in all_classes()]


def rgb_to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def create_app_dirs():
    if not os.path.exists(db_dir):
        os.mkdir(db_dir)

    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    if not os.path.exists(cascade_dir[detect_method]):
        os.mkdir(cascade_dir[detect_method])

    if not os.path.exists(recog_dir[recog_method]):
        os.mkdir(recog_dir[recog_method])

    if not os.path.exists(training_dir):
        os.mkdir(training_dir)
