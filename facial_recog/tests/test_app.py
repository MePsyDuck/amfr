import unittest

from facial_recog.app import *
from .test_config import test_run_count, seed, success_perc
from .test_util import *


class TestFR(unittest.TestCase):
    subject_names = dict()
    subject_classes = dict()

    def setUp(self):
        random.seed(seed)

        create_app_dirs()
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
        success = 0
        for _ in range(test_run_count):
            random_class = random.choice(get_all_classes())
            random_subject = random.choice(get_class_subjects(random_class))
            random_image = random.choice(
                get_images_for_subject(subject_name=self.subject_names[random_subject]))

            if predict(img=path_to_img(random_image), class_id=random_class) == random_subject:
                success += 1

        self.assertGreaterEqual(success, int(success_perc * test_run_count))
