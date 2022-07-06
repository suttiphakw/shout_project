from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN

import requests


def post(line_user_id):
  push_message_url = 'https://api.line.me/v2/bot/message/push'
  headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(LINE_CHANNEL_ACCESS_TOKEN)
  }
  data = {
    "to": line_user_id,
    "messages": [
      {
        "type": "text",
        "text": "✅💰 งานของคุณเสร็จสิ้นเรียบร้อย ระบบได้ทำการชำระเงินให้คุณแล้ว\n\n"
                "ขอบคุณที่ร่วม Shout กับเรา! รอรับงานใหม่ผ่านทางไลน์นี้ได้เลย 💜🧡\n\n"
                "ปล. หากมีข้อสงสัย ติชม แนะนำ สามารถแชทกับพวกเราได้เลยในไลน์นี้😊"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)

