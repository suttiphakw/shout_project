from utils.text.approve import post
from utils.text.approve_link import post as post_link
from utils.flex.approve import secret_voucher, product_promote


def pp_ig(line_user_id, link, comment="ไม่มี"):
  response_1 = post(line_user_id=line_user_id)
  response_2 = post_link(line_user_id=line_user_id, link=link, comment=comment)
  response_3 = product_promote.ig_story(line_user_id=line_user_id)
  return response_1.ok and response_2.ok and response_3.ok


def pp_ig_fb(line_user_id, link, comment="ไม่มี"):
  response_1 = post(line_user_id=line_user_id)
  response_2 = post_link(line_user_id=line_user_id, link=link, comment=comment)
  response_3 = product_promote.ig_fb_story(line_user_id=line_user_id)
  return response_1.ok and response_2.ok and response_3.ok


def sv_ig(line_user_id, link, comment="ไม่มี"):
  response_1 = post(line_user_id=line_user_id)
  response_2 = post_link(line_user_id=line_user_id, link=link, comment=comment)
  response_3 = secret_voucher.ig_story(line_user_id=line_user_id)
  return response_1.ok and response_2.ok and response_3.ok


def sv_ig_fb(line_user_id, link, comment="ไม่มี"):
  response_1 = post(line_user_id=line_user_id)
  response_2 = post_link(line_user_id=line_user_id, link=link, comment=comment)
  response_3 = secret_voucher.ig_fb_story(line_user_id=line_user_id)
  return response_1.ok and response_2.ok and response_3.ok