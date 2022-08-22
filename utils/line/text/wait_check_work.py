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
        "text": "✅📊 คุณทำการส่งผลงานครบถ้วน เรียบร้อย\n\n"
                "➡️ NEXT STEP :\n"
                "รอการตรวจสอบผลงาน จากทีมงาน หากถูกต้องเรียบร้อย ทางระบบจะแจ้งให้ทราบผ่านไลน์นี้"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
