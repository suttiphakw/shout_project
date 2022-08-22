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
        "text": "👩🏻‍💻⚠️  แบรนด์ได้ทำการแจ้งขอ Revise งานของคุณ \n"
                "(Comment จากทางแบรนด์ อยู่ใน Message ถัดไป)\n\n"
                "➡️ NEXT STEP :\n"
                "✍🏻แก้ไขดราฟท์ตามคอมเมนต์ ที่ได้รับจากทางแบรนด์ และนำส่งดราฟท์ใหม่อีกครั้ง เพื่อให้แบรนด์ตรวจสอบ ก่อนลงโพสต์จริง ภายในวันที่ {}\n".format(context['sent_date'])
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
