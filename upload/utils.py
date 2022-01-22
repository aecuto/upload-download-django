import os
import random
import string

BASE_FILE_PATH = 'files'

def uniq_id(size=6, chars=string.ascii_uppercase + string.digits):
     return ''.join(random.choice(chars) for _ in range(size))

def get_file_name(file_name):
    return uniq_id() + '-' + file_name

def handle_uploaded_file(f):
    filename = get_file_name(f.name)
    path = os.path.join(BASE_FILE_PATH,filename)

    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return filename

def handle_delete_file(path):
   if os.path.isfile(path):
       os.remove(path)

def get_upload_path(file_name):
    return os.path.join(BASE_FILE_PATH,file_name)