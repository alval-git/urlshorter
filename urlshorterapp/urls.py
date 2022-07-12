from django.contrib import admin
from django.urls import path, include
from .views import CreateShortUrlView, RedirectDetail, UserUrlsList, SignUp
from django.contrib.auth.decorators import login_required
app_name = 'urlshorterapp'
urlpatterns = [
    path('create/url', CreateShortUrlView, name="create_url"),
    path('<slug:slug>', RedirectDetail.as_view(), name="redirect"),
    path('my/urls/', login_required(UserUrlsList.as_view()), name="user_urls"),
    path('accounts/signup/', SignUp.as_view(), name="signup")
]