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
        "text": "✅📊 คุณทำการส่ง Insight เรียบร้อย\n\n"
                "➡️ NEXT STEP :\n"
                "รอการตรวจสอบ Insights จากทีมงาน หากถูกต้องเรียบร้อย ทางระบบจะแจ้งให้ทราบผ่านไลน์นี้\n\n"
                "🙋🏻‍♀️📲 ระหว่างนี้ ให้ Shouter ทุกคน เข้าไปมาอัพโหลดเอกสารสำหรับการทำจ่าย ดังนี้ :\n"
                "1. สำเนาบัตรประชาชน (เซ็นกำกับสำเนาถูกต้อง)\n"
                "2. สำเนา BookBank (พร้อมเซ็นชื่อกำกับ)\n"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None