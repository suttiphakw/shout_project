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
                "text": "🎉 คุณได้รับการอนุมัติเป็น Shouter \nเรียบร้อยแล้ว \n\n"
                        "➡️ NEXT STEP : 📥 คุณสามารถ อัพโหลด สำเนาบัตรประชาชน และข้อมูลบัญชีธนาคาร เพื่อเป็นเอกสาร "
                        "รับรองในการรับเงินค่าจ้างผ่านแพลตฟอร์ม ที่ Link :XXXX และรอรับงานผ่าน Line นี้ได้เลย!"
            }
        ]
    }

    try:
        response = requests.post(url=push_message_url, headers=headers, json=data)
        return response
    except:
        return None


def api__admin_approve_flex_message(line_user_id, line_profile_picture, first_name, ig_username, ig_follower_count):
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
                                "url": line_profile_picture,
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
                            "text": first_name,
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