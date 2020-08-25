from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required

from homepage.models import MyUser
from homepage.forms import LoginForm, SignupForm

# Create your views here.


# @login_required
def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username=data.get("username"), password=data.get("password"), age=data.get("age"), bio=data.get("bio"), first_name=data.get("firstname"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})


def permission_error_view(request):
    return HttpResponseRedirect(reverse("permissionerror"))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))