# Upload Image
def get_unique_name(dir, filename, shouter):
  if not dir.endswith('/'):
      dir += '/'

  sp = filename.split('.')
  first_name = shouter.first_name
  last_name = shouter.last_name
  ext = sp[-1]
  tz = timezone(timedelta(hours=7))
  today = datetime.datetime.now(tz=tz)
  y = today.year
  m = today.month
  d = today.day
  h = today.hour
  mi = today.minute
  s = today.second
  return f'{dir}{first_name}_{last_name}_{y}{m:02d}{d:02d}_{h:02d}{mi:02d}{s:02d}.{ext}'