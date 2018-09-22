import os
import random
import shutil
import zipfile

import wget

from facial_recog.app import training_dir, recog_dir, add_subject_to_class
from .test_config import image_count, fdb_loc, subject_count, class_count, test_src_dir, fdb_urls, fdb_file, fdb_name


def copy_dataset(subject_names):
    for subject in subject_names:
        subject_dir = os.path.join(training_dir, str(subject))
        subject_images = get_images_for_subject(subject_name=subject_names[subject])
        sample_images = random.sample(subject_images, image_count)

        if not os.path.exists(subject_dir):
            os.makedirs(subject_dir)

        for image in sample_images:
            shutil.copy(image, subject_dir)


def populate_db(subject_classes):
    for subject_id in subject_classes:
        add_subject_to_class(subject_id, subject_classes[subject_id])


def create_sample():
    all_subjects = os.listdir(os.path.join(fdb_loc, fdb_name))

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


def get_images_for_subject(subject_name):
    subject_images = []

    subject_dir = os.path.join(fdb_loc, fdb_name, subject_name)

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


def download_fdb():
    wget.download(fdb_urls[fdb_name], fdb_file)
    unzip_fdb()


def unzip_fdb():
    with zipfile.ZipFile(fdb_file, "r") as zip_file:
        zip_file.extractall(fdb_loc)


def prepare_fdb():
    if not os.path.exists(test_src_dir):
        os.mkdir(test_src_dir)

    if len(os.listdir(test_src_dir)) == 0:
        download_fdb()


def clear_fdb():
    try:
        shutil.rmtree(test_src_dir)
    except FileNotFoundError:
        pass
