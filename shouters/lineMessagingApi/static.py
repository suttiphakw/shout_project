from shouters.models import Shouter

def wait_for_approve_text_message(line_user_id):
    shouter = Shouter.objects.filter(line_user_id=line_user_id).first()

    return {
        "to": line_user_id,
        "messages": [
            {
                "type": "text",
                "text": ' 😊🙏🏻 ขอบคุณคุณ {} ที่ทำการ\nลงทะเบียนเป็น Shouter กับเรา  \n\n '
                        '🙌🏻 ทางทีมงานจะเร่งตรวจสอบข้อมูลบัญชีของคุณ รอผลการตรวจสอบผ่าน Line นี้ได้เลย!'.format(shouter.nickname)
            }
        ]
    }

def wait_for_approve_flex_message(line_user_id):
    shouter = Shouter.objects.filter(line_user_id=line_user_id).first()
    # Get Init Data

    return {
        "to": line_user_id,
        "messages":[
            {
                "type": "flex",
                "altText": "รอการอนุมัติ",
                "contents": {
                    "type": "bubble",
                    "direction": "ltr",
                    "header": {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "xxl",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "none",
                            "margin": "xs",
                            "paddingTop": "6px",
                            "paddingBottom": "6px",
                            "paddingStart": "12px",
                            "width": "180px",
                            "backgroundColor": "#E9EBF1",
                            "cornerRadius": "14px",
                            "contents": [
                            {
                                "type": "text",
                                "text": "รอการตรวจสอบ  + อนุมัติ",
                                "weight": "bold",
                                "size": "sm",
                                "color": "#656C83",
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
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "xl",
                            "position": "relative",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "position": "relative",
                                "width": "64px",
                                "height": "64px",
                                "cornerRadius": "50px",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": shouter.ig_profile_picture,
                                    "backgroundColor": "#000000FF"
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
                                    "text": "@{}".format(shouter.ig_username),
                                    "weight": "bold",
                                    "size": "lg",
                                    "align": "start",
                                    "gravity": "center",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "IG Business Account",
                                    "size": "sm",
                                    "align": "start",
                                    "gravity": "center",
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
                            "spacing": "xxl",
                            "paddingTop": "16px",
                            "paddingBottom": "16px",
                            "contents": [
                            {
                                "type": "text",
                                "text": "ชื่อ",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "{} {}".format(shouter.first_name, shouter.last_name),
                                "flex": 2,
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
                            "paddingBottom": "8px",
                            "contents": [
                            {
                                "type": "text",
                                "text": "Follower",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "{}".format(shouter.ig_follower_count),
                                "flex": 2,
                                "margin": "none",
                                "wrap": False,
                                "contents": []
                            }
                            ]
                        }
                        ]
                    }
                }
            }
        ]
    }

