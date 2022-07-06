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
        "altText": "📍 คุณได้ปฏิเสธการเข้าร่วม",
        "contents": {
          "type": "carousel",
          "contents": [
            {
              "type": "bubble",
              "direction": "ltr",
              "header": {
                "type": "box",
                "layout": "vertical",
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
                        "layout": "vertical",
                        "paddingAll": "4px",
                        "backgroundColor": "#E541410C",
                        "cornerRadius": "100px",
                        "contents": [
                          {
                            "type": "text",
                            "text": "ปฏิเสธการเข้าร่วม",
                            "size": "sm",
                            "color": "#E34240FF",
                            "align": "center",
                            "contents": []
                          }
                        ]
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
        "altText": "📍 คุณได้ปฏิเสธการเข้าร่วม",
        "contents": {
          "type": "carousel",
          "contents": [
            {
              "type": "bubble",
              "direction": "ltr",
              "header": {
                "type": "box",
                "layout": "vertical",
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
                        "layout": "vertical",
                        "paddingAll": "4px",
                        "backgroundColor": "#E541410C",
                        "cornerRadius": "100px",
                        "contents": [
                          {
                            "type": "text",
                            "text": "ปฏิเสธการเข้าร่วม",
                            "size": "sm",
                            "color": "#E34240FF",
                            "align": "center",
                            "contents": []
                          }
                        ]
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
                            "text": "1 Story",
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