from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN

import requests


def post(line_user_id, context):
  push_message_url = 'https://api.line.me/v2/bot/message/push'
  headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(LINE_CHANNEL_ACCESS_TOKEN)
  }
  if not context['comment_story']:
    data = {
      "to": line_user_id,
      "messages": [
        {
          "type": "text",
          "text": "👩🏻‍💻⚠️ Comment จากแบรนด์\n\n"
                  "IG Post: \n"
                  "{}".format(context['comment_post'])
        }
      ]
    }

  elif not context['comment_post']:
    data = {
      "to": line_user_id,
      "messages": [
        {
          "type": "text",
          "text": "👩🏻‍💻⚠️ Comment จากแบรนด์\n\n"
                  "IG Story: \n"
                  "{}".format(context['comment_story'])
        }
      ]
    }

  else:
    data = {
      "to": line_user_id,
      "messages": [
        {
          "type": "text",
          "text": "👩🏻‍💻⚠️ Comment จากแบรนด์\n\n"
                  "IG Story :\n"
                  "{}\n\n"
                  "IG Post: \n"
                  "{}".format(context['comment_story'], context['comment_post'])
        }
      ]
    }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
