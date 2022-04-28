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
        "altText": "📮 รายละเอียดการส่ง Draft",
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
                    "width": "80px",
                    "backgroundColor": "#038E3F10",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "เริ่มทำงาน",
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
                    "paddingTop": "10px",
                    "paddingBottom": "10px",
                    "paddingStart": "10px",
                    "paddingEnd": "10px",
                    "backgroundColor": "#F3732420",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ต้องส่งดราฟท์ก่อนโพสต์จริง",
                        "weight": "bold",
                        "size": "sm",
                        "color": "#F15626",
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
                        "wrap": True,
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
                    "layout": "vertical",
                    "margin": "lg",
                    "paddingBottom": "10px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "➡️ Next Step",
                        "weight": "bold",
                        "size": "md",
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
                          "label": "รายละเอียด / ส่งงาน",
                          "uri": "https://forms.gle/ahQAAagVDcGmgheT8"
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
                    "text": "📮 Send Draft (ส่งดราฟท์งาน)",
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
                            "url": "https://shoutsolution.com/media/source/campaign/how_to_send_draft.png",
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
                          "label": "รายละเอียด / ส่งงาน",
                          "uri": "https://forms.gle/ahQAAagVDcGmgheT8"
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
                            "url": "https://shoutsolution.com/media/source/temp/product_promote.jpg",
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
                          "label": "รายละเอียด / ส่งงาน",
                          "uri": "https://forms.gle/ahQAAagVDcGmgheT8"
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
        "altText": "📮 รายละเอียดการส่ง Draft",
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
                    "width": "80px",
                    "backgroundColor": "#038E3F10",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "เริ่มทำงาน",
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
                    "paddingTop": "10px",
                    "paddingBottom": "10px",
                    "paddingStart": "10px",
                    "paddingEnd": "10px",
                    "backgroundColor": "#F3732420",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ต้องส่งดราฟท์ก่อนโพสต์จริง",
                        "weight": "bold",
                        "size": "sm",
                        "color": "#F15626",
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
                    "layout": "vertical",
                    "margin": "lg",
                    "paddingBottom": "10px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "➡️ Next Step",
                        "weight": "bold",
                        "size": "md",
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
                          "uri": "https://forms.gle/ahQAAagVDcGmgheT8"
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
                    "text": "📮 Send Draft (ส่งดราฟท์งาน)",
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
                            "url": "https://shoutsolution.com/media/source/campaign/how_to_send_draft.png",
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
                          "label": "รายละเอียด / ส่งงาน",
                          "uri": "https://forms.gle/ahQAAagVDcGmgheT8"
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
                            "url": "https://shoutsolution.com/media/source/temp/product_promote.jpg",
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
                          "label": "รายละเอียด / ส่งงาน",
                          "uri": "https://forms.gle/ahQAAagVDcGmgheT8"
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