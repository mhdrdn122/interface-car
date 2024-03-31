from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import SignIn


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def index(request):
    return render(request , "pages/index.html" , {})


@csrf_exempt
def receivData(request):
    if request.method == 'POST':
       
        data = json.loads(request.body.decode('utf-8'))
        value = data.get('value')
        
       
        print(value)

      
        return JsonResponse({'message': 'Value received successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def Reg(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if len(password) < 6:
            return HttpResponse("Password should be at least 6 characters long.")
        else:
            # data = SignIn(username=username , email=email , password=password)
            # data.save()

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return render(request , "pages/index.html" , {})
    else:
        return render(request, 'pages/regestaring.html')   



def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        all_users = User.objects.all()

        user = authenticate(request, username=username, password=password)

        if user is not None:
                login(request, user)
                return render(request, 'pages/index.html')
        else:
                return render(request, 'pages/login.html') 
    else:
        return  render(request, 'pages/login.html') 

