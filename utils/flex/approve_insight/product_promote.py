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
        "altText": "📮 Insights ของคุณได้รับการ Approve แล้ว",
        "contents": {
          "type": "carousel",
          "contents": [
            {
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
                    "width": "85px",
                    "backgroundColor": "#22A2142D",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Complete",
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
                            "text": "Shopee - Product Promote",
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
                    "layout": "vertical",
                    "margin": "lg",
                    "contents": [
                      {
                        "type": "text",
                        "text": "📊เราได้ทำการตรวจสอบ Insight ของคุณเรียบร้อยแล้ว รอรับเงินได้เลยไม่เกิน 7 วัน",
                        "weight": "bold",
                        "size": "sm",
                        "align": "start",
                        "wrap": True,
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
                        "text": "งานเสร็จสิ้นเรียบร้อย 🎉🎉",
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
              },
              "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "Upload เอกสาร",
                          "uri": "https://shoutsolution.com/shouters/line-login?q=bank-account/"
                        },
                        "color": "#F37324",
                        "style": "primary",
                        "gravity": "center"
                      }
                    ]
                  }
                ]
              }
            },
            {
              "type": "bubble",
              "direction": "ltr",
              "header": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "xxl",
                "paddingBottom": "2px",
                "borderColor": "#4B2828FF",
                "contents": [
                  {
                    "type": "text",
                    "text": "📸 Ref.(ตัวอย่างเอกสาร)",
                    "weight": "bold",
                    "size": "sm",
                    "color": "#002257",
                    "margin": "none",
                    "contents": []
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
                    "paddingTop": "15px",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://shoutsolution.com/media/source/ref/id_card.png",
                            "size": "full",
                            "aspectRatio": "1:1",
                            "aspectMode": "fit"
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
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "Upload เอกสาร",
                          "uri": "https://shoutsolution.com/shouters/line-login?q=bank-account/"
                        },
                        "color": "#F37324",
                        "style": "primary",
                        "gravity": "center"
                      }
                    ]
                  }
                ]
              }
            },
            {
              "type": "bubble",
              "direction": "ltr",
              "header": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "xxl",
                "paddingBottom": "2px",
                "borderColor": "#4B2828FF",
                "contents": [
                  {
                    "type": "text",
                    "text": "📸 Ref.(ตัวอย่างเอกสาร)",
                    "weight": "bold",
                    "size": "sm",
                    "color": "#002257",
                    "margin": "none",
                    "contents": []
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
                    "paddingTop": "15px",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://shoutsolution.com/media/source/ref/book_bank.png",
                            "size": "full",
                            "aspectRatio": "1:1",
                            "aspectMode": "fit"
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
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "Upload เอกสาร",
                          "uri": "https://shoutsolution.com/shouters/line-login?q=bank-account/"
                        },
                        "color": "#F37324",
                        "style": "primary",
                        "gravity": "center"
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
  except:
    return None
