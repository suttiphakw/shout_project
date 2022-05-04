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
        "text": "🚨 อย่าลืมส่ง story draft ของคุณเข้ามา เพื่อให้ทางแบรนด์ตรวจสอบ ภายในวันที่ 3 May ใครพร้อมแล้ว ส่งมาก่อนได้เลย!\n\n"
                "⚠️ ตอนส่งดราฟท์ แปะ Sticker link อะไรมาก่อนได้เลย Link จริงจะได้รับหลังแบรนด์ Approve ดราฟท์แล้ว\n\n"
                "ปล. หากมีข้อสงสัยตรงไหน สอบถามเข้ามาในนี้ได้เลย 🙇🏻‍♀"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None