import logging
import os

import cv2

from .config import cascade_dir, detect_method
from .face_detection import detect_face
from .util import get_class_subjects


def prepare_training_data(class_id):
    faces = []
    labels = []
    subjects = get_class_subjects(class_id)

    for subject in subjects:
        subject_loc = os.path.join(cascade_dir[detect_method], subject)
        subject_images = os.listdir(subject_loc)

        if subject_images in None:
            logging.critical('No images found for subject %s', str(subject))
        else:
            logging.info('Found %d images for subject %s', len(subject_images), str(subject))
            for image_name in subject_images:
                if image_name.startswith('.'):
                    logging.debug('Ignoring file %s', image_name)
                    continue

                image_loc = os.path.join(subject_loc, image_name)
                image = cv2.imread(image_loc)

                face, rect = detect_face(img=image, class_id=class_id)

                if face is not None:
                    logging.debug('Adding face found with label %s', str(subject))
                    faces.append(face)
                    labels.append(subject)
                else:
                    logging.warning('No faces found for subject %s in image %s', str(subject), image_name)

    return faces, subjects
