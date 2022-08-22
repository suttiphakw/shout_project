from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN

import requests


def post(line_user_id, context):
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
        "text": "✅ เริ่มต้นทำงานในฐานะ Shouter ได้เลย!\n\n\n"
                "➡️ NEXT STEP :\n"
                "🤳 เริ่มทำงานตามรายละเอียดงานและ ส่งดราฟท์งานเพื่อให้แบรนด์ตรวจสอบ ก่อนลงโพสต์จริงได้เลย!\n\n\n"
                "กำหนดส่งงานภายในวันที่ {} อย่าลืมสร้าง content ในแบบของคุณ เพราะเราเชื่อในความจริงใจในการบอกต่อ 😋".format(context['sent_date'])
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
