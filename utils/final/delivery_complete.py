from utils.text.delivery_complete import post as post_text
from utils.flex.delivery_complete import post as post_flex


def all_social(line_user_id, context):
  response_1 = post_text(line_user_id=line_user_id, context=context)
  response_2 = post_flex.post(line_user_id=line_user_id, context=context)
  return response_1.ok and response_2.ok
