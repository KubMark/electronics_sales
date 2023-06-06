from django.urls import path

from users.views import CreateAccountView, UserLoginView

urlpatterns = [
    path('signup', CreateAccountView.as_view(), name='signup'),
    path('login', UserLoginView.as_view(), name='login'),
]