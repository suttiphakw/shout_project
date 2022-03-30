from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Campaign


# Create your views here.
@login_required
def campaign_draft(request):
    user = request.user
    context = {
        'message': user
    }
    return render(request, 'campaigns/draft.html', context)


@login_required
def campaign_in_progress(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'campaigns/draft.html', context)


@login_required
def campaign_finished(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'campaigns/draft.html', context)
