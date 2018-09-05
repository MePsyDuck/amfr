db = {
    'sqlite3': {
        'host': 'facial_recog/db/master.sqlite',
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

cascade_dir = {
    'lbp': "facial_recog/cascades/lbp/",
    'haar': 'facial_recog/cascades/haar/',
}

recog_dir = {
    'lbph': "facial_recog/recognizers/lbph/",
    'eigen': "facial_recog/recognizers/eigen/",
    'fisher': "facial_recog/recognizers/fisher/",
}

use_db = 'sqlite3'

detect_method = 'lbp'

recog_method = 'lbph'
