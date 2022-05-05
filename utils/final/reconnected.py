from utils.text.reconnected import post as post_text
from utils.flex.reconnected import instagram


def ig_reconnected(line_user_id):
  response_1 = post_text(line_user_id=line_user_id)
  response_2 = instagram.post(line_user_id=line_user_id)
  return response_1.ok and response_2.ok