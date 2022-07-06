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
        "altText": "📍 ชำระเงินเสร็จสิ้น",
        "contents": {
          "type": "carousel",
          "contents": [
            {
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
                        "width": "130px",
                        "backgroundColor": "#44C350",
                        "cornerRadius": "50px",
                        "contents": [
                          {
                            "type": "text",
                            "text": "ชำระเงินเรียบร้อย",
                            "weight": "regular",
                            "size": "sm",
                            "color": "#FFFFFF",
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
                    "layout": "horizontal",
                    "margin": "xxl",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ผู้รับเงิน",
                        "color": "#202046AA",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "{}".format(context['name']),
                        "color": "#202046FF",
                        "align": "end",
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xl",
                    "contents": [
                      {
                        "type": "text",
                        "text": "จำนวนเงิน",
                        "color": "#202046AA",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "{} บาท".format(context['price']),
                        "color": "#202046FF",
                        "align": "end",
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xl",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ชำระวันที่",
                        "color": "#202046AA",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "{}".format(context['payment_date']),
                        "color": "#202046FF",
                        "align": "end",
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xxl",
                    "paddingAll": "12px",
                    "borderWidth": "1px",
                    "backgroundColor": "#038E3F10",
                    "borderColor": "#44C350",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ชำระเงินเรียบร้อย ✅💰",
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
          ]
        }
      }
    ]
  }
  try:
    response = requests.post(url=push_message_url, headers=headers, json=data)
    return response
  except requests.exceptions.HTTPError as err:
    return SystemExit(err)

