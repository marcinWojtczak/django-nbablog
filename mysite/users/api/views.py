from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers 
from users.models import Profile
from django.contrib.auth.models import User
from rest_framework import generics
from . permissions import IsOwnerOrReadOnly


@api_view(['POST'])
def register_view(request):

    if request.method == "POST":
        serializer = serializers.RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return serializers.Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserProfileSerializer
    lookup_field = 'pk'


class UserProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'

    

        
        
