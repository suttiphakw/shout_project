from utils.text.sent_draft import post as post_text


def all_social(line_user_id):
  response_1 = post_text(line_user_id=line_user_id)
  return response_1.ok
