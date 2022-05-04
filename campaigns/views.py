from django.shortcuts import render, redirect, HttpResponse
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
	print(request.method)
	if request.method == 'POST':
		campaign_name = request.POST['campaign_name']
		campaign = Campaign.objects.create(user=request.user, campaign_name=campaign_name)
		campaign.save()
		# Create session => campaign id
		request.session['campaign_id'] = campaign.id

		return redirect('create_scope_budget')
	return render(request, 'campaigns/create/name.html')


@login_required()
def create_scope_budget(request):
	try:
		campaign_id = request.session['campaign_id']
		campaign = Campaign.objects.filter(id=campaign_id).first()
		# Not Found campaign id in session
	except KeyError:
		return HttpResponse('404Error')

	# print(request.session['campaign_id'], request.user)
	if request.method == 'POST':
		# Get List of social media
		campaign_is_ig = request.POST.getlist('is_check_instagram')
		campaign_is_fb = request.POST.getlist('is_check_facebook')

		# Get Budget
		campaign_budget = request.POST['budget']
		# Replace , from budget
		campaign_budget = int(campaign_budget.replace(",", ""))
		campaign_work_type = request.POST['work_type']

		if len(campaign_is_ig) > 0:
			campaign.campaign_is_ig = True
		if len(campaign_is_fb) > 0:
			campaign.campaign_is_fb = True
		campaign.campaign_budget = campaign_budget
		campaign.campaign_work_type = campaign_work_type
		campaign.save()

		return redirect('create_content_type')

	return render(request, 'campaigns/create/scope_budget.html')


@login_required()
def create_content_type(request):
	try:
		campaign_id = request.session['campaign_id']
		campaign = Campaign.objects.filter(id=campaign_id).first()
		# Not Found campaign id in session
	except KeyError:
		return HttpResponse('404Error')

	# Story
	if request.method == 'POST':
		if campaign.campaign_work_type == "story":
			campaign.campaign_content_type_story = request.POST['story_type']
		if campaign.campaign_work_type == "post":
			campaign.campaign_content_type_post = request.POST['post_type']
		if campaign.campaign_work_type == "post_story":
			campaign.campaign_content_type_story = request.POST['story_type']
			campaign.campaign_content_type_post= request.POST['post_type']
		campaign.save()

		return redirect('create_product')

	context = {
		'campaign': campaign
	}
	return render(request, 'campaigns/create/content_type.html', context)


@login_required()
def create_product(request):
	try:
		campaign_id = request.session['campaign_id']
		campaign = Campaign.objects.filter(id=campaign_id).first()
		# Not Found campaign id in session
	except KeyError:
		return HttpResponse('404Error')
	
	if request.method == "POST":
		campaign_product_name = request.POST['product_name']
		campaign_product_photo_1 = request.FILES["product_photo_1"] if "product_photo_1" in request.FILES else False
		campaign_product_photo_2 = request.FILES["product_photo_2"] if "product_photo_2" in request.FILES else False
		campaign_product_photo_3 = request.FILES["product_photo_3"] if "product_photo_3" in request.FILES else False
		campaign_product_detail =  request.POST['product_detail']
		campaign_product_link = request.POST['product_link']

		print(campaign_product_name, campaign_product_photo_1, campaign_product_detail, campaign_product_link)

	context = {
		'campaign': campaign
	}
	return render(request, 'campaigns/create/product.html', context)


@login_required()
def create_target(request):
	return render(request, 'campaigns/create/target.html')