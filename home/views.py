from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render, redirect
from home.forms import HomeForm
from home.models import Post, Friend
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        posts = Post.objects.all().order_by('-updated')
        user = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        args = {
            'form': form,
            'posts': posts,
            'users': user,
            'friends':friends,
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


def Home(request):
    return HttpResponse("Namatullah wahidi")


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')
