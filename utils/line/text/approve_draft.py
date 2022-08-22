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
        "text": "👩🏻‍💻✅ แบรนด์ได้ทำการ Approve งานของคุณแล้ว \n\n\n"
                "➡️ NEXT STEP :\n"
                "📲 🚀 ทำการโพสต์งาน ให้เหมือนกับ Draft ที่ถูก Approve จากนั้น Copy Link มาส่งงานได้เลย!\n\n\n"
                "กำหนดโพสต์ และส่งงานในวันที่ {}".format(context['sent_date'])
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
