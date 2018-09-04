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
    'lbp': "facial_recog/cascades/lbp",
}

default_db = 'sqlite3'
default_method = 'lbp'
