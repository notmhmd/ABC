from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import UserInfoSerializer
from .models import UserInfo


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new User."""
        serializer.save()
