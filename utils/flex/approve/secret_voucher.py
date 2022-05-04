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
        "altText": "📮 งานของคุณได้รับการ Approve แล้ว",
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
                    "backgroundColor": "#038E3F10",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Approved",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#44C350",
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
                    "backgroundColor": "#038E3F10",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ผลการตรวจ = Approved",
                        "weight": "bold",
                        "size": "lg",
                        "color": "#44C350",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "lg",
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
                    "paddingAll": "8px",
                    "backgroundColor": "#FDF7E6FF",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "นำ Draft และ Link ที่ได้รับจากแบรนด์ (อยู่ใน message ด้านบน) ไปโพสท์ลง Story ในวันเวลาที่กำหนด",
                        "size": "xs",
                        "color": "#202046",
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
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "📮 โพสท์งานวันที่",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "04/05/2022",
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
                          "label": "ส่งงาน",
                          "uri": "https://forms.gle/ipWyCtvJm4jQ6ztg6"
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
                            "aspectRatio": "1:1.2",
                            "aspectMode": "fit"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "contents": [
                      {
                        "type": "text",
                        "text": "⚠️ ห้ามนำรูปที่ส่ง Draft ไปโพสท์ ",
                        "size": "xs",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "✅ ให้ Re-Create Story ใหม่ให้ตรงตาม Draft",
                        "size": "xs",
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
                          "label": "ดูรายละเอียดงาน",
                          "uri": "https://forms.gle/ipWyCtvJm4jQ6ztg6"
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
        "altText": "📮 งานของคุณได้รับการ Approve แล้ว",
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
                    "backgroundColor": "#038E3F10",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Approved",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#44C350",
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
                    "backgroundColor": "#038E3F10",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ผลการตรวจ = Approved",
                        "weight": "bold",
                        "size": "lg",
                        "color": "#44C350",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "lg",
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
                    "paddingAll": "8px",
                    "backgroundColor": "#FDF7E6FF",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "นำ Draft และ Link ที่ได้รับจากแบรนด์ (อยู่ใน message ด้านบน) ไปโพสท์ลง Story ในวันเวลาที่กำหนด",
                        "size": "xs",
                        "color": "#202046",
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
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "📮 โพสท์งานวันที่",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "04/05/2022",
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
                          "label": "ส่งงาน",
                          "uri": "https://forms.gle/WvB9VUWwTpDi44GY6"
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
                            "aspectRatio": "1:1.2",
                            "aspectMode": "fit"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "contents": [
                      {
                        "type": "text",
                        "text": "⚠️ ห้ามนำรูปที่ส่ง Draft ไปโพสท์ ",
                        "size": "xs",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "✅ ให้ Re-Create Story ใหม่ให้ตรงตาม Draft",
                        "size": "xs",
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
                          "label": "ดูรายละเอียดงาน",
                          "uri": "https://forms.gle/WvB9VUWwTpDi44GY6"
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