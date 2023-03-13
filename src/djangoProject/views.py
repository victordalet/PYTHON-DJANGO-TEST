from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django import forms

TITLE = "DJANGO PYTHON TEST"

DICO_INFORMATION_INDEX_PAGES = {
    "title": TITLE
}

DICO_INFORMATION_NAV_PAGES = {
    "title": TITLE,
    "error": ""
}


################################### API DISPLAY PICTURE ##########################################

def display_picture():
    lst_img = ""
    for i in range(1, 30):
        lst_img += "<img src='https://inspiranium.fr/cdn/" + str(i) + ".png'>"
    return lst_img


DICO_INFORMATION_INDEX_PAGES['container'] = display_picture()


################################### PAGES ##########################################

def index(request):
    return render(request, "index.html", context=DICO_INFORMATION_INDEX_PAGES)


def formPage(request):
    return render(request, 'form.html', context=DICO_INFORMATION_NAV_PAGES)


@csrf_exempt
def home(request):
    if request.POST:
        if request.POST['email'] == 'victordalet@protonmail.com' and request.POST['password'] == '123':
            return render(request, 'home.html')
        else:
            DICO_INFORMATION_NAV_PAGES['error'] = "EMAIL OR PASSWORD WRONG"
            return render(request, 'form.html', context=DICO_INFORMATION_NAV_PAGES)
    else:
        return render(request, 'index.html', context=DICO_INFORMATION_NAV_PAGES)
