import os
import random
import unittest

import cv2

from .db_util import recreate_db
from .face_recognition import predict
from .log import setup_logger
from .test_util import create_sample, populate_db, clear_dataset, copy_dataset, get_images_for_subject
from .trainer import train
from .util import get_class_subjects


class TestFR(unittest.TestCase):
    subject_names = dict()
    subject_classes = dict()
    sub_count = 10
    class_count = 2
    image_count = 10
    imfdb_loc = os.path.join('c:\\', 'imfdb_final')

    def setUp(self):
        setup_logger()
        self.subject_names, self.subject_classes = create_sample(imfdb_loc=self.imfdb_loc, subject_count=self.sub_count,
                                                                 class_count=self.class_count)

        recreate_db()
        populate_db(self.subject_classes)

        clear_dataset()
        copy_dataset(imfdb_loc=self.imfdb_loc, subject_names=self.subject_names, image_count=self.image_count)

        for class_id in range(self.class_count):
            train(class_id=class_id)

    def test_fr(self):
        random_class = random.choice(range(self.class_count))
        random_subject = random.choice(get_class_subjects(random_class))
        random_image = random.choice(
            get_images_for_subject(imfdb_loc=self.imfdb_loc, subject_name=self.subject_names[random_subject]))

        self.assertEqual(predict(img=cv2.imread(random_image), class_id=random_class), random_subject)


if __name__ == '__main__':
    unittest.main()
