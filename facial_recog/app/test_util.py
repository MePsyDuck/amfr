import os
import random
import shutil

from .config import training_dir, recog_dir
from .db_util import add_subject_to_class


def copy_dataset(fdb_loc, subject_names, image_count):
    for subject in subject_names:
        subject_dir = os.path.join(training_dir, str(subject))
        subject_images = get_images_for_subject(fdb_loc=fdb_loc, subject_name=subject_names[subject])
        sample_images = random.sample(subject_images, image_count)

        if not os.path.exists(subject_dir):
            os.makedirs(subject_dir)

        for image in sample_images:
            shutil.copy(image, subject_dir)


def populate_db(subject_classes):
    for subject_id in subject_classes:
        add_subject_to_class(subject_id, subject_classes[subject_id])


def create_sample(fdb_loc, subject_count, class_count):
    subdir = os.path.join(fdb_loc, 'male')
    all_subjects = os.listdir(os.path.join(fdb_loc, subdir))

    sample_subjects = random.sample(all_subjects, subject_count)
    sample_ids = random.sample(range(subject_count * 10), subject_count)
    sample_classes = [random.randint(1, class_count) for _ in range(subject_count)]
    subject_names = dict(zip(sample_ids, sample_subjects))
    subject_classes = dict(zip(sample_ids, sample_classes))

    return subject_names, subject_classes


def clear_dataset():
    try:
        shutil.rmtree(training_dir)
    except FileNotFoundError:
        pass


def get_images_for_subject(fdb_loc, subject_name):
    subject_images = []

    subject_dir = os.path.join(fdb_loc, 'male', subject_name)

    for image in os.listdir(subject_dir):
        subject_images.append(os.path.join(subject_dir, image))

    return subject_images


def clear_recognizers():
    for subdir in recog_dir:
        try:
            shutil.rmtree(recog_dir[subdir])
        except FileNotFoundError:
            pass
        os.mkdir(recog_dir[subdir])
