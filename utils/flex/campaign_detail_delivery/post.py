import requests

from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN


def ig(line_user_id, price, context):
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
        "altText": "📍 รายละเอียดงาน (โปรดตอบรับ)",
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
                    "type": "text",
                    "text": "📍 Campaign Detail",
                    "size": "lg",
                    "color": "#202046FF",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "รายละเอียดงาน",
                    "weight": "regular",
                    "size": "sm",
                    "color": "#8A8AA0FF",
                    "align": "start",
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
                    "type": "box",
                    "layout": "vertical",
                    "margin": "sm",
                    "paddingTop": "8px",
                    "contents": [
                      {
                        "type": "image",
                        "url": "{}".format(context['campaign_picture']),
                        "size": "full",
                        "aspectRatio": "2:1"
                      },
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
                    "margin": "xxl",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "รูปแบบการโพสต์",
                            "weight": "regular",
                            "size": "sm",
                            "color": "#8A8AA0FF",
                            "flex": 1,
                            "gravity": "center",
                            "contents": []
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "md",
                        "position": "relative",
                        "contents": [
                          {
                            "type": "text",
                            "text": "{}".format(context['work_type_text']),
                            "color": "#202046",
                            "gravity": "center",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "{}".format(context['post_count']),
                            "weight": "regular",
                            "color": "#202046",
                            "align": "end",
                            "gravity": "center",
                            "margin": "none",
                            "wrap": False,
                            "contents": []
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                          {
                            "type": "icon",
                            "url": "https://webstockreview.net/images600_/information-clipart-transparent-19.png",
                            "size": "lg"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xl",
                    "paddingBottom": "10px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "สิ่งที่ต้องทำ",
                        "weight": "regular",
                        "size": "sm",
                        "color": "#8A8AA0FF",
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "{}".format(context['text']),
                            "weight": "regular",
                            "size": "md",
                            "color": "#202046",
                            "align": "start",
                            "gravity": "center",
                            "margin": "lg",
                            "wrap": True,
                            "contents": []
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator",
                    "margin": "xl"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xxl",
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "💵 เงินที่คุณได้รับ",
                        "weight": "regular",
                        "size": "sm",
                        "color": "#8A8AA0FF",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "{} บาท".format(price),
                        "weight": "regular",
                        "size": "md",
                        "color": "#202046",
                        "flex": 1,
                        "align": "end",
                        "margin": "md",
                        "wrap": False,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "md",
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "⏰ ตอบรับภายใน",
                        "weight": "regular",
                        "size": "sm",
                        "color": "#8A8AA0FF",
                        "align": "start",
                        "gravity": "center",
                        "margin": "none",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "{}".format(context['accept_date']),
                        "weight": "regular",
                        "size": "md",
                        "color": "#202046",
                        "flex": 1,
                        "align": "end",
                        "gravity": "center",
                        "margin": "md",
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
                      "label": "ดูรายละเอียด",
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
                    "text": "🗓 Timeline",
                    "weight": "regular",
                    "size": "lg",
                    "color": "#002257",
                    "align": "start",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "ช่วงเวลาการทำงาน",
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
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "none",
                            "margin": "none",
                            "contents": [
                              {
                                "type": "text",
                                "text": "✅",
                                "size": "xl",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "flex": 1,
                            "contents": [
                              {
                                "type": "separator",
                                "margin": "md",
                                "color": "#8A8AA0FF"
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 6,
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "paddingAll": "4px",
                            "width": "100px",
                            "borderWidth": "1px",
                            "borderColor": "#CFD2DAFF",
                            "cornerRadius": "8px",
                            "contents": [
                              {
                                "type": "text",
                                "text": "{}".format(context['accept_work_date']),
                                "weight": "regular",
                                "size": "xs",
                                "color": "#202046",
                                "align": "center",
                                "style": "normal",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "text",
                            "text": "ตอบรับงาน",
                            "weight": "regular",
                            "color": "#202046",
                            "align": "start",
                            "margin": "lg",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "หากไม่ตอบรับภายในเวลา จะถูกปฏิเสธอัตโนมัติ",
                            "size": "xxs",
                            "color": "#EE312B",
                            "margin": "sm",
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
                    "margin": "xl",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "none",
                            "margin": "none",
                            "contents": [
                              {
                                "type": "text",
                                "text": "🚚",
                                "size": "xl",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "flex": 1,
                            "contents": [
                              {
                                "type": "separator",
                                "margin": "md",
                                "color": "#8A8AA0FF"
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 6,
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "paddingAll": "4px",
                            "width": "100px",
                            "borderWidth": "1px",
                            "borderColor": "#CFD2DAFF",
                            "cornerRadius": "8px",
                            "contents": [
                              {
                                "type": "text",
                                "text": "{}".format(context['wait_delivery_date']),
                                "weight": "regular",
                                "size": "xs",
                                "color": "#202046",
                                "align": "center",
                                "style": "normal",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "text",
                            "text": "รอจัดส่งสินค้า",
                            "weight": "regular",
                            "color": "#202046",
                            "align": "start",
                            "margin": "lg",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "เมื่อได้รับสินค้าแล้ว โปรดกดยืนยันการรับสินค้า",
                            "size": "xxs",
                            "color": "#202046AA",
                            "margin": "sm",
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
                    "margin": "xl",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "none",
                            "margin": "none",
                            "contents": [
                              {
                                "type": "text",
                                "text": "🤳",
                                "size": "xl",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "flex": 1,
                            "contents": [
                              {
                                "type": "separator",
                                "margin": "md",
                                "color": "#8A8AA0FF"
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 6,
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "paddingAll": "4px",
                            "width": "100px",
                            "borderWidth": "1px",
                            "borderColor": "#CFD2DAFF",
                            "cornerRadius": "8px",
                            "contents": [
                              {
                                "type": "text",
                                "text": "{}".format(context['start_work_date']),
                                "weight": "regular",
                                "size": "xs",
                                "color": "#202046",
                                "align": "center",
                                "style": "normal",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "text",
                            "text": "เริ่มงานและส่งดราฟท์เพื่อตรวจสอบ",
                            "weight": "regular",
                            "color": "#202046",
                            "align": "start",
                            "margin": "lg",
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
                    "margin": "xl",
                    "paddingTop": "16px",
                    "paddingBottom": "16px",
                    "paddingStart": "10px",
                    "paddingEnd": "10px",
                    "backgroundColor": "#E9EBF1",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "👩🏻‍💻 รอแบรนด์ Approve งานก่อนลง",
                        "weight": "regular",
                        "color": "#202046FF",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "(หากไม่ผ่าน จะต้องแก้ไขงานส่งใหม่อีก 1 ครั้งตามคอมเมนต์)",
                        "size": "xxs",
                        "color": "#202046",
                        "align": "center",
                        "margin": "sm",
                        "wrap": True,
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
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "none",
                            "margin": "none",
                            "contents": [
                              {
                                "type": "text",
                                "text": "🚀",
                                "size": "xl",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "flex": 1,
                            "contents": [
                              {
                                "type": "separator",
                                "margin": "md",
                                "color": "#8A8AA0FF"
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 6,
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "paddingAll": "4px",
                            "width": "100px",
                            "borderWidth": "1px",
                            "backgroundColor": "#F8F0F6",
                            "borderColor": "#AB6E9D",
                            "cornerRadius": "8px",
                            "contents": [
                              {
                                "type": "text",
                                "text": "{}".format(context['post_date']),
                                "weight": "regular",
                                "size": "xs",
                                "color": "#202046",
                                "align": "center",
                                "style": "normal",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "text",
                            "text": "โพสต์งาน และส่ง Link งาน",
                            "weight": "regular",
                            "color": "#202046",
                            "align": "start",
                            "margin": "lg",
                            "wrap": True,
                            "contents": []
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
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xl",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "none",
                            "margin": "none",
                            "contents": [
                              {
                                "type": "text",
                                "text": "💰",
                                "size": "xl",
                                "contents": []
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 6,
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "paddingAll": "4px",
                            "width": "100px",
                            "borderWidth": "1px",
                            "borderColor": "#CFD2DAFF",
                            "cornerRadius": "8px",
                            "contents": [
                              {
                                "type": "text",
                                "text": "{}".format(context['payment_date']),
                                "weight": "regular",
                                "size": "xs",
                                "color": "#202046",
                                "align": "center",
                                "style": "normal",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "text",
                            "text": "รอรับเงินได้เลย!",
                            "weight": "regular",
                            "color": "#202046",
                            "align": "start",
                            "margin": "lg",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "หลังตรวจสอบความเรียบร้อย ไม่เกิน 7 วันหลังเสร็จสิ้น",
                            "size": "xxs",
                            "color": "#202046AA",
                            "margin": "sm",
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
                      "label": "ดูรายละเอียด",
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
                    "text": "📸 Reference",
                    "weight": "regular",
                    "size": "lg",
                    "color": "#002257",
                    "align": "start",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "ตัวอย่างงานที่ต้องการ",
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
                    "url": "{}".format(context['reference_picture']),
                    "align": "center",
                    "gravity": "top",
                    "size": "full",
                    "aspectRatio": "1:2",
                    "aspectMode": "fit"
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
                      "label": "ดูรายละเอียด",
                      "uri": "{}".format(context['google_form_link']),
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


def ig_fb(line_user_id, price, context):
  """ IG + FB """
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
                "layout": "vertical",
                "spacing": "xs",
                "paddingBottom": "2px",
                "borderColor": "#4B2828FF",
                "contents": [
                  {
                    "type": "text",
                    "text": "📍 Campaign Detail",
                    "size": "lg",
                    "color": "#202046FF",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "รายละเอียดงาน",
                    "weight": "regular",
                    "size": "sm",
                    "color": "#8A8AA0FF",
                    "align": "start",
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
                    "type": "box",
                    "layout": "vertical",
                    "margin": "sm",
                    "paddingTop": "8px",
                    "contents": [
                      {
                        "type": "image",
                        "url": "{}".format(context['campaign_picture']),
                        "size": "full",
                        "aspectRatio": "2:1"
                      },
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
                    "margin": "xxl",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "text",
                            "text": "รูปแบบการโพสต์",
                            "weight": "regular",
                            "size": "sm",
                            "color": "#8A8AA0FF",
                            "flex": 1,
                            "gravity": "center",
                            "contents": []
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "md",
                        "position": "relative",
                        "contents": [
                          {
                            "type": "text",
                            "text": "{}".format(context['work_type_text']),
                            "color": "#202046",
                            "gravity": "center",
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "{}".format(context['post_count']),
                            "weight": "regular",
                            "color": "#202046",
                            "align": "end",
                            "gravity": "center",
                            "margin": "none",
                            "wrap": False,
                            "contents": []
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "md",
                        "margin": "md",
                        "contents": [
                          {
                            "type": "icon",
                            "url": "https://webstockreview.net/images600_/information-clipart-transparent-19.png",
                            "margin": "md",
                            "size": "lg"
                          },
                          {
                            "type": "icon",
                            "url": "https://1.bp.blogspot.com/-S8HTBQqmfcs/XN0ACIRD9PI/AAAAAAAAAlo/FLhccuLdMfIFLhocRjWqsr9cVGdTN_8sgCPcBGAYYCw/s1600/f_logo_RGB-Blue_1024.png",
                            "margin": "md",
                            "size": "lg"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xl",
                    "paddingBottom": "10px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "สิ่งที่ต้องทำ",
                        "weight": "regular",
                        "size": "sm",
                        "color": "#8A8AA0FF",
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "{}".format(context['text']),
                            "weight": "regular",
                            "size": "md",
                            "color": "#202046",
                            "align": "start",
                            "gravity": "center",
                            "margin": "lg",
                            "wrap": True,
                            "contents": []
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator",
                    "margin": "xl"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xxl",
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "💵 เงินที่คุณได้รับ",
                        "weight": "regular",
                        "size": "sm",
                        "color": "#8A8AA0FF",
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "{} บาท".format(price),
                        "weight": "regular",
                        "size": "md",
                        "color": "#202046",
                        "flex": 1,
                        "align": "end",
                        "margin": "md",
                        "wrap": False,
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "md",
                    "paddingBottom": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "⏰ ตอบรับภายใน",
                        "weight": "regular",
                        "size": "sm",
                        "color": "#8A8AA0FF",
                        "align": "start",
                        "gravity": "center",
                        "margin": "none",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "{}".format(context['accept_date']),
                        "weight": "regular",
                        "size": "md",
                        "color": "#202046",
                        "flex": 1,
                        "align": "end",
                        "gravity": "center",
                        "margin": "md",
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
                      "label": "ดูรายละเอียด",
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
                    "text": "🗓 Timeline",
                    "weight": "regular",
                    "size": "lg",
                    "color": "#002257",
                    "align": "start",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "ช่วงเวลาการทำงาน",
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
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "none",
                            "margin": "none",
                            "contents": [
                              {
                                "type": "text",
                                "text": "✅",
                                "size": "xl",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "flex": 1,
                            "contents": [
                              {
                                "type": "separator",
                                "margin": "md",
                                "color": "#8A8AA0FF"
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 6,
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "paddingAll": "4px",
                            "width": "100px",
                            "borderWidth": "1px",
                            "borderColor": "#CFD2DAFF",
                            "cornerRadius": "8px",
                            "contents": [
                              {
                                "type": "text",
                                "text": "{}".format(context['accept_work_date']),
                                "weight": "regular",
                                "size": "xs",
                                "color": "#202046",
                                "align": "center",
                                "style": "normal",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "text",
                            "text": "ตอบรับงาน",
                            "weight": "regular",
                            "color": "#202046",
                            "align": "start",
                            "margin": "lg",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "หากไม่ตอบรับภายในเวลา จะถูกปฏิเสธอัตโนมัติ",
                            "size": "xxs",
                            "color": "#EE312B",
                            "margin": "sm",
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
                    "margin": "xl",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "none",
                            "margin": "none",
                            "contents": [
                              {
                                "type": "text",
                                "text": "🚚",
                                "size": "xl",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "flex": 1,
                            "contents": [
                              {
                                "type": "separator",
                                "margin": "md",
                                "color": "#8A8AA0FF"
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 6,
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "paddingAll": "4px",
                            "width": "100px",
                            "borderWidth": "1px",
                            "borderColor": "#CFD2DAFF",
                            "cornerRadius": "8px",
                            "contents": [
                              {
                                "type": "text",
                                "text": "{}".format(context['wait_delivery_date']),
                                "weight": "regular",
                                "size": "xs",
                                "color": "#202046",
                                "align": "center",
                                "style": "normal",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "text",
                            "text": "รอจัดส่งสินค้า",
                            "weight": "regular",
                            "color": "#202046",
                            "align": "start",
                            "margin": "lg",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "เมื่อได้รับสินค้าแล้ว โปรดกดยืนยันการรับสินค้า",
                            "size": "xxs",
                            "color": "#202046AA",
                            "margin": "sm",
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
                    "margin": "xl",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "none",
                            "margin": "none",
                            "contents": [
                              {
                                "type": "text",
                                "text": "🤳",
                                "size": "xl",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "flex": 1,
                            "contents": [
                              {
                                "type": "separator",
                                "margin": "md",
                                "color": "#8A8AA0FF"
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 6,
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "paddingAll": "4px",
                            "width": "100px",
                            "borderWidth": "1px",
                            "borderColor": "#CFD2DAFF",
                            "cornerRadius": "8px",
                            "contents": [
                              {
                                "type": "text",
                                "text": "{}".format(context['start_work_date']),
                                "weight": "regular",
                                "size": "xs",
                                "color": "#202046",
                                "align": "center",
                                "style": "normal",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "text",
                            "text": "เริ่มงานและส่งดราฟท์เพื่อตรวจสอบ",
                            "weight": "regular",
                            "color": "#202046",
                            "align": "start",
                            "margin": "lg",
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
                    "margin": "xl",
                    "paddingTop": "16px",
                    "paddingBottom": "16px",
                    "paddingStart": "10px",
                    "paddingEnd": "10px",
                    "backgroundColor": "#E9EBF1",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "👩🏻‍💻 รอแบรนด์ Approve งานก่อนลง",
                        "weight": "regular",
                        "color": "#202046FF",
                        "align": "center",
                        "wrap": True,
                        "contents": []
                      },
                      {
                        "type": "text",
                        "text": "(หากไม่ผ่าน จะต้องแก้ไขงานส่งใหม่อีก 1 ครั้งตามคอมเมนต์)",
                        "size": "xxs",
                        "color": "#202046",
                        "align": "center",
                        "margin": "sm",
                        "wrap": True,
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
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "none",
                            "margin": "none",
                            "contents": [
                              {
                                "type": "text",
                                "text": "🚀",
                                "size": "xl",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "flex": 1,
                            "contents": [
                              {
                                "type": "separator",
                                "margin": "md",
                                "color": "#8A8AA0FF"
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 6,
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "paddingAll": "4px",
                            "width": "100px",
                            "borderWidth": "1px",
                            "backgroundColor": "#F8F0F6",
                            "borderColor": "#AB6E9D",
                            "cornerRadius": "8px",
                            "contents": [
                              {
                                "type": "text",
                                "text": "{}".format(context['post_date']),
                                "weight": "regular",
                                "size": "xs",
                                "color": "#202046",
                                "align": "center",
                                "style": "normal",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "text",
                            "text": "โพสต์งาน และส่ง Link งาน",
                            "weight": "regular",
                            "color": "#202046",
                            "align": "start",
                            "margin": "lg",
                            "wrap": True,
                            "contents": []
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
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xl",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "none",
                            "margin": "none",
                            "contents": [
                              {
                                "type": "text",
                                "text": "💰",
                                "size": "xl",
                                "contents": []
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 6,
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "paddingAll": "4px",
                            "width": "100px",
                            "borderWidth": "1px",
                            "borderColor": "#CFD2DAFF",
                            "cornerRadius": "8px",
                            "contents": [
                              {
                                "type": "text",
                                "text": "{}".format(context['payment_date']),
                                "weight": "regular",
                                "size": "xs",
                                "color": "#202046",
                                "align": "center",
                                "style": "normal",
                                "contents": []
                              }
                            ]
                          },
                          {
                            "type": "text",
                            "text": "รอรับเงินได้เลย!",
                            "weight": "regular",
                            "color": "#202046",
                            "align": "start",
                            "margin": "lg",
                            "wrap": True,
                            "contents": []
                          },
                          {
                            "type": "text",
                            "text": "หลังตรวจสอบความเรียบร้อย ไม่เกิน 7 วันหลังเสร็จสิ้น",
                            "size": "xxs",
                            "color": "#202046AA",
                            "margin": "sm",
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
                      "label": "ดูรายละเอียด",
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
                    "text": "📸 Reference",
                    "weight": "regular",
                    "size": "lg",
                    "color": "#002257",
                    "align": "start",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "ตัวอย่างงานที่ต้องการ",
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
                    "url": "{}".format(context['reference_picture']),
                    "align": "center",
                    "gravity": "top",
                    "size": "full",
                    "aspectRatio": "1:2",
                    "aspectMode": "fit"
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
                      "label": "ดูรายละเอียด",
                      "uri": "{}".format(context['google_form_link']),
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