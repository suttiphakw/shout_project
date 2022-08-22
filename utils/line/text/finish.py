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
        "text": "👩✅🔎 งานของคุณเสร็จสิ้นเรียบร้อยแล้ว🎉 \n\n\n"
                "➡️ NEXT STEP :\n"
                "เข้าไป ตรวจสอบ/อัพโหลดเอกสารสำหรับการทำจ่าย ดังนี้ :\n"
                "1. สำเนาบัตรประชาชน (เซ็นกำกับสำเนาถูกต้อง)\n"
                "2. สำเนา BookBank (พร้อมเซ็นชื่อกำกับ)\n\n\n"
                "หากเอกสารเรียบร้อย รอรับเงินได้เลย! เราจะทำจ่ายให้คุณไปในบัญชีที่ระบุไว้ ภายใน 15 วัน💰💰"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
