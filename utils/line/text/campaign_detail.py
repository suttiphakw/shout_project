from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN

import requests


def post(line_user_id, ig_username, context):
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
        "text": "🎉 ยินดีด้วย! คุณ {} ได้รับการ\n"
                "คัดเลือกจากนักการตลาดของ\n"
                "{} \n"
                "Platform ในการเข้าร่วมแคมเปญ\n"
                "ในฐานะ Shouter 🗣\n\n\n"
                "➡️ NEXT STEP: \n📍"
                "โปรดอ่านรายละเอียดเพิ่มเติม\n"
                "และ ตอบรับ หรือ ปฏิเสธงาน\n"
                "ได้ที่ปุ่ม 'ดูรายละเอียด' ด้านล่าง\n\n\n"
                "⏰ โปรดตอบรับงานภายในวันที่\n"
                "{}\n\n"
                "ไม่เช่นนั้นระบบจะทำการปฏิเสธงานอัตโนมัติ\n".format(ig_username, context['campaign_name'], context['accept_date_time'])
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
