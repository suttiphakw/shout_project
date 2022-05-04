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
        "text": "👩🏻‍💻⚠️  แบรนด์ได้ทำการแจ้งขอ Revise งานของคุณ (Comment จากทางแบรนด์ อยู่ใน Message ถัดไป)\n\n"
                "➡️ NEXT STEP :\n"
                "✍🏻แก้ไขดราฟท์ตามคอมเมนต์ที่ได้รับจากทางแบรนด์ และนำส่งดราฟท์ใหม่อีกครั้ง เพื่อให้แบรนด์ตรวจสอบก่อนลงโพสท์จริง ภายในวันที่ 03/05/2022"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None