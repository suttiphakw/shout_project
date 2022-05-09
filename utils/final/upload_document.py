from utils.text.upload_document import post as post_text
from utils.flex.upload_document import secret_voucher, product_promote


def pp(line_user_id):
  response_1 = post_text(line_user_id=line_user_id)
  response_2 = product_promote.post(line_user_id=line_user_id)
  return response_1.ok and response_2.ok

def sv(line_user_id):
  response_1 = post_text(line_user_id=line_user_id)
  response_2 = secret_voucher.post(line_user_id=line_user_id)
  return response_1.ok and response_2.ok