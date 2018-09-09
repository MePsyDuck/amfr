import os
import random
import shutil

from .config import training_dir
from .db_util import add_subject_to_class


def copy_dataset(imfdb_loc, subject_names, image_count):
    for subject in subject_names:
        subject_dir = os.path.join(training_dir, str(subject))
        subject_images = get_images_for_subject(imfdb_loc=imfdb_loc, subject_name=subject_names[subject])
        sample_images = random.sample(subject_images, image_count)

        if not os.path.exists(subject_dir):
            os.makedirs(subject_dir)

        for image in sample_images:
            shutil.copy(image, subject_dir)


def populate_db(subject_classes):
    for subject_id in subject_classes:
        add_subject_to_class(subject_id, subject_classes[subject_id])


def create_sample(imfdb_loc, subject_count, class_count):
    all_subjects = os.listdir(imfdb_loc)
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


def get_images_for_subject(imfdb_loc, subject_name):
    subject_movies = []
    for movie in os.listdir(os.path.join(imfdb_loc, subject_name)):
        if os.path.isdir(os.path.join(imfdb_loc, subject_name, movie)):
            subject_movies.append(movie)

    subject_images = []

    for movie in subject_movies:
        for image in os.listdir(os.path.join(imfdb_loc, subject_name, movie, 'images')):
            subject_images.append(os.path.join(imfdb_loc, subject_name, movie, 'images', image))

    return subject_images
