from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Campaign


# Create your views here.
@login_required()
def campaign_draft(request):
	user = request.user
	context = {
			'message': user
	}
	return render(request, 'campaigns/draft.html', context)


@login_required()
def campaign_in_progress(request):
	user = request.user
	context = {
			'user': user
	}
	return render(request, 'campaigns/in_progress.html', context)


@login_required()
def campaign_finished(request):
	user = request.user
	context = {
			'user': user
	}
	return render(request, 'campaigns/finished.html', context)


@login_required()
def create_name(request):
	if request.method == 'post':
		campaign_name = request.POST['campaign_name']
		print(campaign_name)
		return render(request, 'campaigns/create/name.html')
	return render(request, 'campaigns/create/name.html')


@login_required()
def create_scope_budget(request):
	return render(request, 'campaigns/create/scope_budget.html')


@login_required()
def create_content_type(request):
	return render(request, 'campaigns/create/content_type.html')


@login_required()
def create_product(request):
	return render(request, 'campaigns/create/product.html')


@login_required()
def create_target(request):
	return render(request, 'campaigns/create/target.html')