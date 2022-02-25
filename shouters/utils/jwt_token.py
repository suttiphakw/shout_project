import jwt
import datetime

# KEY = U0hPVVRFUl9BQ0NFU1NfVE9LRU5fc2hvdXRzb2x1dGlvbkAyMDIw
# Encode
def encode(data, _id, exp=True):
  if data:
    data['_id'] = _id
  else:
    data = {
      '_id': _id,
    }
  if exp:
    data['exp'] = datetime.datetime.now() + datetime.timedelta(days=1)
  token = jwt.encode(data, 'U0hPVVRFUl9BQ0NFU1NfVE9LRU5fc2hvdXRzb2x1dGlvbkAyMDIw', algorithm='HS256')
  return token

def decode(token):
  decoded_token = jwt.decode(token, 'U0hPVVRFUl9BQ0NFU1NfVE9LRU5fc2hvdXRzb2x1dGlvbkAyMDIw', algorithms='HS256')
  return decoded_token