from utils.text.campaign_detail import post
from utils.flex.campaign_detail import secret_voucher, product_promote


def pp_ig(line_user_id, price):
  response_1 = post(line_user_id=line_user_id)
  response_2 = product_promote.ig_story(line_user_id=line_user_id, price=price)
  return response_1.ok and response_2.ok

def pp_ig_fb(line_user_id, price):
  response_1 = post(line_user_id=line_user_id)
  response_2 = product_promote.ig_fb_story(line_user_id=line_user_id, price=price)
  return response_1.ok and response_2.ok

def sv_ig(line_user_id, price):
  response_1 = post(line_user_id=line_user_id)
  response_2 = secret_voucher.ig_story(line_user_id=line_user_id, price=price)
  return response_1.ok and response_2.ok


def sv_ig_fb(line_user_id, price):
  response_1 = post(line_user_id=line_user_id)
  response_2 = secret_voucher.ig_fb_story(line_user_id=line_user_id, price=price)
  return response_1.ok and response_2.ok