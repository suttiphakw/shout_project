import requests
from shouters.models import Shouter
from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN


def ig_story(line_user_id):
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
                    "width": "105px",
                    "backgroundColor": "#EFB00810",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "รอส่ง Insights",
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
                    "layout": "vertical",
                    "margin": "lg",
                    "paddingBottom": "10px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Next Step",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "flex": 1,
                    "spacing": "xxl",
                    "margin": "xs",
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "📸📊 Capture Insight หลังโพสท์ 24 ชม. และส่งรูปเพื่อเสร็จสิ้นงาน",
                        "size": "xs",
                        "color": "#202046",
                        "wrap": True,
                        "contents": []
                      }
                    ]
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
                        "text": "ภายในวันที่",
                        "size": "xs",
                        "color": "#202046",
                        "align": "start",
                        "gravity": "center",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "06/05/2022",
                        "weight": "bold",
                        "color": "#202046",
                        "flex": 1,
                        "align": "end",
                        "margin": "none",
                        "wrap": False,
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
                          "label": "ส่งรูป Insights",
                          "uri": "https://forms.gle/9H8u9aAbmzqF2nsY9"
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
                    "text": "📮 Capture Insights",
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
                            "url": "https://shoutsolution.com/media/source/campaign/how_to_send_insight.png",
                            "size": "full",
                            "aspectRatio": "1:1.2",
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
                          "label": "ส่งรูป Insights",
                          "uri": "https://forms.gle/9H8u9aAbmzqF2nsY9"
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


def ig_fb_story(line_user_id):
  """ IG and FB Story Only"""
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
                    "width": "105px",
                    "backgroundColor": "#EFB00810",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "รอส่ง Insights",
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
                    "layout": "vertical",
                    "margin": "lg",
                    "paddingBottom": "10px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Next Step",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "flex": 1,
                    "spacing": "xxl",
                    "margin": "xs",
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "📸📊 Capture Insight หลังโพสท์ 24 ชม. และส่งรูปเพื่อเสร็จสิ้นงาน",
                        "size": "xs",
                        "color": "#202046",
                        "wrap": True,
                        "contents": []
                      }
                    ]
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
                        "text": "ภายในวันที่",
                        "size": "xs",
                        "color": "#202046",
                        "align": "start",
                        "gravity": "center",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "06/05/2022",
                        "weight": "bold",
                        "color": "#202046",
                        "flex": 1,
                        "align": "end",
                        "margin": "none",
                        "wrap": False,
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
                          "label": "ส่งรูป Insights",
                          "uri": "https://forms.gle/Ezx3ed7hVzoUhzx88"
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
                    "text": "📮 Capture Insights",
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
                            "url": "https://shoutsolution.com/media/source/campaign/how_to_send_insight.png",
                            "size": "full",
                            "aspectRatio": "1:1.2",
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
                          "label": "ส่งรูป Insights",
                          "uri": "https://forms.gle/Ezx3ed7hVzoUhzx88"
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