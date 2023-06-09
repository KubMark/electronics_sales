from django.urls import path

from users.views import CreateAccountView, UserLoginView, ProfileView, UserLogoutView

urlpatterns = [
    path('signup/', CreateAccountView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

]