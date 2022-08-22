from utils.line.text.text_message import post as post_text


def all_social(line_user_id, context):
  response_1 = post_text(line_user_id=line_user_id, context=context)
  return response_1.ok
