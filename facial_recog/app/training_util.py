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
        subject_dir_path = cascade_dir[detect_method] + os.pathsep + subject
        subject_images = os.listdir(subject_dir_path)

        if subject_images in None:
            print("No images found for subject: " + subject)
        else:
            for image_name in subject_images:
                if image_name.startswith("."):
                    continue

                image_path = subject_dir_path + "/" + image_name
                image = cv2.imread(image_path)

                face, rect = detect_face(img=image, class_id=class_id)

                if face is not None:
                    faces.append(face)
                    labels.append(subject)

    return faces, subjects
