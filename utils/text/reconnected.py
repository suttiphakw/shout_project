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
        "text": "🙋🏻‍♀️🙋🏻‍♂️ ขอเชิญ Shouter ที่ลงทะเบียนเลือก Shopee Social Partner Affiliate Link ในการทำงาน เข้าร่วม Online Workshop เพื่อเข้าใจวิธีการใช้งานและเทคนิคการสร้างยอดขาย ตามวันและเวลาดังต่อไปนี้ 👇🏻\n\n"
                "วัน : 29/04/2022 (วันศุกร์นี้)\n" 
                "เวลา :  15.00 - 16.00 น.\n"
                "Link : https://sea.zoom.us/j/6378055892\n\n"
                "ปล. Workshop จำเป็นต้องเข้าร่วมทุกท่าน หากท่านใดไม่สะดวกตามวันและเวลาดังกล่าว รบกวนแจ้งทางทีมงานผ่านทาง Line OA นี้ได้เลย"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None