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
        "text": "🚀✅ คุณได้ทำการส่งงานด้วย Link เรียบร้อยแล้ว\n\n"
                "➡️ NEXT STEP :\n"
                "📸📊 โปรดแคปหน้า IG Story Insights ให้เห็นยอด “Link Clicks” และในหัวข้อ “Story Interactions”  หลังจากโพสท์ไปแล้วครบ 24 ชม. และส่งรูป Insight เพื่อเป็นการเสร็จสิ้นงาน\n\n"
                "❓ How to get IG Story Insights :\n"
                "1. กดที่ ☰ ของหน้า IG Profile (มุมขวาบน)\n"
                "2. เข้าไปที่ Archive\n"
                "3. เลือก Story งาน >> ปัดขึ้น\n"
                "4. เลือก 📊 Insight\n"
                "5. ทำการ 📸 แคปหน้าจอ หัวข้อ 'Story Interactions' & 'Sticker Taps' ให้เห็นตัวเลขครบชัดเจน\n"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except:
    return None