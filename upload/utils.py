import os
from time import time

BASE_FILE_PATH = 'files'

def get_upload_path(file_name):
    return os.path.join(BASE_FILE_PATH,file_name)

def handle_uploaded_file(f):
    filename = str(int(time())) +'.'+ f.name.split(".")[1]
    upload_path = get_upload_path(filename)

    if not os.path.exists(os.path.dirname(upload_path)):
        os.makedirs(os.path.dirname(upload_path))

    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return filename

def handle_delete_file(path):
   if os.path.isfile(path):
       os.remove(path)

def validate_file_size(file):
    filesize= file.size
    # 100MB - 104857600
    if filesize > 104857600:
        return True
    else:
        return False