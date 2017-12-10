import uuid
from config import UPLOADS_DIR
import os


def move_uploaded_file(files, name):
    file_name = str(uuid.uuid4()) + '.' + os.path.splitext(files[name].name)[1][1:]

    if not os.path.exists(UPLOADS_DIR):
        os.mkdir(UPLOADS_DIR)

    with open(UPLOADS_DIR + file_name, 'wb+') as destination:
        for chunk in files[name].chunks():
            destination.write(chunk)

    return UPLOADS_DIR + file_name


def tmp_file(ext):
    return UPLOADS_DIR + str(uuid.uuid4()) + '.' + ext
