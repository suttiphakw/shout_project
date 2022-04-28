from utils.text.draft import post
from utils.image.draft import post_img
from utils.draft import product_promote, secret_voucher

def pp_ig(line_user_id):
  response_1 = post(line_user_id=line_user_id)
  response_2 = post_img(line_user_id=line_user_id)
  response_3 = product_promote.ig_story(line_user_id=line_user_id)
  return response_1.ok and response_2.ok and response_3.ok

def pp_ig_fb(line_user_id):
  response_1 = post(line_user_id=line_user_id)
  response_2 = post_img(line_user_id=line_user_id)
  response_3 = product_promote.ig_fb_story(line_user_id=line_user_id)
  return response_1.ok and response_2.ok and response_3.ok

def sv_ig(line_user_id):
  response_1 = post(line_user_id=line_user_id)
  response_2 = post_img(line_user_id=line_user_id)
  response_3 = secret_voucher.ig_story(line_user_id=line_user_id)
  return response_1.ok and response_2.ok and response_3.ok


def sv_ig_fb(line_user_id):
  response_1 = post(line_user_id=line_user_id)
  response_2 = post_img(line_user_id=line_user_id)
  response_3 = secret_voucher.ig_fb_story(line_user_id=line_user_id)
  return response_1.ok and response_2.ok and response_3.ok