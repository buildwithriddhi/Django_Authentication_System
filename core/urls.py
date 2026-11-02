from django.urls import path, include
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('',include('django.contrib.auth.urls')),
    path('secret_page',views.secret_page,name='secret_page')
]