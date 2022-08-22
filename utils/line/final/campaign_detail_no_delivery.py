from utils.line.text.campaign_detail import post as post_text
from utils.line.flex.campaign_detail_no_delivery import post as post_flex


def ig(line_user_id, ig_username, price, context):
  response_1 = post_text(line_user_id=line_user_id, ig_username=ig_username, context=context)
  response_2 = post_flex.ig(line_user_id=line_user_id, price=price, context=context)
  return response_1.ok and response_2.ok


def ig_fb(line_user_id, ig_username, price, context):
  response_1 = post_text(line_user_id=line_user_id, ig_username=ig_username, context=context)
  response_2 = post_flex.ig_fb(line_user_id=line_user_id, price=price, context=context)
  return response_1.ok and response_2.ok
