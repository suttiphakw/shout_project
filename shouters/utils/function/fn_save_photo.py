from urllib.request import urlopen
from django.core.files import File
from tempfile import NamedTemporaryFile


def profile_picture(shouter, img_src):
  img_temp = NamedTemporaryFile(delete=True)
  img_temp.write(urlopen(img_src).read())
  img_temp.flush()
  shouter.ig_profile_picture_file.save(f"{shouter.first_name}.png", File(img_temp))
  shouter.save()


def media_picture(shouter, media_src, counter):
  img_temp = NamedTemporaryFile(delete=True)
  img_temp.write(urlopen(media_src).read())
  img_temp.flush()
  shouter['ig_media_picture_{}'.format(counter)].save(f"{shouter.first_name}.png", File(img_temp))
  shouter.save()
