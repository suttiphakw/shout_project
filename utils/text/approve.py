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
        "text": "👩🏻‍💻✅ แบรนด์ได้ทำการ Approve งานของคุณแล้ว และได้ส่ง LINK ที่ต้องการให้นำไปใส่ในสตอรี่จริง (Sticker Link) เรียบร้อย\n\n"
                "➡️ NEXT STEP :\n"
                "📲 🚀 ทำการสร้าง Story ใหม่ให้ เหมือนกับ Draft ที่ถูก Approve และโพสท์ลง Story จากนั้น Copy Story Link นั้น มาส่งงานในนี้ได้เลย!\n\n"
                "⚠️⚠️ อย่าลืมแก้ LINK ในสตอรี่ตอนโพสท์จริง เป็นอันที่แบรนด์ส่งให้ และห้ามนำ Story Draft ไปโพสท์ลงทันที ⚠️⚠️\n\n" 
                "กำหนดโพสท์ และส่งงานในวันที่ 04/05/2022 เวลา 20.00-22.00 น."
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None