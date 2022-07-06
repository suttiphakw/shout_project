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
        "altText": "📍 ส่งงานเสร็จสิ้น",
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
                        "width": "100px",
                        "backgroundColor": "#F3BB20FF",
                        "cornerRadius": "50px",
                        "contents": [
                          {
                            "type": "text",
                            "text": "รอส่ง Insights",
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
                    "layout": "vertical",
                    "margin": "xl",
                    "paddingAll": "12px",
                    "borderWidth": "1px",
                    "backgroundColor": "#038E3F10",
                    "borderColor": "#44C350",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "➡️Next Step",
                        "weight": "bold",
                        "size": "sm",
                        "color": "#202046",
                        "margin": "none",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": " Capture Insight หลังจากที่โพสต์ไปแล้วครบ 24 ชม. และเข้ามาส่งรูปเพื่อเสร็จสิ้นงาน",
                        "color": "#202046",
                        "margin": "xxl",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "paddingBottom": "8px",
                        "contents": [
                          {
                            "type": "text",
                            "text": "📮ส่งภายในวันที่",
                            "weight": "bold",
                            "size": "md",
                            "color": "#202046",
                            "align": "start",
                            "gravity": "center",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "{}".format(context['sent_date']),
                            "weight": "regular",
                            "color": "#202046",
                            "align": "start",
                            "gravity": "center",
                            "margin": "md",
                            "wrap": True,
                            "contents": []
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "ส่งรูป Insights",
                      "uri": "{}".format(context['google_form_link'])
                    },
                    "color": "#F37324",
                    "style": "primary",
                    "gravity": "center"
                  }
                ]
              }
            },
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
                    "type": "text",
                    "text": "📮 Capture Insights",
                    "weight": "regular",
                    "size": "lg",
                    "color": "#002257",
                    "align": "start",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "ส่งรูป Insights",
                    "size": "sm",
                    "color": "#8A8AA0FF",
                    "offsetStart": "28px",
                    "contents": []
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
                    "type": "image",
                    "url": "https://www.img.in.th/images/d01c92b9b8fd5c36ba7ebb906c160cf9.png",
                    "align": "center",
                    "gravity": "top",
                    "size": "full",
                    "aspectRatio": "1:1.5",
                    "aspectMode": "fit"
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
                      "label": "ส่งรูป Insights",
                      "uri": "{}".format(context['google_form_link'])
                    },
                    "color": "#F37324",
                    "style": "primary"
                  }
                ]
              }
            },
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
                    "type": "text",
                    "text": "📮 Capture Insights",
                    "weight": "regular",
                    "size": "lg",
                    "color": "#002257",
                    "align": "start",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "ส่งรูป Insights",
                    "size": "sm",
                    "color": "#8A8AA0FF",
                    "offsetStart": "28px",
                    "contents": []
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
                    "type": "image",
                    "url": "https://www.img.in.th/images/7151652978c496a7f2af03c978d11dc6.jpg",
                    "align": "center",
                    "gravity": "top",
                    "size": "full",
                    "aspectRatio": "1:1.5",
                    "aspectMode": "fit"
                  }
                ]
              },
              "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "ส่งรูป Insights",
                      "uri": "{}".format(context['google_form_link'])
                    },
                    "color": "#F37324",
                    "style": "primary",
                    "gravity": "center"
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

