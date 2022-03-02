from django.shortcuts import render

# Create your views here.
def register(request):
  if request.method == 'POST':
    username = request.POST['email']
    password_1 = request.POST['password_1']
    password_2 = request.POST['password_2']
  return render(request, 'accounts/register.html')

def login(request):
  return render(request, 'accounts/login.html')