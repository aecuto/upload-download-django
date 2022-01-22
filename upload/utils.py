import os

def handle_uploaded_file(f):
  filename = os.path.join('files',f.name)

  if not os.path.exists(os.path.dirname(filename)):
    os.makedirs(os.path.dirname(filename))

  with open(filename, 'wb+') as destination:
    for chunk in f.chunks():
      destination.write(chunk)