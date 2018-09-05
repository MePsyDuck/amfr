from os.path import pathsep

import numpy as np

from .config import recog_method, recog_dir
from .training_util import prepare_training_data
from .util import get_recognizer


def trainer(class_id):
    face_recognizer = get_recognizer()
    faces, labels = prepare_training_data(class_id)
    face_recognizer.train(faces, np.array(labels))
    face_recognizer.save(recog_dir[recog_method] + pathsep + class_id + ".xml")
