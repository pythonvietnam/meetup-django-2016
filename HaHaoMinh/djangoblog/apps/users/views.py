from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from .forms import SignUpForm


def sign_in(request):
    return render(request, "signin.html")


def sign_up(request):
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():

            messages.success(request, "Sign up success!")
            return render(request, 'signup_success.html')
        else:
            messages.error(request, "Sign up error!")
    else:
        form = SignUpForm()

    return render(request, "signup.html", {
        'form': form,
    })
