from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN

import requests


def post(line_user_id, comment):
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
        "text": "👩🏻‍💻⚠️  Comment จากแบรนด์\n\n"
                "Story :\n"
                "{}".format(comment)
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None