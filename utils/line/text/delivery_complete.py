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
        "text": "✅ จัดส่งสินค้าเรียบร้อยแล้ว\n"
                "Tracking Number : {}\n\n\n"
                "➡️ NEXT STEP :\n"
                "🚚 คุณสามารถติดตามสถานะการจัดส่ง ได้ตามเลข Tracking Number ด้านบน และโปรดตอบรับ เมื่อได้รับสินค้าเรียบร้อยแล้ว\n\n\n"
                "ปล. หากไม่ได้รับสินค้า รบกวนแจ้งผ่านทางไลน์นี้ได้เลย".format(context['tracking_num'])
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
