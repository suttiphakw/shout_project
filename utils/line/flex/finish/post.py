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
        "altText": "📍 ตรวจงานงานเสร็จสิ้น",
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
                        "backgroundColor": "#44C350",
                        "cornerRadius": "50px",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Completed",
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
                    "type": "text",
                    "text": "📊เราได้ทำการตรวจสอบผลงานของคุณเรียบร้อยแล้ว รอรับเงินได้เลยภายใน 15 วัน",
                    "size": "sm",
                    "color": "#202046",
                    "margin": "xl",
                    "wrap": True,
                    "contents": []
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
                        "text": "งานเสร็จสิ้นเรียบร้อย 🎉🎉",
                        "color": "#202046",
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
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "อัพโหลดเอกสารรับเงิน",
                      "uri": "https://www.shoutsolution.com/shouters/line-login?q=bank-account/"
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
                    "text": "📄 Reference",
                    "weight": "regular",
                    "size": "lg",
                    "color": "#002257",
                    "align": "start",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "ตัวอย่างเอกสาร",
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
                    "url": "https://www.img.in.th/images/e7ec9a6df41cd7f95bc818b71aaafcff.png",
                    "align": "center",
                    "gravity": "top",
                    "size": "full",
                    "aspectRatio": "1:1",
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
                      "label": "อัพโหลดเอกสารรับเงิน",
                      "uri": "https://www.shoutsolution.com/shouters/line-login?q=bank-account/"
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
                    "text": "📄 Reference",
                    "weight": "regular",
                    "size": "lg",
                    "color": "#002257",
                    "align": "start",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "ตัวอย่างเอกสาร",
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
                    "url": "https://www.img.in.th/images/1999a58cac32760fe2783dd69aa6fc05.png",
                    "align": "center",
                    "gravity": "top",
                    "size": "full",
                    "aspectRatio": "1:1",
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
                      "label": "อัพโหลดเอกสารรับเงิน",
                      "uri": "https://www.shoutsolution.com/shouters/line-login?q=bank-account/"
                    },
                    "color": "#F37324",
                    "style": "primary"
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

