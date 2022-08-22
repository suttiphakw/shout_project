from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN

import requests


def post_img(line_user_id):
  push_message_url = 'https://api.line.me/v2/bot/message/push'
  headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(LINE_CHANNEL_ACCESS_TOKEN)
  }
  data = {
    "to": line_user_id,
    "messages": [
      {
        "type": "image",
        "originalContentUrl": "https://www.shoutsolution.com/media/source/campaign/how_to_do_campaign.jpeg",
        "previewImageUrl": "https://www.shoutsolution.com/media/source/campaign/how_to_do_campaign.jpeg"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None