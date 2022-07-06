from utils.text.revise_draft import post as post_text
from utils.text.brand_comment import post as post_comment
from utils.flex.revise_draft import post as post_flex


def ig(line_user_id, context):
  response_1 = post_text(line_user_id=line_user_id, context=context)
  response_2 = post_comment(line_user_id=line_user_id, context=context)
  response_3 = post_flex.ig(line_user_id=line_user_id, context=context)
  return response_1.ok and response_2.ok and response_3.ok


def ig_fb(line_user_id, context):
  response_1 = post_text(line_user_id=line_user_id, context=context)
  response_2 = post_comment(line_user_id=line_user_id, context=context)
  response_3 = post_flex.ig_fb(line_user_id=line_user_id, context=context)
  return response_1.ok and response_2.ok and response_3.ok
