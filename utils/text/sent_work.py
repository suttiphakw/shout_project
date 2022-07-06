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
        "text": "🚀✅ คุณได้ทำการส่งงานด้วย Link เรียบร้อยแล้ว\n\n\n"
                "➡️ NEXT STEP :\n"
                "📸📊 โปรดแคปหน้า IG Story Insights ให้เห็นยอด “Link Clicks” และในหัวข้อ “Story Interactions”  "
                "หลังจากโพสท์ไปแล้วครบ 24 ชม. และส่งรูป Insight เพื่อเป็นการเสร็จสิ้นงาน\n\n\n"
                "❓ How to get IG Story Insights :\n"
                "1. กดที่ ☰ ของหน้า IG Profile (มุมขวาบน)\n"
                "2. เข้าไปที่ Archive\n"
                "3. เลือก Story งาน >> ปัดขึ้น\n"
                "4. เลือก 📊 Insight\n"
                "5. ทำการ 📸 แคปหน้าจอ หัวข้อ 'Story Interactions' & 'Sticker Taps' ให้เห็นตัวเลขครบชัดเจน\n\n"
                "(กรณีมี Facebook Story)\n"
                "❓How to แคป FB Story มาส่ง :\n"
                "1. เข้าไปที่ FB Profile\n"
                "2. กดที่ “...”  (ปุ่มขวาข้างๆ edit profile)\n"
                "3. เข้าไปที่ Archive\n"
                "4. กดที่ปุ่ม Story Archives (ซ้ายบน)\n"
                "5. เลือก Story งาน >> Capture หน้านั้นมาส่ง (ให้เห็นยอด viewers)\n"
                "⚠️ถ้าหาไม่เจอ โปรดแจ้งทีมงานและแจ้งค่าประมาณการณ์ของ viewers มาแทน"
      }
    ]
  }

  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)
