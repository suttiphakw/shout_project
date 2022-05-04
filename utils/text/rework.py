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
        "text": "🚨🚨🚨 อย่าลืม!! ลงโพสท์งาน Shopee ภายในวันนี และนำส่ง story link งานของคุณ ที่ปุ่ม “ส่งงาน” ข้อความด้านบนได้เลย\n\n"
                "⚠️ อย่าลืมสร้าง Story (ให้เหมือนกับ Approved Draft) พร้อมแปะ Sticker Link โดยใช้ Link ที่ได้รับจากทางแบรนด์นะ"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None