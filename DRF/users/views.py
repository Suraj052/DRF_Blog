
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewUser
from .serializers import CustomUserSerializer,UserSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated,AllowAny



# Create your views here.
class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserList(generics.ListCreateAPIView):
    queryset = NewUser.objects.all() 
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
