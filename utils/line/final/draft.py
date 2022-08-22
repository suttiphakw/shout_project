from utils.line.text.draft import post as post_text
from utils.line.image.draft import post_img
from utils.line.flex.draft import post as post_flex


def ig(line_user_id, context):
  response_1 = post_text(line_user_id=line_user_id, context=context)
  response_2 = post_img(line_user_id=line_user_id)
  response_3 = post_flex.ig(line_user_id=line_user_id, context=context)
  return response_1.ok and response_2.ok and response_3.ok


def ig_fb(line_user_id, context):
  response_1 = post_text(line_user_id=line_user_id, context=context)
  response_2 = post_img(line_user_id=line_user_id)
  response_3 = post_flex.ig_fb(line_user_id=line_user_id, context=context)
  return response_1.ok and response_2.ok and response_3.ok
