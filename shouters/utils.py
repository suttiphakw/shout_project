import requests
import time
import statistics
import numpy as np

from collections import OrderedDict
from django.conf import settings

from utils.predicted_value import PredictedIG, check_is_predicted
from utils.outliers_cut import outlier_cut


def get_json(response, param):
    response_json = response.json()
    data = response_json[param]
    return data

class LineAPI:

    line_url = 'https://access.line.me/oauth2/v2.1/authorize'
    line_client_id = settings.LINE_CLIENT_ID
    line_client_secret = settings.LINE_CLIENT_SECRET
    line_redirect_uri = settings.TEMP_HOST + 'shouters/oauth/'
    line_response_type = 'code'
    line_scope = 'profile%20openid'

    access_token_url = 'https://api.line.me/oauth2/v2.1/token'
    verify_url = 'https://api.line.me/oauth2/v2.1/verify'

    def line_auth(self, state):
        return f'{self.line_url}?response_type={self.line_response_type}&client_id={self.line_client_id}' \
               f'&redirect_uri={self.line_redirect_uri}&state={state}&scope={self.line_scope}'

    def line_auth_form(self, code):
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.line_redirect_uri,
            'client_id': self.line_client_id,
            'client_secret': self.line_client_secret,
        }
        return data

    def line_profile_form(self, id_token):
        data = {
            'id_token': id_token,
            'client_id': self.line_client_id,
        }
        return data

    def get_access_token(self, code):
        response_auth = requests.post(self.access_token_url,
                                      data=self.line_auth_form(code=code))
        access_token = get_json(response=response_auth, param='access_token')
        id_token = get_json(response=response_auth, param='id_token')

        return access_token, id_token

    def get_profile_user(self, id_token):
        response_user = requests.post(self.verify_url,
                                      data=self.line_profile_form(id_token=id_token))

        user_id = get_json(response=response_user, param='sub')
        username = get_json(response=response_user, param='name')
        profile_picture = get_json(response=response_user, param='picture')

        context = {
            'user_id': user_id,
            'username': username,
            'profile_picture': profile_picture
        }

        return context

class FacebookAPI:

    # AUTHENTICATION
    fb_url = 'https://www.facebook.com/v11.0/dialog/oauth'
    fb_client_id = settings.FB_CLIENT_ID
    fb_client_secret = settings.FB_CLIENT_SECRET
    fb_redirect_uri = settings.TEMP_HOST + 'shouters/oauth2/'
    fb_scope = 'instagram_basic,' \
               'instagram_manage_insights,' \
               'pages_show_list,' \
               'pages_read_engagement'

    # SCOPE
    scope_list = ['biography', 'followers_count', 'follows_count', 'media_count', 'username', 'profile_picture_url']
    audience_scope = ['audience_city', 'audience_country', 'audience_gender_age', 'audience_locale', 'online_followers']

    # API URL
    basic_url = 'https://graph.facebook.com/v12.0/'
    basic_url_v3_2 = 'https://graph.facebook.com/v3.2/'
    access_token_url = 'https://graph.facebook.com/v12.0/oauth/access_token'
    page_id_url = 'https://graph.facebook.com/v12.0/me/accounts'

    def fb_auth(self, state):
        return f'{self.fb_url}?client_id={self.fb_client_id}&redirect_uri={self.fb_redirect_uri}' \
               f'&state={state}&scope={self.fb_scope}'

    def fb_auth_form(self, code):
        data = {
            'client_id': self.fb_client_id,
            'redirect_uri': self.fb_redirect_uri,
            'client_secret': self.fb_client_secret,
            'code': code
        }
        return data

    def get_access_token(self, code):
        response_auth = requests.get(self.access_token_url, params=self.fb_auth_form(code))
        if not response_auth.status_code == 200:
            return False

        data = response_auth.json()
        try:
            access_token = get_json(response=response_auth, param='access_token')
        except:
            access_token = ''

        context = {
            'data': data,
            'access_token': access_token
        }
        return context

    def get_facebook_page_id(self, access_token):
        response_page_id = requests.get(self.page_id_url, params={'access_token': access_token})
        if not response_page_id.status_code == 200:
            return False

        data = response_page_id.json()
        try:
            page_id = data['data'][0]['id']
        except:
            page_id = ''

        context = {
            'data': data,
            'page_id': page_id
        }
        return context

    def get_business_account_id(self, page_id, access_token):
        response_business_account_id = requests.get(self.basic_url + page_id,
                                                    params={'fields': 'instagram_business_account',
                                                            'access_token': access_token})
        if not response_business_account_id.status_code == 200:
            return False

        data = response_business_account_id.json()
        try:
            business_account_id = data['instagram_business_account']['id']
        except:
            business_account_id = ''

        context = {
            'data': data,
            'business_account_id': business_account_id
        }
        return context

    def get_ig_biography(self, business_account_id, access_token):
        response_bio = requests.get(self.basic_url_v3_2 + business_account_id,
                                    params={'fields': ','.join(self.scope_list),
                                            'access_token': access_token})
        if not response_bio.status_code == 200:
            return False

        data = response_bio.json()

        try:
            username = get_json(response=response_bio, param='username')
        except:
            username = ''

        try:
            media_count = get_json(response=response_bio, param='media_count')
        except:
            media_count = 0

        try:
            followers = get_json(response=response_bio, param='followers_count')
        except:
            followers = 0

        try:
            followings = get_json(response=response_bio, param='follows_count')
        except:
            followings = 0

        try:
            profile_picture_url = get_json(response=response_bio, param='profile_picture_url')
        except:
            profile_picture_url = ''

        context = {
            'data': data,
            'username': username,
            'media_count': media_count,
            'followers': followers,
            'followings': followings,
            'profile_picture_url': profile_picture_url,
        }
        return context

    def get_ig_media_objects(self, business_account_id, access_token):
        media_object_url = self.basic_url + business_account_id + '/media'
        response_media_objects = requests.get(media_object_url, params={'access_token': access_token})

        if not response_media_objects.status_code == 200:
            return False

        data = response_media_objects.json()
        try:
            media_objects = get_json(response=response_media_objects, param='data')
        except:
            media_objects = ''

        context = {
            'data': data,
            'media_objects': media_objects
        }
        return context

    def get_engagement_insight(self, media_objects, access_token, followers):
        list_like = []
        list_reach = []
        if len(media_objects) >= 20:
            for item in media_objects[0:20]:
                item_detail_url = self.basic_url + item['id']
                item_insight_url = item_detail_url + '/insights'
                response_like_count = requests.get(item_detail_url,
                                                   params={
                                                       'fields': 'like_count',
                                                       'access_token': access_token
                                                   })
                if response_like_count.status_code != 200:
                    list_like.append(0)
                else:
                    list_like.append(get_json(response=response_like_count, param='like_count'))

                response_reach_count = requests.get(item_insight_url,
                                                    params={
                                                        'metric': 'reach',
                                                        'access_token': access_token
                                                    })
                if response_reach_count.status_code != 200:
                    list_reach.append(0)
                else:
                    data = response_reach_count.json()
                    reach = data['data'][0]['values']
                    list_reach.append(reach)

        elif len(media_objects) != 0:
            for item in media_objects[0:len(media_objects)]:
                item_detail_url = self.basic_url + item['id']
                item_insight_url = item_detail_url + '/insights'
                response_like_count = requests.get(item_detail_url,
                                                   params={
                                                       'fields': 'like_count',
                                                       'access_token': access_token
                                                   })
                if response_like_count.status_code != 200:
                    list_like.append(0)
                else:
                    list_like.append(get_json(response=response_like_count, param='like_count'))

                response_reach_count = requests.get(item_insight_url,
                                                    params={
                                                        'metric': 'reach',
                                                        'access_token': access_token
                                                    })
                if response_reach_count.status_code != 200:
                    list_reach.append(0)
                else:
                    data = response_reach_count.json()
                    reach = data['data'][0]['values']
                    list_reach.append(reach)

        # Calculation Like
        if check_is_predicted(list_like):
            average_total_like = PredictedIG().like(followers)
            story_view = PredictedIG().story_view(likes=average_total_like, followers=followers)
            average_post_reach = PredictedIG().post_reach(average_total_like, story_view)
        else:
            outlier = outlier_cut(list_like)
            average_total_like = outlier.get('mean')
            index = outlier.get('used_idx')

            # Calculation Story View
            story_view = PredictedIG().story_view(likes=average_total_like, followers=followers)

            # Calculation Post Reach
            if check_is_predicted(list_reach):
                average_post_reach = PredictedIG().post_reach(average_total_like, story_view)
            else:
                final_list = []
                for idx, value in enumerate(list_reach):
                    if idx not in index:
                        continue
                    else:
                        final_list.append(value)

                average_post_reach = statistics.mean(final_list)

        context = {
            'average_total_like': average_total_like,
            'story_view': story_view,
            'average_post_reach': average_post_reach
        }

        return context

    @staticmethod
    def get_key_audience(json_data, position):
        return json_data['data'][position]['name']

    @staticmethod
    def get_item_audience(json_data, position):
        return json_data['data'][position]['values'][0]['value']

    @staticmethod
    def get_gender_count(item_audience_gender_age, gender):
        return {k: v for k, v in item_audience_gender_age.items() if k[0] == gender}

    @staticmethod
    def get_age_count(item_audience_gender_age, age):
        return {k: v for k, v in item_audience_gender_age.items() if k[2:4] == age}

    @staticmethod
    def get_percentage_audience(item_audience, max_total):
        value = OrderedDict()
        for k, v in sorted(item_audience.items(), key=lambda item: item[1], reverse=True):
            value[k] = round(v * 100 / max_total, 1)
        return value

    def get_audience_insight(self, business_account_id, access_token):
        audience_insight_url = self.basic_url + business_account_id + '/insights'
        response_audience_insight = requests.get(audience_insight_url,
                                                 params={'metric': ','.join(self.audience_scope),
                                                         'period': 'lifetime',
                                                         'access_token': access_token})
        data = response_audience_insight.json()
        return data

        # # Get Data -> Audience City
        # key_audience_city = self.get_key_audience(data, 0)
        # item_audience_city = self.get_item_audience(data, 0)
        # total_audience_city = sum(item_audience_city.values())
        #
        # # Get Data -> Audience Country
        # key_audience_country = self.get_key_audience(data, 1)
        # item_audience_country = self.get_item_audience(data, 1)
        # total_audience_country = sum(item_audience_country.values())
        #
        # # Get Data -> Audience Gender in Age range
        # key_audience_gender_age = self.get_key_audience(data, 2)
        # item_audience_gender_age = self.get_item_audience(data, 2)
        # total_audience_gender_age = sum(item_audience_gender_age.values())
        #
        # # Calculate Max Total
        # max_total = max(total_audience_city, total_audience_country, total_audience_gender_age)
        #
        # # Get Data -> Only Male Gender
        # audience_male_gender = self.get_gender_count(item_audience_gender_age, 'M')
        # total_audience_male_gender = sum(audience_male_gender.values())
        #
        # # Get Data -> Only Female Gender
        # audience_female_gender = self.get_gender_count(item_audience_gender_age, 'F')
        # total_audience_female_gender = sum(audience_female_gender.values())
        #
        # # Get Data -> Only Undefined Gender
        # audience_undefined_gender = self.get_gender_count(item_audience_gender_age, 'U')
        # total_audience_undefined_gender = sum(audience_undefined_gender.values())
        #
        # # Get Data -> Age Range 13-17
        # audience_13_to_17_age = self.get_age_count(item_audience_gender_age, '13')
        # total_audience_13_to_17_age = sum(audience_13_to_17_age.values())
        #
        # # Get Data -> Age Range 18-24
        # audience_18_to_24_age = self.get_age_count(item_audience_gender_age, '18')
        # total_audience_18_to_24_age = sum(audience_18_to_24_age.values())
        #
        # # Get Data -> Age Range 25-34
        # audience_25_to_34_age = self.get_age_count(item_audience_gender_age, '25')
        # total_audience_25_to_34_age = sum(audience_25_to_34_age.values())
        #
        # # Get Data -> Age Range 35-44
        # audience_35_to_44_age = self.get_age_count(item_audience_gender_age, '35')
        # total_audience_35_to_44_age = sum(audience_35_to_44_age.values())
        #
        # # Get Data -> Age Range 45-54
        # audience_45_to_54_age = self.get_age_count(item_audience_gender_age, '45')
        # total_audience_45_to_54_age = sum(audience_45_to_54_age.values())
        #
        # # Get Data -> Age Range 55-64
        # audience_55_to_64_age = self.get_age_count(item_audience_gender_age, '55')
        # total_audience_55_to_64_age = sum(audience_55_to_64_age.values())
        #
        # # Get Data -> Age Range 65+
        # audience_65_up_age = self.get_age_count(item_audience_gender_age, '65')
        # total_audience_65_up_age = sum(audience_65_up_age.values())
        #
        # # Get Dict for see Ordered Audience_city
        # value_audience_city = self.get_percentage_audience(item_audience_city, max_total)
        # value_audience_country = self.get_percentage_audience(item_audience_country, max_total)
        # value_audience_gender_age = self.get_percentage_audience(item_audience_gender_age, max_total)
        #
        # two_most_common_city = {key_audience_city: list(value_audience_city.items())[:2]}
        # two_most_common_country = {key_audience_country: list(value_audience_country.items())[:2]}
        # two_most_common_gender_age = {key_audience_gender_age: list(value_audience_gender_age.items())[:2]}
        #
        # audience_male_percentage = round(
        #     total_audience_male_gender * 100 / (max_total - total_audience_undefined_gender), 1)
        # audience_female_percentage = round(
        #     total_audience_female_gender * 100 / (max_total - total_audience_undefined_gender), 1)
        # audience_age_13_17_percentage = round(total_audience_13_to_17_age * 100 / max_total, 1)
        # audience_age_18_24_percentage = round(total_audience_18_to_24_age * 100 / max_total, 1)
        # audience_age_25_34_percentage = round(total_audience_25_to_34_age * 100 / max_total, 1)
        # audience_age_35_44_percentage = round(total_audience_35_to_44_age * 100 / max_total, 1)
        # audience_age_45_54_percentage = round(total_audience_45_to_54_age * 100 / max_total, 1)
        # audience_age_55_64_percentage = round(total_audience_55_to_64_age * 100 / max_total, 1)
        # audience_age_65_up_percentage = round(total_audience_65_up_age * 100 / max_total, 1)
        #
        # context = {
        #     'insight': data,
        #     'max_total': max_total,
        #     'two_most_common_city': two_most_common_city,
        #     'two_most_common_country': two_most_common_country,
        #     'two_most_common_gender_age': two_most_common_gender_age,
        #     'audience_male_percentage': audience_male_percentage,
        #     'audience_female_percentage': audience_female_percentage,
        #     'audience_age_13_17_percentage': audience_age_13_17_percentage,
        #     'audience_age_18_24_percentage': audience_age_18_24_percentage,
        #     'audience_age_25_34_percentage': audience_age_25_34_percentage,
        #     'audience_age_35_44_percentage': audience_age_35_44_percentage,
        #     'audience_age_45_54_percentage': audience_age_45_54_percentage,
        #     'audience_age_55_64_percentage': audience_age_55_64_percentage,
        #     'audience_age_65_up_percentage': audience_age_65_up_percentage,
        # }
        #
        # return context

    @staticmethod
    def geo_mean_overflow(iterable):
        a = np.log(iterable)
        return np.exp(a.mean())

    def get_active_follower(self, business_account_id, access_token):
        my_list = []
        my_list_2 = []
        unix_time = round(time.time())
        _9_days_before = unix_time - 9 * 86400
        _2_days_before = unix_time - 2 * 86400
        active_follower_url = self.basic_url + business_account_id + '/insights'
        response_active_follower = requests.get(active_follower_url,
                                                params={'metric': 'online_followers',
                                                        'period': 'lifetime',
                                                        'access_token': access_token,
                                                        'since': _9_days_before,
                                                        'until': _2_days_before})

        if not response_active_follower.status_code == 200:
            return False

        data = response_active_follower.json()
        try:
            for value in data['data'][0]['values']:
                mean_1 = sum([value['value']['0'], value['value']['1'], value['value']['2']])
                mean_2 = sum([value['value']['3'], value['value']['4'], value['value']['5']])
                mean_3 = sum([value['value']['6'], value['value']['7'], value['value']['8']])
                mean_4 = sum([value['value']['9'], value['value']['10'], value['value']['11']])
                mean_5 = sum([value['value']['12'], value['value']['13'], value['value']['14']])
                mean_6 = sum([value['value']['15'], value['value']['16'], value['value']['17']])
                mean_7 = sum([value['value']['18'], value['value']['19'], value['value']['20']])
                mean_8 = sum([value['value']['21'], value['value']['22'], value['value']['23']])
                avg = self.geo_mean_overflow([mean_1, mean_2, mean_3, mean_4, mean_5, mean_6, mean_7, mean_8])
                avg_2 = statistics.harmonic_mean([mean_1, mean_2, mean_3, mean_4, mean_5, mean_6, mean_7, mean_8])
                my_list.append(avg)
                my_list_2.append(avg_2)

            geometric_active_follower = statistics.mean(my_list)
            harmonic_active_follower = statistics.mean(my_list_2)
        except:
            response_bio = requests.get(self.basic_url_v3_2 + business_account_id,
                                        params={'fields': ','.join(self.scope_list),
                                                'access_token': access_token})
            followers = get_json(response=response_bio, param='followers_count')
            predicted_active_followers = 0.7 * followers
            geometric_active_follower = predicted_active_followers
            harmonic_active_follower = predicted_active_followers

        context = {
            'data': data,
            'geometric_active_follower': geometric_active_follower,
            'harmonic_active_follower': harmonic_active_follower
        }
        return context
