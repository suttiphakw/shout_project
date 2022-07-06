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
        "text": "❌ คุณได้ทำการยกเลิกการทำงาน ในแคมเปญ ของ {} เรียบร้อยแล้ว\n\n"
                "🙏🏻หากมีคำแนะนำติชม สามารถแจ้งพวกเรา หรือรอรับงานใหม่ผ่านไลน์นี้ได้เลย".format(context['campaign_name'])
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
