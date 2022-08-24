import os.path
from urllib.request import urlopen
from django.core.files import File
from tempfile import NamedTemporaryFile


def profile_picture(shouter, img_src):
  img_temp = NamedTemporaryFile(delete=True)
  img_temp.write(urlopen(img_src).read())
  img_temp.flush()
  filename, file_ext = os.path.splitext(img_src)
  shouter.ig_profile_picture_file.save(f"{shouter.first_name}{file_ext}", File(img_temp))
  shouter.save()
