import os

db_dir = os.path.join('facial_recog', 'db')

db = {
    'sqlite3': {
        'host': os.path.join(db_dir, 'master.sqlite'),
        'user': '',
        'passwd': '',
        'db': 'master',
    },
    'mongodb': {
        'host': '',
        'user': '',
        'passwd': '',
        'db': '',
        'table': '',
    },
}

tables = {
    'class': {
        'name': 'class',
        'columns': ('id INT PRIMARY KEY', 'vtuID INT', 'classID INT',),
    },
}

cascade = {
    'lbp': 'lbpcascade_frontalface_improved.xml',
    'haar': 'haarcascade_frontalface_default.xml',
}

cascade_dir = {
    'lbp': os.path.join('facial_recog', 'cascades', 'lbp'),
    'haar': os.path.join('facial_recog', 'cascades', 'haar'),
}

recog_dir = {
    'lbph': os.path.join('facial_recog', 'recognizers', 'lbph'),
    'eigen': os.path.join('facial_recog', 'recognizers', 'eigen'),
    'fisher': os.path.join('facial_recog', 'recognizers', 'fisher'),
}

training_dir = os.path.join('facial_recog', 'training_dataset')

log_dir = os.path.join('logs')

use_db = 'sqlite3'

detect_method = 'lbp'

recog_method = 'lbph'

confidence_threshold = 100.0
