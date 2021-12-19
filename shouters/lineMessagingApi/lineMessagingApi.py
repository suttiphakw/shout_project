import requests

from shout_project.settings import LINE_CHANNEL_ACCESS_TOKEN


from . import static


class LineApiMessage:
    push_message_url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(LINE_CHANNEL_ACCESS_TOKEN)
    }

    def api__wait_for_approve_text_message(self, line_user_id):
        data = static.wait_for_approve_text_message(line_user_id=line_user_id)
        try:
            response = requests.post(url=self.push_message_url, headers=self.headers, json=data)
            return response
        except:
            return None

    def api__wait_for_approve_flex_message(self, line_user_id):
        data = static.wait_for_approve_flex_message(line_user_id=line_user_id)
        try:
            response = requests.post(url=self.push_message_url, headers=self.headers, json=data)
            return response
        except:
            return None







