from django.conf import settings

#########################################################################
### LINE ###
# AUTHENTICATION
line_authentication_uri = 'https://access.line.me/oauth2/v2.1/authorize'
line_client_id = settings.LINE_CLIENT_ID
line_client_secret = settings.LINE_CLIENT_SECRET
line_redirect_uri = settings.TEMP_HOST + 'shouters/oauth/'
line_response_type = 'code'
line_scope = 'profile%20openid'

# ENDPOINT URI
line_endpoint = 'https://access.line.me/oauth2/v2.1/'

#########################################################################
### FACEBOOK ###
# AUTHENTICATION
fb_authentication_uri = 'https://www.facebook.com/v12.0/dialog/oauth'
fb_client_id = settings.FB_CLIENT_ID
fb_client_secret = settings.FB_CLIENT_SECRET
fb_redirect_uri = settings.TEMP_HOST + 'shouters/oauth2/'
fb_permissions_scope = 'instagram_basic,' \
                       'instagram_manage_insights,' \
                       'pages_show_list,' \
                       'pages_read_engagement'

# SCOPE
ig_bio_scope = ['biography', 'followers_count', 'follows_count', 'media_count', 'username', 'profile_picture_url']
ig_audience_scope = ['audience_city', 'audience_country', 'audience_gender_age', 'audience_locale', 'online_followers']

# ENDPOINT URI
fb_endpoint = 'https://graph.facebook.com/v12.0/'
fb_endpoint_v3_2 = 'https://graph.facebook.com/v3.2/'
#########################################################################