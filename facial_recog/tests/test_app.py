import unittest

import cv2

from facial_recog.app import setup_logger, recreate_db, get_all_classes, train, get_class_subjects, predict
from .test_util import *


class TestFR(unittest.TestCase):
    subject_names = dict()
    subject_classes = dict()

    def setUp(self):
        setup_logger()

        # only for super strict testing
        # clear_fdb()
        prepare_fdb()

        self.subject_names, self.subject_classes = create_sample()

        recreate_db()
        populate_db(self.subject_classes)

        clear_dataset()
        copy_dataset(subject_names=self.subject_names)

        clear_recognizers()

        for class_id in get_all_classes():
            train(class_id=class_id)

    def test_fr(self):
        random_class = random.choice(get_all_classes())
        random_subject = random.choice(get_class_subjects(random_class))
        random_image = random.choice(
            get_images_for_subject(subject_name=self.subject_names[random_subject]))

        self.assertEqual(predict(img=cv2.imread(random_image), class_id=random_class), random_subject)


if __name__ == '__main__':
    unittest.main()
