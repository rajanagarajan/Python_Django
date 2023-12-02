from django.http import HttpResponse

def home(request):
    return HttpResponse("This is first response")

def raja(request):
    return HttpResponse("This is Raja's route")

def user(request,name):
    return HttpResponse("This is user "+ name +" route")