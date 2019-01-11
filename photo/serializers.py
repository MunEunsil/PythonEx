from .models import Photo
from rest_framework import serializers

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'  #언더바두개임!!!  어떤 필드를 보여줄 지 결정 all로 했으니까 모든게 보임


