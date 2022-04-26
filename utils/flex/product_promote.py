import requests
from shouters.models import Shouter
from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN


def ig_story(line_user_id):
  """ IG Story Only """
  shouter = Shouter.objects.filter(line_user_id=line_user_id).first()
  price = shouter.ig_price_story_fc
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
        "altText": "📍 รายละเอียดงาน (โปรดตอบรับ)",
        "contents": {
          "type": "carousel",
          "contents": [
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
                    "text": "📍 Campaign Detail (รายละเอียดงาน)",
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
                        "text": "สิ่งที่ต้องทำ",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
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
                        "text": "แชร์รูปที่กำหนดให้พร้อมเขียนแคปชันบอกต่อตาม Brief",
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
                    "layout": "baseline",
                    "flex": 1,
                    "spacing": "xxl",
                    "margin": "xxl",
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "💵 เงินที่คุณได้รับ",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "{} บาท".format(price),
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
                    "layout": "baseline",
                    "flex": 1,
                    "spacing": "xxl",
                    "margin": "xxl",
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "⏰ ตอบรับภายในวันที่",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "30/04/2022",
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
                          "label": "ตกลงรับงาน!",
                          "uri": "https://linecorp.com"
                        },
                        "color": "#F37324",
                        "style": "primary",
                        "gravity": "center"
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "md",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "ปฎิเสธ",
                          "uri": "https://linecorp.com"
                        },
                        "color": "#FFFFFFFF",
                        "margin": "none",
                        "style": "secondary"
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
                    "text": "🗓 Timeline (ช่วงเวลาการทำงาน)",
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
                    "layout": "horizontal",
                    "spacing": "xxl",
                    "paddingTop": "16px",
                    "paddingBottom": "16px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "26-30 Apr",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 2,
                        "contents": [
                          {
                            "type": "text",
                            "text": "✅ ตอบรับงาน",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#202046",
                            "flex": 1,
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "(หากไม่ตอบรับภายในเวลา จะถูกปฏิเสธอัตโนมัติ)",
                            "size": "xxs",
                            "color": "#F37324",
                            "wrap": True,
                            "contents": []
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
                        "text": "1-4 May",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 2,
                        "contents": [
                          {
                            "type": "text",
                            "text": "🤳 เริ่มงานและส่งดราฟท์เพื่อตรวจสอบ",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#202046",
                            "flex": 1,
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "md",
                    "paddingTop": "10px",
                    "paddingBottom": "10px",
                    "paddingStart": "10px",
                    "paddingEnd": "10px",
                    "backgroundColor": "#FDF7E6FF",
                    "contents": [
                      {
                        "type": "text",
                        "text": "👩🏻‍💻 รอแบรนด์ Approve งานก่อนลง",
                        "weight": "bold",
                        "size": "sm",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "(หากไม่ผ่าน จะต้องแก้ไขงานส่งใหม่อีก 1 ครั้งตามคอมเมนต์)",
                        "size": "xs",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "xxl",
                    "margin": "lg",
                    "paddingTop": "16px",
                    "paddingBottom": "16px",
                    "paddingStart": "6px",
                    "paddingEnd": "6px",
                    "borderWidth": "1px",
                    "backgroundColor": "#FCF5FCBC",
                    "borderColor": "#852693FF",
                    "cornerRadius": "6px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "4-5 May",
                        "weight": "bold",
                        "size": "md",
                        "color": "#202046",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 2,
                        "contents": [
                          {
                            "type": "text",
                            "text": "🚀 โพสท์งานและส่งงาน",
                            "weight": "bold",
                            "size": "md",
                            "color": "#202046",
                            "flex": 1,
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
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
                        "text": "6-20 May",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 2,
                        "contents": [
                          {
                            "type": "text",
                            "text": "💰 รอรับเงินได้เลย!",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#202046",
                            "flex": 1,
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "(หลังตรวจสอบความเรียบร้อย ไม่เกิน 14 วันหลังเสร็จสิ้น)",
                            "size": "xxs",
                            "color": "#F37324",
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
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "เข้าใจแล้ว เริ่มเลย!",
                          "uri": "https://linecorp.com"
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
                            "url": "https://www.shoutsolution.com/media/source/temp/product_promote.jpg",
                            "size": "full",
                            "aspectRatio": "1:2",
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
                          "uri": "https://linecorp.com"
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
  shouter = Shouter.objects.filter(line_user_id=line_user_id).first()
  price = shouter.ig_fb_price_story_fc
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
        "altText": "📍 รายละเอียดงาน (โปรดตอบรับ)",
        "contents": {
          "type": "carousel",
          "contents": [
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
                    "text": "📍 Campaign Detail (รายละเอียดงาน)",
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
                        "text": "สิ่งที่ต้องทำ",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
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
                        "text": "แชร์รูปที่กำหนดให้พร้อมเขียนแคปชันบอกต่อตาม Brief",
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
                    "layout": "baseline",
                    "flex": 1,
                    "spacing": "xxl",
                    "margin": "xxl",
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "💵 เงินที่คุณได้รับ",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "{} บาท".format(price),
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
                    "layout": "baseline",
                    "flex": 1,
                    "spacing": "xxl",
                    "margin": "xxl",
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "⏰ ตอบรับภายในวันที่",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "30/04/2022",
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
                          "label": "ตกลงรับงาน!",
                          "uri": "https://linecorp.com"
                        },
                        "color": "#F37324",
                        "style": "primary",
                        "gravity": "center"
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "md",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "ปฎิเสธ",
                          "uri": "https://linecorp.com"
                        },
                        "color": "#FFFFFFFF",
                        "margin": "none",
                        "style": "secondary"
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
                    "text": "🗓 Timeline (ช่วงเวลาการทำงาน)",
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
                    "layout": "horizontal",
                    "spacing": "xxl",
                    "paddingTop": "16px",
                    "paddingBottom": "16px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "26-30 Apr",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 2,
                        "contents": [
                          {
                            "type": "text",
                            "text": "✅ ตอบรับงาน",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#202046",
                            "flex": 1,
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "(หากไม่ตอบรับภายในเวลา จะถูกปฏิเสธอัตโนมัติ)",
                            "size": "xxs",
                            "color": "#F37324",
                            "wrap": True,
                            "contents": []
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
                        "text": "1-4 May",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 2,
                        "contents": [
                          {
                            "type": "text",
                            "text": "🤳 เริ่มงานและส่งดราฟท์เพื่อตรวจสอบ",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#202046",
                            "flex": 1,
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "md",
                    "paddingTop": "10px",
                    "paddingBottom": "10px",
                    "paddingStart": "10px",
                    "paddingEnd": "10px",
                    "backgroundColor": "#FDF7E6FF",
                    "contents": [
                      {
                        "type": "text",
                        "text": "👩🏻‍💻 รอแบรนด์ Approve งานก่อนลง",
                        "weight": "bold",
                        "size": "sm",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "(หากไม่ผ่าน จะต้องแก้ไขงานส่งใหม่อีก 1 ครั้งตามคอมเมนต์)",
                        "size": "xs",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "xxl",
                    "margin": "lg",
                    "paddingTop": "16px",
                    "paddingBottom": "16px",
                    "paddingStart": "6px",
                    "paddingEnd": "6px",
                    "borderWidth": "1px",
                    "backgroundColor": "#FCF5FCBC",
                    "borderColor": "#852693FF",
                    "cornerRadius": "6px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "4-5 May",
                        "weight": "bold",
                        "size": "md",
                        "color": "#202046",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 2,
                        "contents": [
                          {
                            "type": "text",
                            "text": "🚀 โพสท์งานและส่งงาน",
                            "weight": "bold",
                            "size": "md",
                            "color": "#202046",
                            "flex": 1,
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
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
                        "text": "6-20 May",
                        "weight": "bold",
                        "size": "xs",
                        "color": "#202046",
                        "flex": 1,
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 2,
                        "contents": [
                          {
                            "type": "text",
                            "text": "💰 รอรับเงินได้เลย!",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#202046",
                            "flex": 1,
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "(หลังตรวจสอบความเรียบร้อย ไม่เกิน 14 วันหลังเสร็จสิ้น)",
                            "size": "xxs",
                            "color": "#F37324",
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
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "เข้าใจแล้ว เริ่มเลย!",
                          "uri": "https://linecorp.com"
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
                            "url": "https://www.shoutsolution.com/media/source/temp/product_promote.jpg",
                            "size": "full",
                            "aspectRatio": "1:2",
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
                          "uri": "https://linecorp.com"
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