from utils.text.approve_insight import post as post_text
from utils.flex.approve_insight import secret_voucher, product_promote


def pp(line_user_id):
  response_1 = post_text(line_user_id=line_user_id)
  response_2 = product_promote.post(line_user_id=line_user_id)
  return line_user_id, response_1.ok and response_2.ok


def sv(line_user_id):
  response_1 = post_text(line_user_id=line_user_id)
  response_2 = secret_voucher.post(line_user_id=line_user_id)
  return line_user_id, response_1.ok and response_2.ok
