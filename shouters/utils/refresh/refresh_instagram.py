from shouters.utils.instagram import ig_api_bio

def ig_photo(access_token, business_account_id):
  context__ig_biography = ig_api_bio.get(business_account_id, access_token)
  if not context__ig_biography:
    return None
  if 'ig_profile_picture' in context__ig_biography.keys():
    ig_profile_picture = context__ig_biography['ig_profile_picture']
  else:
    ig_profile_picture = None

  return ig_profile_picture