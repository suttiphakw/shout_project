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
        "text": "📩  คุณได้ทำการส่งดราฟท์เรียบร้อยแล้ว \n\n"
                "➡️  NEXT STEP : \n"
                "👩🏻‍💻โปรดรอแบรนด์ตรวจสอบและ Approve งานก่อนเริ่มขั้นตอนต่อไป โดยผลการ Approve จะแจ้งให้คุณทราบผ่านช่องทาง Line นี้ \n"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
