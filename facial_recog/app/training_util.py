import os

import cv2

from facial_recog.app.classifier_util import get_class_subjects
from facial_recog.app.config import cascade_dir, default_method
from facial_recog.app.face_detection import detect_face


def prepare_training_data(class_id):
    faces = []
    labels = []
    subjects = get_class_subjects(class_id)

    for subject in subjects:
        subject_dir_path = cascade_dir[default_method] + os.pathsep + subject
        subject_images = os.listdir(subject_dir_path)

        for image_name in subject_images:
            if image_name.startswith("."):
                continue

            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)

            cv2.imshow("Training on image...", image)
            cv2.waitKey(100)

            face, rect = detect_face(img=image, class_id=class_id)

            if face is not None:
                faces.append(face)
                labels.append(subject)

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()

    return faces, subjects
