import requests
from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN


def post(line_user_id):
  """ IG Story Only """
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
        "altText": "📮 โปรดรอการตรวจสอบ Insights",
        "contents": {
          "type": "bubble",
          "direction": "ltr",
          "header": {
            "type": "box",
            "layout": "horizontal",
            "spacing": "none",
            "margin": "none",
            "paddingBottom": "2px",
            "borderColor": "#4B2828FF",
            "contents": [
              {
                "type": "text",
                "text": "📢 Status",
                "weight": "bold",
                "size": "sm",
                "color": "#002257",
                "gravity": "center",
                "margin": "none",
                "contents": []
              },
              {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "10px",
                "width": "130px",
                "backgroundColor": "#EFB00810",
                "cornerRadius": "8px",
                "contents": [
                  {
                    "type": "text",
                    "text": "ตรวจสอบ Insights",
                    "weight": "bold",
                    "size": "xs",
                    "color": "#B48508",
                    "align": "end",
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
                "type": "separator"
              },
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "none",
                "margin": "none",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "none",
                    "contents": [
                      {
                        "type": "image",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Shopee.svg/2560px-Shopee.svg.png",
                        "size": "full",
                        "aspectRatio": "2:1"
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
                        "text": "Shopee - Secret Voucher",
                        "weight": "bold",
                        "size": "lg",
                        "align": "start",
                        "gravity": "center",
                        "offsetBottom": "8px",
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
                "layout": "baseline",
                "flex": 1,
                "spacing": "xxl",
                "margin": "lg",
                "paddingAll": "10px",
                "backgroundColor": "#EFB00810",
                "cornerRadius": "8px",
                "contents": [
                  {
                    "type": "text",
                    "text": "📊ขณะนี้กำลังตรวจสอบ Insights ของท่าน รอผลการตรวจสอบทาง line นี้ได้เลย!",
                    "weight": "bold",
                    "size": "md",
                    "color": "#B48508",
                    "align": "center",
                    "gravity": "center",
                    "wrap": True,
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


