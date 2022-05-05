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
        "text": "🚨Your Instagram is disconnected ! 🚨\n\n"
                "📲โปรดเชื่อมต่อบัญชี Instagram ของคุณใหม่อีกครั้ง\n\n" 
                "🙋🏻‍♀ อย่าลืมเชื่อมใหม่นะ เพราะจะทำให้คุณไม่สามารถรับงานผ่าน Shout! และไม่สามารถส่งงานเพื่อเสร็จสิ้นงานได้ (รวมไปถึงราคาจะไม่อัพเดทด้วยนะ) 💖\n\n"
                "ปล. หากคุณไม่ได้ทำการ Log Out ออกเอง อาจเกิดจาก การปิด Private IG  หรือหมดอายุการเชื่อมต่อ"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None