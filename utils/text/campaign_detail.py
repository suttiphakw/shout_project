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
        "text": "🎉 ยินดีด้วย! คุณได้รับการคัดเลือกจากนักการตลาดของ Shopee ในการเข้าร่วมแคมเปญ ในฐานะ Shouter 🗣\n\n"
                "➡️ NEXT STEP :\n"
                "📍 โปรดอ่านรายละเอียดงานด้านล่าง และตอบรับงานได้เลย!\n\n"
                "⏰ โปรดตอบรับงานภายในวันที่ 30/04/2022 ไม่เช่นนั้นระบบจะทำการ ปฏิเสธงานอัตโนมัติ"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None