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
        "text": "✅ คุณได้ทำการตกลงรับงานเรียบร้อยแล้ว\n\n"
                "➡️ NEXT STEP :\n📦"
                "🕑 โปรดรอการจัดส่งสินค้า \n"
                "หากจัดส่งสินค้าแล้ว ระบบจะแจ้งหมายเลข Tracking Number เพื่อให้คุณตรวจสอบสถานะการจัดส่ง"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
