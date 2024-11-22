from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Social, Photo
from .serializers import SocialSerializer, PhotoSerializer

@api_view(['POST'])
def create_album(request):
    if request.method == 'POST':
        serializer = SocialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SocialList(generics.ListAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()
    
class PhotoList(generics.ListAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

class SocialDetailUser(generics.ListAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.filter()