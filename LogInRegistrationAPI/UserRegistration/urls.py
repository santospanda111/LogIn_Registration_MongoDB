from django.urls import path
from UserRegistration import views as UserView

urlpatterns = [
    path('', UserView.Index.as_view(), name='homepage'),
    path('register',UserView.RegisterAPI.as_view(), name='register'),
    path('login', UserView.LogInAPI.as_view(), name='user_login')
]