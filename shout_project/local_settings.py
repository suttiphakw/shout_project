# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'abcdefghigk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'shoutsolution.com', 'www.shoutsolution.com']

TEMP_HOST = 'https://www.shoutsolution.com/'
LINE_CLIENT_ID = '1656634729'
LINE_CLIENT_SECRET = 'a9123c0aeec0fb3e37fbed8391411930'
FB_CLIENT_ID = '996291567596754'
FB_CLIENT_SECRET = 'b062a622b0c0bcf418d77c6612654b7f'

LINE_CHANNEL_ACCESS_TOKEN = '2vlk1sbdeB/YgPsZlUzFxq647gDOeVBhs+swmUG1XOGFol9YCN48D9I+XD/6gBXqi1j+aSwUcwTS42j1XcDgb2nK0OofFGPyjqHtrC+a/qD0nadY3KGqnvOMBgiEE0Aku/l19AcDAQYgO3V2WnLMZAdB04t89/1O/w1cDnyilFU='

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shout_mvp',
        'USERNAME': 'shoutadmin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
    }
}