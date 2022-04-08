import requests

from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN

def api__admin_approve_text_message(line_user_id):
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
                "text": " 🎉 คุณได้รับการอนุมัติเป็น\n"
                        "Shouter เรียบร้อยแล้ว\n\n"
                        "➡️ NEXT STEP :\n\n"
                        "🙆🏻 รอรับงานผ่านไลน์นี้ได้เลย!\n\n"
                        "📤 คุณสามารถอัพโหลด สำเนาบัตรประชาชน และข้อมูลบัญชีธนาคาร เพื่อเป็นเอกสารรับรองในการรับเงินค่าจ้างผ่านแพลตฟอร์ม\n"
                        "(สามารถใส่ทีหลัง ก่อนรับเงินได้)\n"
                        "Link :https://shoutsolution.com/shouters/line-login?q=bank-account/"
            }
        ]
    }

    try:
        response = requests.post(url=push_message_url, headers=headers, json=data)
        return response
    except:
        return None


def api__admin_approve_flex_message(line_user_id, ig_profile_picture, first_name, last_name, ig_username, ig_follower_count):
    push_message_url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(LINE_CHANNEL_ACCESS_TOKEN)
    }
    data = {
        "to": line_user_id,
        "messages": [
            {
                "type": "flex",
                "altText": "อนุมัติเรียบร้อยแล้ว รอรับงานผ่าน Line ได้เลย!",
                "contents": {
                  "type": "bubble",
                  "direction": "ltr",
                  "header": {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "xxl",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "none",
                        "margin": "xs",
                        "paddingTop": "6px",
                        "paddingBottom": "6px",
                        "paddingStart": "12px",
                        "width": "90px",
                        "backgroundColor": "#44C350",
                        "cornerRadius": "14px",
                        "contents": [
                          {
                            "type": "text",
                            "text": "🎉 อนุมัติ",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#FFFFFF",
                            "contents": []
                          }
                        ]
                      }
                    ]
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "xl",
                        "position": "relative",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "position": "relative",
                            "width": "64px",
                            "height": "64px",
                            "cornerRadius": "50px",
                            "contents": [
                              {
                                "type": "image",
                                "url": ig_profile_picture,
                                "backgroundColor": "#000000FF"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "paddingTop": "8px",
                            "contents": [
                              {
                                "type": "text",
                                "text": ig_username,
                                "weight": "bold",
                                "size": "lg",
                                "align": "start",
                                "gravity": "center",
                                "contents": []
                              },
                              {
                                "type": "text",
                                "text": "IG Business Account",
                                "size": "sm",
                                "align": "start",
                                "gravity": "center",
                                "contents": []
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "separator",
                        "margin": "xxl"
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "xxl",
                        "paddingTop": "16px",
                        "paddingBottom": "16px",
                        "contents": [
                          {
                            "type": "text",
                            "text": "ชื่อ",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "{} {}".format(first_name, last_name),
                            "flex": 1,
                            "margin": "none",
                            "wrap": False,
                            "contents": []
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "baseline",
                        "flex": 1,
                        "spacing": "xxl",
                        "paddingBottom": "8px",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Follower",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": ig_follower_count,
                            "flex": 1,
                            "margin": "none",
                            "wrap": False,
                            "contents": []
                          }
                        ]
                      }
                    ]
                  }
                }
            }
        ]
    }

    try:
        response = requests.post(url=push_message_url, headers=headers, json=data)
        return response
    except:
        return None

def api__admin_approve_image_message(line_user_id):
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
                "originalContentUrl": "https://www.img.in.th/images/1f29ab7ec529c58263075cc6c3bca3ec.png",
                "previewImageUrl": "https://www.img.in.th/images/1bc0545644eefd347bae258f8eb6d0ae.png"
            }
        ]
    }

    try:
        response = requests.post(url=push_message_url, headers=headers, json=data)
        return response
    except:
        return None


def api__resend_connect_instagram(line_user_id):
    push_message_url = 'https://api.line.me/v2/bot/message/multicast'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(LINE_CHANNEL_ACCESS_TOKEN)
    }
    data = {
        "to": line_user_id,
        "messages": [
            {
                "type": "text",
                "text": "Hello World!"
            }
        ]
    }

    try:
        response = requests.post(url=push_message_url, headers=headers, json=data)
        return response
    except:
        return None


def video_message(line_user_id):
    push_message_url = 'https://api.line.me/v2/bot/message/multicast'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(LINE_CHANNEL_ACCESS_TOKEN)
    }
    data = {
        "to": line_user_id,
        "messages": [
            {
                "type": "video",
                "originalContentUrl": "https://shoutsolution.com/media/source/connect-instagram.mp4",
                "previewImageUrl": "https://shoutsolution.com/media/source/connect-instagram-thumbnail.png",
                "altText": "อีกนิดจะสมัครเสร็จแล้ว!!",
            }
        ]
    }

    try:
        response = requests.post(url=push_message_url, headers=headers, json=data)
        return response
    except:
        return None


def re_register_message(line_user_id):
    push_message_url = 'https://api.line.me/v2/bot/message/multicast'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(LINE_CHANNEL_ACCESS_TOKEN)
    }
    data = {
        "to": line_user_id,
        "messages": [
            {
                "type": "text",
                "text": "💓 อีกนิดเดียวคุณจะสมัครเสร็จแล้ว แค่ 1 คลิกเท่านั้น❗️(ไม่ถึง 2 นาที)\n\n"
                        "เหลือแค่เชื่อมต่อ IG ก็เสร็จการสมัครพร้อมรับงานผ่าน Shout! ได้ง่ายๆ\n\n"
                        "2 ขั้นตอนในการสมัครง่ายๆ 🔥\n\n"
                        "ดูวิธีใน Video ที่ส่งไปได้เลย 👇🏻📲\n\n"
                        "📌 IG เป็น Professional Account (เพียง 1 คลิกเสร็จ ดูเพิ่มเติมพิมพ์ 1)\n\n"
                        "📌 IG ผูกกับ Facebook Page (เพียง 1 คลิกเสร็จ ดูเพิ่มเติมพิมพ์ 2)\n\n"
                        "📌  คลิกลิงค์ https://shoutsolution.com/shouters/line-login?q=register/ หรือกดปุ่มบน Rich Menu เพื่อสมัคร Shout! ต่อได้เลย  🎉🎉🎉 \n\n"
                        "หากมีข้อสงสัยประการใด สามารถกด Support บน Rich Menu หรือสอบถามทีมงานผ่านทางนี้ได้เลย \n\n"
                        "หวังว่าจะได้ร่วมงานกันในฐานะ Shouter นะคะ ☺️🙏🏻"
            }
        ]
    }

    try:
        response = requests.post(url=push_message_url, headers=headers, json=data)
        return response
    except:
        return None