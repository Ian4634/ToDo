from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from .models import Goal
from django.contrib.auth.models import User
from . import my_funcs
from django.middleware.csrf import get_token
# Create your views here.


def home(request):
    is_authenticated = request.user.is_authenticated
    username = request.user.username
    if is_authenticated:
        goals = Goal.objects.filter(
            username=User.objects.get(username=username))
        # doing data stuff-------------------------
        after6 = []
        num = 7
        for obj in goals[6:]:

            after6.append([obj, num])
            num += 1
        context = {
            'username': username,
            'goals': goals,  # a list of goal objs,
            'goal_length': len(goals),
            'goals_after_6': after6,
        }
        return render(request, 'Home.html', context)

    else:
        return redirect('/register/login/')

def delete(request):
    name  = request.POST['name']
    discription = request.POST['discription']

    Goal.objects.get(name = name, discription = discription).delete()
    return redirect('/')
def addgoal(request):
    token = get_token(request)
    return render(request, 'addgoal.html', {"token":token})

# csrfmiddlewaretoken=O4UkuwNCei4pRASrgdJOdNFptxL5wAQO196maNyxjTEnGBmThXZeaupVkjwyXjSy&name=a&discription=a&recaptchaResponse=


def creategoal(request):

    goal_name = request.POST['name']
    discription = request.POST['discription']

    new_goal = Goal.objects.create(
        name=goal_name,
        discription=discription,
        username=User.objects.get(username=request.user.username)
    )
    response = HttpResponse('ohoh')
    response.status_code = 200  # sample status code
    return HttpResponse('message sent')


def testing(request):
    return redirect('/')
