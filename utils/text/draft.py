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
        "text": "✅ คุณได้ทำการตกลงรับงาน เรียบร้อยแล้ว\n\n"
                "➡️ NEXT STEP :\n"
                "🤳 เริ่มทำงานตามรายละเอียดงานและ ส่งดราฟท์งานเพื่อให้แบรนด์ตรวจสอบ ก่อนลงโพสท์จริงได้เลย!\n\n"
                "กำหนดส่งงานภายในวันที่ 03/05/2022 อย่าลืมบอกต่อในแบบของคุณ เพราะเราเชื่อในความจริงใจในการบอกต่อ 😋"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None