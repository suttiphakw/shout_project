import requests

from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN


def ig(line_user_id, context):
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
        "altText": "📍 กำลังทำงาน",
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
                            "text": "กำลังทำงาน",
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
                    "type": "box",
                    "layout": "vertical",
                    "margin": "md",
                    "paddingAll": "8px",
                    "backgroundColor": "#F3732428",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ต้องส่งดราฟท์ก่อนโพสต์จริง",
                        "size": "sm",
                        "color": "#F15626",
                        "align": "center",
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "separator",
                    "margin": "xl"
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
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "lg",
                        "paddingBottom": "8px",
                        "contents": [
                          {
                            "type": "text",
                            "text": "ส่งดราฟท์ภายใน",
                            "weight": "regular",
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
                            "align": "end",
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
                      "label": "ส่งดราฟท์",
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
                    "text": "📮 Send Draft",
                    "weight": "regular",
                    "size": "lg",
                    "color": "#002257",
                    "align": "start",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "ส่งดราฟท์งาน",
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
                    "url": "https://www.img.in.th/images/25eaee62850fa87844409d8f535a01f2.png",
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
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "ส่งดราฟท์",
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
                      "label": "ส่งดราฟท์",
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


def ig_fb(line_user_id, context):
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
        "altText": "📍 กำลังทำงาน",
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
                            "text": "กำลังทำงาน",
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
                        "text": "{}".format(context['sent_date']),
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
                    "type": "box",
                    "layout": "vertical",
                    "margin": "md",
                    "paddingAll": "8px",
                    "backgroundColor": "#F3732428",
                    "cornerRadius": "8px",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ต้องส่งดราฟท์ก่อนโพสต์จริง",
                        "size": "sm",
                        "color": "#F15626",
                        "align": "center",
                        "contents": []
                      }
                    ]
                  },
                  {
                    "type": "separator",
                    "margin": "xl"
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
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "lg",
                        "paddingBottom": "8px",
                        "contents": [
                          {
                            "type": "text",
                            "text": "ส่งดราฟท์ภายใน",
                            "weight": "regular",
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
                            "align": "end",
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
                      "label": "ส่งดราฟท์",
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
                    "text": "📮 Send Draft",
                    "weight": "regular",
                    "size": "lg",
                    "color": "#002257",
                    "align": "start",
                    "margin": "none",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "ส่งดราฟท์งาน",
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
                    "url": "https://www.img.in.th/images/25eaee62850fa87844409d8f535a01f2.png",
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
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "ส่งดราฟท์",
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
                      "label": "ส่งดราฟท์",
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
