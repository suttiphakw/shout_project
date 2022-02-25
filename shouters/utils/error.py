def log(shouter, error_message):
  shouter.is_error = True
  shouter.error_section = error_message
  shouter.save()