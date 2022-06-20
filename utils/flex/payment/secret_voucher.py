import requests
from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN


def post(line_user_id, ig_username, price, datetime):
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
        "altText": "📮 ทำจ่ายเสร็จสิ้น",
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
                "width": "115px",
                "backgroundColor": "#22A2142D",
                "cornerRadius": "8px",
                "contents": [
                  {
                    "type": "text",
                    "text": "ชำระเงินเรียบร้อย",
                    "weight": "bold",
                    "size": "xs",
                    "color": "#21802AFF",
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
                "margin": "xl",
                "contents": [
                  {
                    "type": "text",
                    "text": "ผู้รับเงิน",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "wrap": True,
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": f"{ig_username}",
                    "weight": "bold",
                    "size": "md",
                    "align": "end",
                    "gravity": "center",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "xl",
                "contents": [
                  {
                    "type": "text",
                    "text": "จำนวนเงิน",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "wrap": True,
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": f"{price} บาท",
                    "weight": "bold",
                    "size": "md",
                    "align": "end",
                    "gravity": "center",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "xl",
                "contents": [
                  {
                    "type": "text",
                    "text": "ชำระวันที่",
                    "weight": "bold",
                    "size": "md",
                    "align": "start",
                    "gravity": "center",
                    "wrap": True,
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": f"{datetime}",
                    "weight": "bold",
                    "size": "md",
                    "align": "end",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "flex": 1,
                "spacing": "xxl",
                "margin": "lg",
                "paddingAll": "10px",
                "backgroundColor": "#22A2142D",
                "cornerRadius": "8px",
                "contents": [
                  {
                    "type": "text",
                    "text": "ชำระเงินเรียบร้อย ✅💰",
                    "weight": "bold",
                    "size": "lg",
                    "color": "#21802AFF",
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
