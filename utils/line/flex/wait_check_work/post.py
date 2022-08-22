import requests

from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN


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
        "type": "flex",
        "altText": "📍 รอการตรวจสอบ",
        "contents": {
          "type": "bubble",
          "direction": "ltr",
          "header": {
            "type": "box",
            "layout": "vertical",
            "spacing": "xs",
            "paddingBottom": "2px",
            "borderColor": "#4B2828FF",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "📢 Status",
                    "size": "lg",
                    "color": "#202046FF",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "none",
                    "margin": "none",
                    "paddingAll": "4px",
                    "width": "115px",
                    "backgroundColor": "#E9EBF1",
                    "cornerRadius": "50px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "🔍รอตรวจสอบ",
                        "weight": "regular",
                        "size": "sm",
                        "color": "#656C83",
                        "align": "center",
                        "gravity": "center",
                        "contents": []
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "height": "16px",
                "contents": [
                  {
                    "type": "filler"
                  }
                ]
              },
              {
                "type": "separator",
                "margin": "xxl"
              }
            ]
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "margin": "sm",
                "paddingTop": "8px",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(context['campaign_name']),
                    "weight": "regular",
                    "size": "lg",
                    "color": "#202046",
                    "align": "start",
                    "gravity": "center",
                    "margin": "md",
                    "offsetBottom": "8px",
                    "contents": []
                  }
                ]
              },
              {
                "type": "separator",
                "margin": "xxl"
              },
              {
                "type": "box",
                "layout": "vertical",
                "margin": "xl",
                "paddingAll": "12px",
                "borderWidth": "1px",
                "backgroundColor": "#FDF7E6",
                "borderColor": "#F3BB20FF",
                "cornerRadius": "8px",
                "contents": [
                  {
                    "type": "text",
                    "text": "📊ขณะนี้กำลังตรวจสอบผลงานของท่าน รอผลการตรวจสอบทาง Line นี้ได้เลย!",
                    "color": "#202046",
                    "align": "center",
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
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)

