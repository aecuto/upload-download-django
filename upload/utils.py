import os
from time import time

def handle_uploaded_file(f):
    file_name = str(time()) +'.'+ f.name.split(".")[1]
    upload_path = os.path.join('files', file_name)

    if not os.path.exists(os.path.dirname(upload_path)):
        os.makedirs(os.path.dirname(upload_path))

    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return upload_path

def handle_delete_file(path):
   if os.path.isfile(path):
       os.remove(path)