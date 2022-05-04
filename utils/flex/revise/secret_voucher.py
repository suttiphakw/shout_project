import requests
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
        "altText": "📮 งานของคุณได้รับการ Revise จากทางแบรนด์",
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
                    "width": "65px",
                    "backgroundColor": "#EFB00810",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Revise",
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
                        "margin": "lg",
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
                    "margin": "md"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "paddingTop": "10px",
                    "paddingBottom": "10px",
                    "paddingStart": "10px",
                    "paddingEnd": "10px",
                    "backgroundColor": "#F3AB2421",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ผลการตรวจ = แก้งาน",
                        "weight": "bold",
                        "size": "lg",
                        "color": "#F78030FF",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xxl",
                    "contents": [
                      {
                        "type": "text",
                        "text": "รูปแบบการโพสท์",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "flex": 1,
                        "gravity": "center",
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "flex": 1,
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png",
                            "align": "end",
                            "size": "xxs"
                          }
                        ]
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
                        "text": "IG Story",
                        "size": "xs",
                        "color": "#202046",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "1 Story",
                        "weight": "bold",
                        "color": "#202046",
                        "flex": 1,
                        "align": "end",
                        "margin": "none",
                        "wrap": False,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "sm",
                    "paddingBottom": "10px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "สิ่งที่ต้องแก้",
                        "weight": "bold",
                        "size": "md",
                        "color": "#202046",
                        "decoration": "underline",
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "none",
                    "paddingTop": "10px",
                    "paddingBottom": "10px",
                    "paddingStart": "10px",
                    "paddingEnd": "10px",
                    "backgroundColor": "#FDF7E6FF",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "โปรดอ่าน comment จากแบรนด์ ที่ Message ที่ส่งไปด้านบน",
                        "weight": "bold",
                        "size": "sm",
                        "color": "#202046",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      }
                    ]
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
                        "size": "md",
                        "color": "#202046",
                        "decoration": "underline",
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
                        "text": "📮 ส่งดราฟท์ภายใน",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "03/05/2022",
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
                          "label": "รายละเอียด / ส่งงาน",
                          "uri": "https://forms.gle/irLrfwZsQ5P577dj6"
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
                    "text": "📸 Ref.(ตัวอย่างงานที่ต้องการ)",
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
                            "url": "https://shoutsolution.com/media/source/temp/secret_voucher.png",
                            "size": "full",
                            "aspectRatio": "1:1.5",
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
                          "label": "ดูรายละเอียดงาน",
                          "uri": "https://forms.gle/irLrfwZsQ5P577dj6"
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
        "altText": "📮 งานของคุณได้รับการ Revise จากทางแบรนด์",
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
                    "width": "65px",
                    "backgroundColor": "#EFB00810",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Revise",
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
                        "margin": "lg",
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
                    "margin": "md"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "paddingTop": "10px",
                    "paddingBottom": "10px",
                    "paddingStart": "10px",
                    "paddingEnd": "10px",
                    "backgroundColor": "#F3AB2421",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ผลการตรวจ = แก้งาน",
                        "weight": "bold",
                        "size": "lg",
                        "color": "#F78030FF",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xxl",
                    "contents": [
                      {
                        "type": "text",
                        "text": "รูปแบบการโพสท์",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "flex": 1,
                        "gravity": "center",
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "flex": 1,
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png",
                            "align": "end",
                            "size": "xxs"
                          },
                          {
                            "type": "image",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Facebook_Logo_(2019).png/1200px-Facebook_Logo_(2019).png",
                            "align": "end",
                            "size": "xxs"
                          }
                        ]
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
                        "text": "IG + FB Story",
                        "size": "xs",
                        "color": "#202046",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "1 Story",
                        "weight": "bold",
                        "color": "#202046",
                        "flex": 1,
                        "align": "end",
                        "margin": "none",
                        "wrap": False,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "sm",
                    "paddingBottom": "10px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "สิ่งที่ต้องแก้",
                        "weight": "bold",
                        "size": "md",
                        "color": "#202046",
                        "decoration": "underline",
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "none",
                    "paddingTop": "10px",
                    "paddingBottom": "10px",
                    "paddingStart": "10px",
                    "paddingEnd": "10px",
                    "backgroundColor": "#FDF7E6FF",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "โปรดอ่าน comment จากแบรนด์ ที่ Message ที่ส่งไปด้านบน",
                        "weight": "bold",
                        "size": "sm",
                        "color": "#202046",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      }
                    ]
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
                        "size": "md",
                        "color": "#202046",
                        "decoration": "underline",
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
                        "text": "📮 ส่งดราฟท์ภายใน",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "03/05/2022",
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
                          "label": "รายละเอียด / ส่งงาน",
                          "uri": "https://forms.gle/irLrfwZsQ5P577dj6"
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
                    "text": "📸 Ref.(ตัวอย่างงานที่ต้องการ)",
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
                            "url": "https://shoutsolution.com/media/source/temp/secret_voucher.png",
                            "size": "full",
                            "aspectRatio": "1:1.5",
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
                          "label": "ดูรายละเอียดงาน",
                          "uri": "https://forms.gle/irLrfwZsQ5P577dj6"
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