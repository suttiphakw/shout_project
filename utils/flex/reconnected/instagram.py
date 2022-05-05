import requests
from shouters.models import Shouter
from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN

def post(line_user_id):
  # Get Shouter Vlue
  shouter = Shouter.objects.filter(line_user_id=line_user_id).first()
  ig_username = shouter.ig_username
  ig_follower_count = shouter.ig_follower_count
  first_name = shouter.first_name
  last_name = shouter.last_name

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
        "altText": "📮 ส่ง Insights",
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
                "margin": "none",
                "paddingTop": "6px",
                "paddingBottom": "6px",
                "paddingStart": "12px",
                "width": "140px",
                "backgroundColor": "#FF4747FF",
                "cornerRadius": "14px",
                "contents": [
                  {
                    "type": "text",
                    "text": "IG Disconnected",
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
            "margin": "none",
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
                        "url": "https://developers.line.biz/assets/images/services/bot-designer-icon.png",
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
                        "text": f"{ig_username}",
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
                    "text": f"{first_name} {last_name}",
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
                    "text": f"{ig_follower_count}",
                    "flex": 1,
                    "margin": "none",
                    "wrap": False,
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "margin": "md",
                "contents": [
                  {
                    "type": "text",
                    "text": "Status",
                    "weight": "bold",
                    "color": "#FF4747FF",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "IG Disconnected",
                    "weight": "bold",
                    "color": "#FF4747FF",
                    "align": "start",
                    "contents": []
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "paddingAll": "10px",
                "backgroundColor": "#E541410C",
                "cornerRadius": "8px",
                "contents": [
                  {
                    "type": "text",
                    "text": "โปรดเชื่อมต่อใหม่อีกครั้งเพื่อทำการรับงาน / ส่งงาน",
                    "weight": "bold",
                    "size": "lg",
                    "color": "#992727FF",
                    "align": "center",
                    "wrap": True,
                    "contents": []
                  }
                ]
              }
            ]
          },
          "footer": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "เชื่อมต่ออีกครั้ง",
                  "uri": "https://shoutsolution.com/shouter/line-login?q=social"
                },
                "color": "#F37324",
                "style": "primary"
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