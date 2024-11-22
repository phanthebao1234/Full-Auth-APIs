from rest_framework import serializers
from .models import Social, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class SocialSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
            child=serializers.ImageField(allow_empty_file=False, use_url=False),
            write_only=True
        )
    
    class Meta:
        model = Social
        fields = ('id', 'title', 'description', 'photos', 'uploaded_images')
        

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        social = Social.objects.create(**validated_data)

        for image in uploaded_images:
            Photo.objects.create(album=social, image=image)

        return social
