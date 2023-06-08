from django.urls import path

from users.views import CreateAccountView, UserLoginView, ProfileView

urlpatterns = [
    path('signup/', CreateAccountView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]