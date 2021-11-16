from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')

