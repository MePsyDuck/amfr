import logging
import os

import cv2

from .config import training_dir
from .face_detection import detect_face
from .util import get_class_subjects


def prepare_training_data(class_id):
    all_faces = []
    all_labels = []
    subjects = get_class_subjects(class_id)

    for subject in subjects:
        subject_loc = os.path.join(training_dir, str(subject))
        subject_images = os.listdir(subject_loc)

        if subject_images is None:
            logging.critical('No images found for subject %s', str(subject))
        else:
            logging.info('Found %d images for subject %s', len(subject_images), str(subject))
            for image_name in subject_images:
                if image_name.startswith('.'):
                    logging.debug('Ignoring file %s', image_name)
                    continue

                image_loc = os.path.join(subject_loc, image_name)
                image = cv2.imread(image_loc)

                face = detect_face(img=image)

                if face is not None:
                    logging.debug('Adding face found in image %s with label %d', image_name, subject)
                    all_faces.append(face)
                    all_labels.append(subject)

                else:
                    logging.warning('No faces found in image %s for label %d', image_name, subject)

    return all_faces, all_labels
