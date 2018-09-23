import os
from datetime import datetime

fdb_urls = {
    # In increasing order of difficulty -> faces94 < faces 95 < faces96 < grimace
    # faces94 uses different directory structure so ignore it for now
    'faces94': r'http://cmp.felk.cvut.cz/~spacelib/faces/faces94.zip',
    'faces95': r'http://cmp.felk.cvut.cz/~spacelib/faces/faces95.zip',
    'faces96': r'http://cmp.felk.cvut.cz/~spacelib/faces/faces96.zip',
    'grimace': r'http://cmp.felk.cvut.cz/~spacelib/faces/grimace.zip',
}

fdb_name = 'faces95'

test_src_dir = os.path.join('test_src')

fdb_loc = os.path.join(test_src_dir, fdb_name)

fdb_file = os.path.join(test_src_dir, fdb_name + '.zip')

subject_count = 10

class_count = 2

image_count = 10

seed = datetime.now()

test_run_count = 10

success_perc = 0.7
