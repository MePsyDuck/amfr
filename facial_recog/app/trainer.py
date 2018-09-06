import os

import numpy as np

from .config import recog_method, recog_dir
from .training_util import prepare_training_data
from .util import get_recognizer


def trainer(class_id):
    recognizer_loc = os.path.join(recog_dir[recog_method], class_id + ".xml")
    face_recognizer = get_recognizer()
    faces, labels = prepare_training_data(class_id)
    face_recognizer.train(faces, np.array(labels))
    face_recognizer.save(recognizer_loc)