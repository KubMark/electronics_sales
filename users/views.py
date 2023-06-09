from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from users.models import User
from users.serializers import CreateUserSerializer, LoginUserSerializer, ProfileSerializer
from django.urls import reverse


class CreateAccountView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all


class UserLoginView(CreateAPIView):
    serializer_class = LoginUserSerializer

    def create(self, request, *args, **kwargs) -> Response:
        serializer: LoginUserSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)


class ProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all

    def get_object(self):
        return self.request.user


class UserLogoutView(GenericAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all

    def get(self, request):
        logout(request)
        return redirect(reverse('login'))
