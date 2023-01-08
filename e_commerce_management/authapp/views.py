from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


# @login_required(login_url='/login')
def home(request):

   
    return render(request, 'layout.html')





def signup(request):
    if request.POST:
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        passwordr=request.POST.get('passwordr')
        if password == passwordr:
            pass
        else:
            context={
                'type':'error',
                'msg':'Password mouch kif kif'
            }
            return render(request, 'registration/msg.html',context)
        try:
            user = User.objects.create_user(username, email, password)
            context={
                'type':'suc',
                'msg':' User tsajel jawou behi'
            }
            return render(request, 'registration/msg.html',context)

        except:
            context={
                'type':'error',
                'msg':' User me tsajilch!!!'
            }
            return render(request, 'registration/msg.html',context)
   
    return render(request, 'registration/signup.html')

