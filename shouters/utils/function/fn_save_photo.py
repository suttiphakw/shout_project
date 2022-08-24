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
  if counter == 1:
    shouter.ig_media_picture_1.save(f"{shouter.first_name}.png", File(img_temp))
  elif counter == 2:
    shouter.ig_media_picture_2.save(f"{shouter.first_name}.png", File(img_temp))
  elif counter == 3:
    shouter.ig_media_picture_3.save(f"{shouter.first_name}.png", File(img_temp))
  elif counter == 4:
    shouter.ig_media_picture_4.save(f"{shouter.first_name}.png", File(img_temp))
  elif counter == 5:
    shouter.ig_media_picture_5.save(f"{shouter.first_name}.png", File(img_temp))
  elif counter == 6:
    shouter.ig_media_picture_6.save(f"{shouter.first_name}.png", File(img_temp))
  elif counter == 7:
    shouter.ig_media_picture_7.save(f"{shouter.first_name}.png", File(img_temp))
  elif counter == 8:
    shouter.ig_media_picture_8.save(f"{shouter.first_name}.png", File(img_temp))
  elif counter == 9:
    shouter.ig_media_picture_9.save(f"{shouter.first_name}.png", File(img_temp))

  shouter.save()
