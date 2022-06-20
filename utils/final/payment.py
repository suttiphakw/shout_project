from utils.text.payment import post as post_text
from utils.flex.payment import secret_voucher, product_promote


def pp(line_user_id, ig_username, price, datetime):
  response_1 = post_text(line_user_id=line_user_id)
  response_2 = product_promote.post(line_user_id=line_user_id, ig_username=ig_username, price=price, datetime=datetime)
  return line_user_id, response_1.ok and response_2.ok


def sv(line_user_id, ig_username, price, datetime):
  response_1 = post_text(line_user_id=line_user_id)
  response_2 = secret_voucher.post(line_user_id=line_user_id, ig_username=ig_username, price=price, datetime=datetime)
  return line_user_id, response_1.ok and response_2.ok
