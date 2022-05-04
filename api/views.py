from django.shortcuts import render
from shouters.models import Shouter
from shouters.utils.instagram.ig_api_get_story_list import get as get_list
from shouters.utils.instagram.ig_api_get_permalink_story import get as get_id
from shouters.utils.instagram.ig_api_get_story_insights import get as get_insights

# Create your views here.
def insights(request):
  if request.method == "POST":
    url = request.POST['url']
    ig_username = request.POST['ig_username']

    shouter = Shouter.objects.filter(ig_username=ig_username).first()
    business_account_id = shouter.ig_business_account_id
    access_token = shouter.fb_main_access_token

    # Find Story ID
    context_list = get_list(business_account_id, access_token)
    if not context_list:
      return render(request, 'api/insights_form.html')
    story_list = context_list['data']

    # For Loop
    story_id = get_id(story_list, access_token, url)
    if not story_id:
      return render(request, 'api/insights_form.html')

    # Get Insights
    insight = get_insights(story_id, access_token)

    context = {}

    for obj in insight:
      context[obj['name']] = obj['values'][0]['value']

    return render(request, 'api/insights_form.html', context)

  return render(request, 'api/insights_form.html')