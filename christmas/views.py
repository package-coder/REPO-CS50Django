from django.shortcuts import render
import datetime
# Create your views here.

def getDateNow():
    return datetime.datetime.now()

def isItChrismas():
    now = getDateNow()
    return now.month == 12 and now.day == 25


def index(request):
    return render(request, "christmas/index.html", {
        "now": getDateNow(),
        "isChristmas": isItChrismas()
    })