import uuid

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import views, permissions, status
from rest_framework import generics
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import ORMUser
# Create your views here.

class UserLogoutAllView(views.APIView):
    """
    Use this endpoint to log out all sessions for a given user
    """

    permission_classes =[permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = uuid.uuid4()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    serializer_class = UserSerializer
    queryset = ORMUser.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = {'user_id': self.request.user.user_id}

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
