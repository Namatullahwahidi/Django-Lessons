from django.urls import path
from django.conf.urls import  url
from django.contrib.auth.views import (
    login,logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)
from . import views

app_name='account'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^$',views.Home,name='home'),
    url(r'^login/$',login,{'template_name':'account/login.html'},name='login'),
    url(r'^logout/$',logout,{'template_name':'account/logout.html'},name='logout'),
    url(r'^register_user/$',views.register_user,name='register_user'),
    url(r'^view_profile/$',views.View_profile,name='view_profile'),
    url(r'^view_profile/(?P<pk>\d+)$',views.View_profile,name='view_profile_with_pk'),
    url(r'^edit_profile/$',views.Edit_Profile,name='edit_profile'),
    url(r'^password_change/$',views.Change_password,name='password_change'),

    url(r'^password_reset/$',password_reset,{'template_name':'account/password_reset.html',
                                             'post_reset_redirect':'account:password_reset_done',
                                             'email_template_name':'account/email_template_name.html'},
                                              name='password_reset'),

    url(r'^password_reset/done/$',password_reset_done,{'template_name':'account/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,{'template_name':'account/password_reset_confirm.html',
                                'post_reset_redirect':'account:password_reset_complete'},name='password_reset_confirm'),

    url(r'^password_reset/complete/$',password_reset_complete,{'template_name':'account/password_reset_complete.html'},
        name='password_reset_complete'),


    path('cart/', views.Cart, name='cart'),
    path('product/', views.Product, name='product'),
    path('category/', views.Category, name='category'),

]