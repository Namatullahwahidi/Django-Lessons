from django.shortcuts import render, redirect
from django.http import HttpResponse
import matplotlib.pyplot as plot
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from polls.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "base.html")



def Home(request):
    return render(request, "home.html")


# def register_user(request):
#     if request.method=="POST":
#         print("method is post")
#         form=UserCreationForm(request.POST)
#
#         if form.is_valid():
#             print("form is valid")
#             form .save()
#             return  redirect('/account/')
#     else:
#         print("form is invalid")
#         form=UserCreationForm()
#         args={'form':form}
#         return render(request,'account/reg_form.html',args)

# we can use for custom user

def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            args = {'user': request.user}
            return redirect('account:home')
            # return render(request, 'home.html', args)
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'account/reg_form.html', args)



def View_profile(request,pk=None):
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user=request.user
    args = {'user': user}
    return render(request, 'account/profile.html', args)


@login_required
def Edit_Profile(request):
    if request.method == "POST":
        form = EditProfileForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('account:view_profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'account/edit_profile.html', args)


@login_required
def Change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('account:view_profile')
        else:
            return redirect('account:password_change')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'account/password_change.html', args)


def Cart(request):
    return render(request, "cart.html")


def Product(request):
    return render(request, "product.html")


def Category(request):
    return render(request, "category.html")
