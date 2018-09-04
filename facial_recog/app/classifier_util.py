from facial_recog.app.db_util import all_subjects_for_class


def get_class_subjects(class_id):
    return [i[0] for i in all_subjects_for_class(class_id)]
